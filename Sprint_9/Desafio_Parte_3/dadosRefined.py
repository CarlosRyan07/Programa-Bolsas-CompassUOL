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

# Lista de nomes de dimensões
dimensoes = ['dim_data', 'dim_genero', 'dim_idioma', 'dim_empresa_producao', 'dim_pais_producao', 'dim_filme']

# Criação e gravação das dimensões
for dimensao in dimensoes:
    if dimensao == 'dim_data':
        df = parquet_data.select(
            col("release_date").alias("data_lancamento"),
            year("release_date").alias("ano"),
            month("release_date").alias("mes"),
            dayofmonth("release_date").alias("dia")
        ).distinct()
        output_path = f"s3://ryan-desafio-bucket/Refined/{dimensao}/"
        df.write.mode("overwrite").parquet(output_path)
    elif dimensao == 'dim_genero':
        df = parquet_data.select(
            explode("genres").alias("genre")
        ).distinct()
        df = df.select(
            col("genre.id").alias("id_genero"),
            col("genre.name").alias("nome_genero")
        )
        output_path = f"s3://ryan-desafio-bucket/Refined/{dimensao}/"
        df.write.mode("overwrite").parquet(output_path)
    elif dimensao == 'dim_empresa_producao':
        df = parquet_data.select(
            explode("production_companies").alias("production_company")
        ).distinct()
        df = df.select(
            col("production_company.id").alias("id_empresa_producao"),
            col("production_company.logo_path").alias("logo_path_empresa_producao"),
            col("production_company.name").alias("nome_empresa_producao"),
            col("production_company.origin_country").alias("pais_origem_empresa_producao")
        )
        output_path = f"s3://ryan-desafio-bucket/Refined/{dimensao}/"
        df.write.mode("overwrite").parquet(output_path)
    elif dimensao == 'dim_pais_producao':
        df = parquet_data.select(
            explode("production_countries").alias("production_country")
        ).distinct()
        df = df.select(
            col("production_country.iso_3166_1").alias("id_pais_producao"),
            col("production_country.name").alias("nome_pais_producao")
        )
        output_path = f"s3://ryan-desafio-bucket/Refined/{dimensao}/"
        df.write.mode("overwrite").parquet(output_path)
    elif dimensao == 'dim_filme':
        df = parquet_data.select(
            col("id").alias("filme_id"),
            col("original_title").alias("titulo_original"),
            col("overview").alias("sinopse"),
            col("poster_path").alias("caminho_poster"),
            col("imdb_id"),
            col("original_language").alias("idioma_original"),
            col("runtime").alias("duracao")
        )
        output_path = f"s3://ryan-desafio-bucket/Refined/{dimensao}/"
        df.write.mode("overwrite").parquet(output_path)

# Lista de nomes de tabelas de fatos
fatos = ['fato_financeiro', 'fato_popularidade']

# Loop para processar cada tabela de fato
for fato in fatos:
    if fato == 'fato_financeiro':
        df = parquet_data.select(
            col("id").alias("filme_id"),
            col("revenue").alias("receita"),
            col("budget").alias("orcamento"),
            col("release_date").alias("data_lancamento"),
            col("original_language").alias("idioma_original"),
            "genres",
            "production_companies",
            "production_countries"
        ).withColumn("genre", explode("genres")).withColumn("production_company", explode("production_companies")).withColumn("production_country", explode("production_countries")).drop("genres", "production_companies", "production_countries")
        
        # Extrair os campos específicos da estrutura aninhada para production_company e production_country
        df = df.select(
            "filme_id",
            "receita",
            "orcamento",
            "data_lancamento",
            "idioma_original",
            col("genre.id").alias("id_genero"),
            col("genre.name").alias("nome_genero"),
            col("production_company.id").alias("id_empresa_producao"),
            col("production_company.name").alias("nome_empresa_producao"),
            col("production_country.iso_3166_1").alias("id_pais_producao"),
            col("production_country.name").alias("nome_pais_producao")
        )
    elif fato == 'fato_popularidade':
        df = parquet_data.select(
            col("id").alias("filme_id"),
            col("popularity").alias("popularidade"),
            col("vote_average").alias("media_votos"),
            col("vote_count").alias("contagem_votos"),
            col("release_date").alias("data_lancamento"),
            col("original_language").alias("idioma_original"),
            "genres",
            "production_companies",
            "production_countries"
        ).withColumn("genre", explode("genres")).withColumn("production_company", explode("production_companies")).withColumn("production_country", explode("production_countries")).drop("genres", "production_companies", "production_countries")
        
        # Extrair os campos específicos da estrutura aninhada para production_company e production_country
        df = df.select(
            "filme_id",
            "popularidade",
            "media_votos",
            "contagem_votos",
            "data_lancamento",
            "idioma_original",
            col("genre.id").alias("id_genero"),
            col("genre.name").alias("nome_genero"),
            col("production_company.id").alias("id_empresa_producao"),
            col("production_company.name").alias("nome_empresa_producao"),
            col("production_country.iso_3166_1").alias("id_pais_producao"),
            col("production_country.name").alias("nome_pais_producao")
        )
    
    # Defina o caminho de saída no S3 e grave os DataFrames no formato Parquet na pasta refined
    if df.columns:
        output_path = f"s3://ryan-desafio-bucket/Refined/{fato}/"
        df.write.mode("overwrite").parquet(output_path)

# Commite o Job Glue
job.commit()
