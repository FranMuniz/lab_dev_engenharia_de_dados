import boto3
from botocore.client import Config

minio_endpoint = "http://localhost:9000"
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

bucket_name = "bucket-teste-fran"

if s3.Bucket(bucket_name) not in s3.buckets.all():
    s3.create_bucket(Bucket=bucket_name)
    print(f"Bucket '{bucket_name}' criado com sucesso!")

file_name = "exemplo.csv"
with open(file_name, "w") as f:
    f.write("id,nome,idade\n1,Ana,25\n2,Carlos,30\n3,João,28")

s3.Bucket(bucket_name).upload_file(file_name, file_name)
print(f"Arquivo '{file_name}' enviado para o bucket '{bucket_name}'!")
