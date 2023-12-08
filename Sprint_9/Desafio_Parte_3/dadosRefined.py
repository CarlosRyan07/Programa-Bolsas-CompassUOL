import sys
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from pyspark.sql.functions import col, year, month, dayofmonth, explode

# Inicialização do contexto Glue
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

# Parâmetros do Job Glue
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
job.init(args['JOB_NAME'], args)

# Caminho para os dados Parquet
parquet_path = "s3://ryan-desafio-bucket/Trusted/TMDB/Crime/2023/12/08/Movie/"

# Leitura dos dados Parquet
parquet_data = spark.read.parquet(parquet_path)

# Lista de nomes de tabelas
tabelas = ['dim_data', 'fato_financeiro', 'fato_popularidade', 'dim_genero', 'dim_idioma', 'dim_empresa_producao', 'dim_pais_producao', 'dim_filme']

# Loop para processar cada tabela
for tabela in tabelas:
    # Selecione as colunas necessárias e realize as transformações
    if tabela == 'dim_data':
        df = parquet_data.select(
            col("release_date").alias("data_lancamento"),
            year("release_date").alias("ano"),
            month("release_date").alias("mes"),
            dayofmonth("release_date").alias("dia")
        ).distinct()
    elif tabela == 'fato_financeiro':
        df = parquet_data.select(
            col("id").alias("filme_id"),
            "revenue",
            "budget",
            "release_date",
            "genres",
            "original_language",
            "production_companies",
            "production_countries"
        ).withColumn("genre", explode("genres")).withColumn("production_company", explode("production_companies")).withColumn("production_country", explode("production_countries")).drop("genres", "production_companies", "production_countries")
    elif tabela == 'fato_popularidade':
        df = parquet_data.select(
            col("id").alias("filme_id"),
            "popularity",
            "vote_average",
            "vote_count",
            "release_date",
            "genres",
            "original_language",
            "production_companies",
            "production_countries"
        ).withColumn("genre", explode("genres")).withColumn("production_company", explode("production_companies")).withColumn("production_country", explode("production_countries")).drop("genres", "production_companies", "production_countries")
    elif tabela == 'dim_genero':
        df = parquet_data.select(
            explode("genres").alias("genre")
        ).distinct()
    elif tabela == 'dim_idioma':
        df = parquet_data.select(
            col("original_language").alias("nome_idioma")
        ).distinct()
    elif tabela == 'dim_empresa_producao':
        df = parquet_data.select(
            explode("production_companies").alias("production_company")
        ).distinct()
    elif tabela == 'dim_pais_producao':
        df = parquet_data.select(
            explode("production_countries").alias("production_country")
        ).distinct()
    elif tabela == 'dim_filme':
        df = parquet_data.select(
            col("id").alias("filme_id"),
            col("original_title").alias("titulo_original"),
            col("overview").alias("sinopse"),
            col("poster_path"),
            col("imdb_id"),
            col("runtime")
        ).drop("tagline", "homepage")  # Remover colunas indesejadas

    # Defina o caminho de saída no S3
    output_path = f"s3://ryan-desafio-bucket/Refined/{tabela}/"

    # Grave os DataFrames no formato Parquet na pasta refined
    df.write.mode("overwrite").parquet(output_path)

# Commite o Job Glue
job.commit()
