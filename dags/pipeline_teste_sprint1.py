from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine
import boto3
from botocore.client import Config

def pipeline_teste():
    minio_endpoint = "http://minio:9000"
    access_key = "admin"
    secret_key = "franadmin"

    s3 = boto3.resource(
        "s3",
        endpoint_url=minio_endpoint,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        config=Config(signature_version="s3v4"),
        region_name="us-east-1"
    )

    bucket_name = "ingestao-teste-csv"
    arquivo_teste = "teste_pipeline_e2e.csv"

    if bucket_name not in [b.name for b in s3.buckets.all()]:
        s3.create_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' criado com sucesso.")
    else:
        print(f"Bucket '{bucket_name}' já existe.")

    df_teste = pd.DataFrame({
        "id": [1, 2, 3],
        "nome": ["Fran", "Andre", "Amanda"],
        "valor": [100, 200, 300]
    })
    df_teste.to_csv(arquivo_teste, index=False)

    s3.Bucket(bucket_name).upload_file(arquivo_teste, arquivo_teste)
    print(f"Arquivo '{arquivo_teste}' enviado para o bucket '{bucket_name}'.")

    s3.Bucket(bucket_name).download_file(arquivo_teste, f"download_{arquivo_teste}")
    print(f"Arquivo '{arquivo_teste}' baixado com sucesso para 'download_{arquivo_teste}'.")

    DB_USER = "admin"
    DB_PASSWORD = "admin"
    DB_HOST = "postgres"
    DB_PORT = "5432"
    DB_NAME = "lab_dev"

    engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
    df_teste.to_sql("tabela_teste_pipeline", engine, if_exists="replace", index=False)
    print("Dados inseridos com sucesso no PostgreSQL.")

    with engine.connect() as conn:
        result = conn.execute("SELECT * FROM tabela_teste_pipeline;")
        print("\nDados inseridos no PostgreSQL:")
        for row in result.fetchall():
            print(row)

with DAG(
    dag_id="pipeline_teste_e2e",
    start_date=datetime(2025, 9, 13),
    schedule_interval="@once",
    catchup=False
) as dag:

    task_pipeline = PythonOperator(
        task_id="executar_pipeline_teste",
        python_callable=pipeline_teste
    )
