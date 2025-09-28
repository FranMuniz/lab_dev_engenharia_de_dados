import pandas as pd
import boto3
import os
from datetime import datetime, timedelta

# Configurações
symbol = "AAPL"
bucket_name = "raw-api-data"
s3_prefix = "raw_api/"
os.makedirs("temp_csvs", exist_ok=True)

s3 = boto3.resource(
    "s3",
    endpoint_url="http://localhost:9000",
    aws_access_key_id="admin",
    aws_secret_access_key="franadmin",
    region_name="us-east-1"
)

# Datas do período que queremos ter arquivos
start_date = datetime(2025, 9, 1)
end_date = datetime(2025, 9, 10)
todas_datas = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]
datas_str = [d.strftime("%Y-%m-%d") for d in todas_datas]

# Criar bucket se não existir
if bucket_name not in [b.name for b in s3.buckets.all()]:
    s3.create_bucket(Bucket=bucket_name)
    print(f"Bucket '{bucket_name}' criado com sucesso.")

# Listar arquivos existentes no S3
bucket = s3.Bucket(bucket_name)
arquivos_existentes = [obj.key for obj in bucket.objects.filter(Prefix=s3_prefix)]
datas_existentes = [k.split("_")[-1].replace(".csv","") for k in arquivos_existentes]

# Detectar gaps
datas_faltando = [d for d in datas_str if d not in datas_existentes]
print("Datas faltando:", datas_faltando)

# Definir quantas linhas por data
linhas_por_dia = {d: 10 for d in datas_str}  # exemplo: 10 linhas por dia

# Gerar arquivos faltantes
for date_str in datas_faltando:
    # Criar DataFrame com pequenas variações para cada linha
    n_linhas = linhas_por_dia.get(date_str, 1)
    df_day = pd.DataFrame([{
        "data": date_str,
        "open": 100 + i*0.1,
        "high": 105 + i*0.1,
        "low": 95 + i*0.1,
        "close": 102 + i*0.1,
        "volume": 1000 + i*10
    } for i in range(n_linhas)])

    # Salvar CSV local
    arquivo_csv = f"temp_csvs/raw_api_{symbol}_{date_str}.csv"
    df_day.to_csv(arquivo_csv, index=False)

    # Upload para S3
    s3.Bucket(bucket_name).upload_file(arquivo_csv, f"{s3_prefix}{arquivo_csv.split('/')[-1]}")
    print(f"Arquivo '{arquivo_csv}' gerado e enviado para o S3 com {n_linhas} linhas")
