import requests
import pandas as pd
import random
import string

def gerar_id_fake(length=5):
    return ''.join(random.choices(string.digits, k=length))

def consumir_api(symbol, api_key):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=compact&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    if "Time Series (Daily)" in data:
        ts_data = data["Time Series (Daily)"]
        df = pd.DataFrame(ts_data).T
        df.index = pd.to_datetime(df.index)
        df = df.astype(float)
        return df
    else:
        print("Erro ou limite de requisições:", data)
        return pd.DataFrame()

def arquivos_existentes_s3(s3_client, bucket, prefixo):
    """
    Retorna uma lista com os nomes dos arquivos existentes em um bucket S3/MinIO
    filtrando pelo prefixo informado.
    """
    arquivos = []
    continuation_token = None

    while True:
        if continuation_token:
            response = s3_client.list_objects_v2(
                Bucket=bucket,
                Prefix=prefixo,
                ContinuationToken=continuation_token
            )
        else:
            response = s3_client.list_objects_v2(
                Bucket=bucket,
                Prefix=prefixo
            )

        if "Contents" in response:
            arquivos.extend([obj["Key"] for obj in response["Contents"]])

        if response.get("IsTruncated"):  # se houver mais páginas
            continuation_token = response.get("NextContinuationToken")
        else:
            break

    return arquivos