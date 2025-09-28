import requests
import pandas as pd
import boto3
import os
from datetime import datetime, timedelta

# Configurações
API_KEY = "FRAN123"
symbol = "AAPL"

s3 = boto3.resource(
    "s3",
    endpoint_url="http://localhost:9000",
    aws_access_key_id="admin",
    aws_secret_access_key="franadmin",
    region_name="us-east-1"
)
bucket_name = "raw-api-data"
os.makedirs("temp_csvs", exist_ok=True)

# Simular datas (com gaps)
start_date = datetime(2025, 9, 1)
end_date = datetime(2025, 9, 10)
todas_datas = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]

# Criar gaps: datas que NÃO terão arquivos
datas_faltando = ["2025-09-03", "2025-09-07"]

# Definir quantas linhas por data
linhas_por_dia = {
    "2025-09-01": 10,
    "2025-09-02": 15,
    "2025-09-04": 5,
    "2025-09-05": 12,
    "2025-09-06": 8,
    "2025-09-08": 20,
    "2025-09-09": 10,
    "2025-09-10": 7
}

# Consumir API (ou gerar dados simulados)
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=compact&apikey={API_KEY}"
response = requests.get(url)
data = response.json()
if "Time Series (Daily)" in data:
    ts_data = data["Time Series (Daily)"]
    df_api = pd.DataFrame(ts_data).T.astype(float)
else:
    print("Erro ou limite de requisições, gerando dados simulados")
    df_api = pd.DataFrame(columns=["1. open","2. high","3. low","4. close","5. volume"])

# Criar bucket se não existir
if bucket_name not in [b.name for b in s3.buckets.all()]:
    s3.create_bucket(Bucket=bucket_name)
    print(f"Bucket '{bucket_name}' criado com sucesso.")

# Gerar arquivos por data
for data_obj in todas_datas:
    date_str = data_obj.strftime("%Y-%m-%d")
    if date_str in datas_faltando:
        print(f"Pulando {date_str} (gap simulado)")
        continue

    # Obter linha do API ou criar simulada
    if date_str in df_api.index:
        row = df_api.loc[date_str]
    else:
        row = pd.Series({"1. open": 100, "2. high": 105, "3. low": 95, "4. close": 102, "5. volume": 1000})

    n_linhas = linhas_por_dia.get(date_str, 1)
    df_day = pd.DataFrame([row + pd.Series({
        "1. open": i*0.1, "2. high": i*0.1, "3. low": i*0.1, "4. close": i*0.1, "5. volume": i*10
    }) for i in range(n_linhas)]).reset_index()
    df_day.rename(columns={"index":"data"}, inplace=True)
    df_day["data"] = date_str  # garantir que todas as linhas tenham a mesma data

    arquivo_csv = f"temp_csvs/raw_api_{symbol}_{date_str}.csv"
    df_day.to_csv(arquivo_csv, index=False)

    s3.Bucket(bucket_name).upload_file(arquivo_csv, f"raw_api/{arquivo_csv.split('/')[-1]}")
    print(f"Arquivo '{arquivo_csv}' enviado com {n_linhas} linhas")
