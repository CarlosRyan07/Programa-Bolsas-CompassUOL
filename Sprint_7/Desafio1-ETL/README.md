
### Desafio Parte 1 - ETL


Aqui tivemos o Desafio de criar código Python que carrega arquivos CSV para a Nuvem utilizando as técnicas de ETL.


1) Implementar código Python:

- ler os 2 arquivos (filmes e series) no formato CSV inteiros, ou seja, sem filtrar os dados

- utilizar a lib boto3 para carregar os dados para a AWS

- acessar a AWS e grava no S3, no bucket definido com RAW Zone

- no momento da gravação dos dados deve-se considerar o padrão: <nome do bucket>\<camada de armazenamento>\<origem do dado>\<formato do dado>\<especificação do dado>\<data de processamento separada por ano\mes\dia>\<arquivo>

Por exemplo:

S3:\\data-lake-do-fulano\Raw\Local\CSV\Movies\2022\05\02\movies.csv

S3:\\data-lake-do-fulano\Raw\Local\CSV\Series\2022\05\02\series.csv

Utilizei o seguinte código:

    1passo.py

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
 

2) Criar container Docker com um volume para armazenar os arquivos CSV e executar processo Python implementado.
3) Executar localmente o container docker para realizar a carga dos dados ao S3.

E aqui está essas 2 questões respondidas:

![Docker Run Desafio](https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_7/Desafio1-ETL/Evidencias/DockerRunDesafio.png){width=600}

E os Arquivos enviados para o bucket S3:

![Movies Enviados](https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_7/Desafio1-ETL/Evidencias/Movies_Enviados.png){width=600}


![Series Enviados](https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_7/Desafio1-ETL/Evidencias/Series_Enviados.png){width=600}

