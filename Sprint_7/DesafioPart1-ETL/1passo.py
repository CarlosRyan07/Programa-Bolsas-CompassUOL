import boto3
import os
from datetime import datetime
 
AWS_ACCESS_KEY_ID = 'AKIAW6Q6ZOWBQIRLH3UA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_REGION = 'us-east-1'
 
NOME_DO_BUCKET_S3 = 'ryan-desafio-bucket'
ZONA_RAW = 'Raw/Local/CSV'
data_atual = datetime.now().strftime('%Y/%m/%d')
 
caminho_local_filmes_csv = 'files/movies.csv'
caminho_local_series_csv = 'files/series.csv'
 
s3 = boto3.client('s3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)
 

chave_s3_filmes = f"{ZONA_RAW}/Movies/{data_atual}/{os.path.basename(caminho_local_filmes_csv)}"
chave_s3_series = f"{ZONA_RAW}/Series/{data_atual}/{os.path.basename(caminho_local_series_csv)}"
 
s3.upload_file(caminho_local_filmes_csv, NOME_DO_BUCKET_S3, chave_s3_filmes)
s3.upload_file(caminho_local_series_csv, NOME_DO_BUCKET_S3, chave_s3_series)
 
print("Arquivos CSV enviados com sucesso para o S3.")
