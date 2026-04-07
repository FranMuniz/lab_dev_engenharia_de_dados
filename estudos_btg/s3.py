# Testes de upload para o s3

import boto3
import os
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

# Pegaa as variáveis
access_key = os.getenv('ACCESS_KEY')
secret_key = os.getenv('SECRET_KEY')
region =  'us-east-2'
bucket = 'fran-muniz-studies'

# Variáveis extras
file_path = 'estudos_btg/arquivos/Manual Financiamento Caixa.pdf'

# Cria cliente S3
s3 = boto3.client(
    's3',
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name=region
)

# Upload
s3.upload_file(
    file_path,
    bucket,
    'caixa/financiamento'
)

print(f'Upload do arquivo {file_path} no bucket {bucket} finalizado com sucesso :)')