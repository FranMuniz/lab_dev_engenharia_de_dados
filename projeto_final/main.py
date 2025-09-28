# projeto_final/main.py
import os
import shutil
from datetime import datetime, timedelta
import pandas as pd
import boto3
from botocore.client import Config
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

from utils import auxiliares, carga_db, retry_fallback, validacao

# Carrega .env
load_dotenv()

def run_pipeline():
    # Configs gerais
    API_KEY = os.getenv("API_KEY")
    SYMBOL = os.getenv("SYMBOL")
    TEMP_DIR = os.getenv("TEMP_DIR", "temp_files")
    PREFIXO_CSV = os.getenv("PREFIXO_CSV", "csv/")
    PREFIXO_PARQUET = os.getenv("PREFIXO_PARQUET", "parquet/")

    # MinIO / S3 usando client
    s3 = boto3.client(
        "s3",
        endpoint_url=os.getenv("S3_ENDPOINT"),
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        config=Config(signature_version="s3v4"),
        region_name=os.getenv("AWS_REGION", "us-east-1")
    )

    BUCKET_BACKUP = os.getenv("BUCKET_BACKUP")
    BUCKET_RAW = os.getenv("BUCKET_RAW")

    # Criar buckets se não existirem
    existing_buckets = [b["Name"] for b in s3.list_buckets().get("Buckets", [])]
    for bucket_name in [BUCKET_BACKUP, BUCKET_RAW]:
        if bucket_name not in existing_buckets:
            s3.create_bucket(Bucket=bucket_name)
            print(f"Bucket '{bucket_name}' criado com sucesso.")

    # Banco de Dados
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")
    DB_SCHEMA = os.getenv("DB_SCHEMA")

    engine = create_engine(
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    # Pasta temporária
    os.makedirs(TEMP_DIR, exist_ok=True)

    # Datas do pipeline
    data_inicio = datetime(2025, 8, 1)
    data_fim = datetime(2025, 8, 10)
    datas_esperadas = [data_inicio + timedelta(days=x) for x in range((data_fim - data_inicio).days + 1)]

    # Consultar datas já existentes no Bronze
    with engine.connect() as conn:
        result = conn.execute(text(f"""
            SELECT DISTINCT data_ref 
            FROM {DB_SCHEMA}.br_alphavantage_s0_daily_raw
            WHERE data_ref BETWEEN :start AND :end
        """), {"start": data_inicio, "end": data_fim})
        datas_existentes = [row[0] for row in result.fetchall()]

    # Apenas as datas que ainda não foram baixadas
    datas_a_baixar = [d for d in datas_esperadas if d.date() not in datas_existentes]

    arquivos_backup = auxiliares.arquivos_existentes_s3(s3, BUCKET_BACKUP, PREFIXO_CSV)

    for data_ref in datas_a_baixar:
        date_str = data_ref.strftime("%Y%m%d")

        if any(date_str in arquivo for arquivo in arquivos_backup):
            continue

        df_api = retry_fallback.executar_com_retry(
            auxiliares.consumir_api, 3, 5, retry_fallback.fallback_api, SYMBOL, API_KEY
        )

        print("\n=== DEBUG API ===")
        print("Data atual:", data_ref)
        print("df_api vazio?", df_api.empty)

        encontrado = False
        if not df_api.empty:
            try:
                df_api.index = pd.to_datetime(df_api.index)
                if data_ref in df_api.index:
                    row = df_api.loc[data_ref]
                    encontrado = True
            except Exception:
                if "data_ref" in df_api.columns:
                    df_api["data_ref"] = pd.to_datetime(df_api["data_ref"])
                    match = df_api[df_api["data_ref"] == data_ref]
                    if not match.empty:
                        row = match.iloc[0]
                        encontrado = True

        if encontrado:
            df_day = row.to_frame().T if isinstance(row, pd.Series) else row.to_frame().T
            df_day.insert(0, "data_ref", data_ref.strftime("%Y-%m-%d"))

            # Renomear colunas
            df_day = df_day.rename(columns={
                "1. open": "open",
                "2. high": "high",
                "3. low": "low",
                "4. close": "close",
                "5. volume": "volume"
            })

            fake_id = auxiliares.gerar_id_fake()
            nome_base = f"raw_api_{SYMBOL}_{date_str}{fake_id}"

            arquivo_csv = os.path.join(TEMP_DIR, f"{nome_base}.csv")
            arquivo_parquet = os.path.join(TEMP_DIR, f"{nome_base}.parquet")

            df_day.to_csv(arquivo_csv, index=False)
            df_day.to_parquet(arquivo_parquet, index=False)

            # Upload
            retry_fallback.executar_com_retry(
                s3.upload_file, 3, 5, retry_fallback.fallback_upload,
                arquivo_csv, BUCKET_BACKUP, f"{PREFIXO_CSV}{nome_base}.csv"
            )
            retry_fallback.executar_com_retry(
                s3.upload_file, 3, 5, retry_fallback.fallback_upload,
                arquivo_parquet, BUCKET_RAW, f"{PREFIXO_PARQUET}{nome_base}.parquet"
            )

            # Bronze
            retry_fallback.executar_com_retry(
                carga_db.inserir_raw, 3, 5, retry_fallback.fallback_db, df_day, nome_base, engine, DB_SCHEMA
            )
        else:
            print("Nenhum dado encontrado para:", data_ref)
            carga_db.registrar_log(engine, DB_SCHEMA, data_ref, "NA", "falha")

    # Silver e Gold
    carga_db.processar_silver(engine, DB_SCHEMA)
    carga_db.processar_gold(engine, DB_SCHEMA)
    validacao.validar_consistencia(engine, DB_SCHEMA)

    # Limpeza
    # if os.path.exists(TEMP_DIR):
    #     shutil.rmtree(TEMP_DIR)
