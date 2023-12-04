import sys
from datetime import datetime
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.transforms import *
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from pyspark.sql.functions import col
 
# Local aonde quero inserir os Dados
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
output_path_details = "s3://ryan-desafio-bucket/Trusted/TMDB/Crime/{}/{}/{}/Movie".format(
    datetime.now().strftime('%Y'),
    datetime.now().strftime('%m'),
    datetime.now().strftime('%d')
)
 
# Inicialização do contexto Glue
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
 
# Ler os dados
details_data = spark.read.json("s3://ryan-desafio-bucket/Raw/Local/JSON/2023/11/17/*.json")
 
# Remover a coluna "adult"
details_data = details_data.drop("adult")
 
# Remover linhas com valores nulos (NaN ou null)
details_data = details_data.na.drop()
 
# Salvar dados transformados no formato Parquet
details_data.write.mode("overwrite").parquet(output_path_details)

job.commit()
