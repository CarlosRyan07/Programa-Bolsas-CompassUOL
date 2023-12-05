import sys
from datetime import datetime
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext

# Local onde quero inserir os Dados
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

try:
    print("Lendo dados JSON...")
    # Ler todos os arquivos JSON usando um wildcard
    details_data = spark.read.option("multiline", "true").json("s3://ryan-desafio-bucket/Raw/Local/JSON/2023/11/17/*.json")

    print("Aplicando transformações...")
    # Continuar com as transformações necessárias
    details_data = details_data.drop("adult").na.drop()

    print("Salvando dados transformados no formato Parquet...")
    # Salvar dados transformados no formato Parquet
    details_data.write.mode("overwrite").parquet(output_path_details)

    print("Operação concluída com sucesso!")

except Exception as e:
    print("Erro ao processar os dados:", str(e))
    # Adicione qualquer outra lógica de tratamento de erro necessária

job.commit()
