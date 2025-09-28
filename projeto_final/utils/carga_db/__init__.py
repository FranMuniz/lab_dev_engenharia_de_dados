from sqlalchemy import text
from datetime import datetime

def registrar_log(engine, schema, data_ref, file_name, status):
    with engine.begin() as conn:  # begin() já faz commit automático
        conn.execute(
            text(f"""
                INSERT INTO {schema}.br_alphavantage_s0_file_log
                (data_ref, file_name, status, processed_at)
                VALUES (:data_ref, :file_name, :status, CURRENT_TIMESTAMP)
            """),
            {"data_ref": data_ref, "file_name": file_name, "status": status}
        )

def inserir_raw(df, file_name, engine, schema):
    try:
        df["file_name"] = file_name
        df["grass_date"] = datetime.today().date()
        df["ingestion_timestamp"] = datetime.now()

        df.to_sql(
            "br_alphavantage_s0_daily_raw",
            engine,
            schema=schema,
            if_exists="append",
            index=False,
            method="multi"  # mais eficiente em inserts grandes
        )
        registrar_log(engine, schema, df['data_ref'].iloc[0], file_name, "sucesso")
        print(f"[BRONZE] Arquivo {file_name} carregado com sucesso.")
    except Exception as e:
        registrar_log(engine, schema, df['data_ref'].iloc[0], file_name, "falha")
        print(f"[BRONZE][ERRO] Falha ao carregar {file_name}: {e}")

def processar_silver(engine, schema):
    query = f"""
    INSERT INTO {schema}.br_alphavantage_s0_daily_live 
    (data_ref, open, high, low, close, volume, file_name, grass_date, ingestion_timestamp)
    SELECT DISTINCT data_ref, open, high, low, close, volume, file_name, CURRENT_DATE, CURRENT_TIMESTAMP
    FROM {schema}.br_alphavantage_s0_daily_raw
    ON CONFLICT (data_ref) DO NOTHING
    """
    with engine.begin() as conn:  # begin() cuida do commit
        conn.execute(text(query))
    print("[SILVER] Dados carregados e duplicatas removidas.")

def processar_gold(engine, schema):
    query = f"""
    INSERT INTO {schema}.br_alphavantage_s0_daily_refined 
    (data_ref, avg_price, total_volume, file_name, grass_date, ingestion_timestamp)
    SELECT
        data_ref,
        (open + high + low + close)/4 AS avg_price,
        SUM(volume) AS total_volume,
        MIN(file_name) AS file_name,
        CURRENT_DATE AS grass_date,
        CURRENT_TIMESTAMP AS ingestion_timestamp
    FROM {schema}.br_alphavantage_s0_daily_live
    GROUP BY data_ref
    ON CONFLICT (data_ref) DO NOTHING
    """
    with engine.begin() as conn:
        conn.execute(text(query))
    print("[GOLD] Agregações realizadas e carregadas.")
