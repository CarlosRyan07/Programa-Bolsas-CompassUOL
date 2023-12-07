
## Desafio Parte 3

Aqui retomamos com o nosso desafio final pela 3 vez, no ultimo passo do desafio, injetamos dados de filmes de crime .json no nosso s3 na camada Raw, e agora vamos dar o prosseguimento.

## Processamento -  Camada Trusted

Aqui vamos fazer o processamento dos dados que estão na camada Raw, e vamos injetar os dados na camada Trusted.

A camada Trusted de um data lake corresponde àquela em que os dados encontram-se limpos e são confiáveis. É resultado da integração das diversas fontes de origem, que encontram-se na camada anterior, que chamamos de Raw.

Aqui faremos uso do Apache Spark no processo, integrando dados existentes na camada Raw Zone. O objetivo é gerar uma visão padronizada dos dados, persistida no S3,  compreendendo a Trusted Zone do data lake.  Nossos jobs Spark serão criados por meio do AWS Glue.

Todos os dados serão persistidos na Trusted no formato PARQUET, que é um formato colunar, otimizado para processamento analítico.  O formato PARQUET é o formato mais utilizado em data lakes, pois permite a execução de queries SQL de forma eficiente, além de ser um formato colunar, que permite a leitura de colunas específicas, sem a necessidade de leitura de todas as colunas, como ocorre em formatos como CSV.

e aqui está o codigo que utilizei nos jobs do Glue utilizando a opção Spark script editor: [Processamento na camada Trusted](https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_9/Desafio_Parte_3/processamentoTrusted.py)

Aqui os logs do codigo:

![Logs](https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_9/Desafio_Parte_3/Evidencias/Logs_Processamento_Trusted.png)

## Modelagem de dados - Camada Refined

Aqui vamos fazer a modelagem dos dados que estão na camada Trusted, e vamos injetar os dados na camada Refined.
A camada Refined corresponde à camada de um data lake em que os dados estão prontos para análise e extração de insights. Sua origem corresponde aos dados da camada anterior, a Trusted.

Devemos pensar em estruturar os dados seguindo os princípios de modelagem multidimensional, a fim de permitir consultas sobre diferentes perspectivas.

Nesta etapa do desafio, devemos fazer a modelagem de dados da camada refined, definindo as tabelas e, se necessário, views, a fim de disponibilizar os dados para a ferramenta de visualização (QuickSight, a partir da próxima Sprint). 

![Modelagem](https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_9/Desafio_Parte_3/Evidencias/ModelagemRefined.png)


