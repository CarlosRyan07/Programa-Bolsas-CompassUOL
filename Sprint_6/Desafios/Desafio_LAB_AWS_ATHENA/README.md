
Nesse Desafio usaremos AWS Athena e criaremos uma pasta chamada queries no nosso Bucket para armazenar as consultas executadas.

### Etapa 1: Configurar Athena

<img src="https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_6/Desafios/Desafio_LAB_AWS_ATHENA/Evidencias/1_CriadaPastaQueries.png" witgh=600>

Aqui criei a pasta que irá armazenar nossas queries no bucket que criamos no desafio anterior.

### Etapa 2: Criar um banco de dados

<img src="https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_6/Desafios/Desafio_LAB_AWS_ATHENA/Evidencias/2_CriadoMeuBanco.png" witgh=600>

Aqui criei um banco de dados chamado "meubanco" e uma tabela chamada "nomes".


### Etapa 3: Criar uma tabela

<img src="https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_6/Desafios/Desafio_LAB_AWS_ATHENA/Evidencias/3_TabelaCriadaAthena.png" witgh=600>

Aqui rodando pequeno teste um teste:

<img src="https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_6/Desafios/Desafio_LAB_AWS_ATHENA/Evidencias/4_QueryRodando.png" witgh=600>

E aqui abaixo uma consulta que lista os 3 nomes mais usados em cada década desde o 1950 até hoje.

<img src="https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_6/Desafios/Desafio_LAB_AWS_ATHENA/Evidencias/5_QueryNomes.png" witgh=600>

utilizando a seguinte query:
    
        WITH RankedNames AS (
        SELECT
            nome,
            total,
            ano,
            CAST(((ano / 10) * 10) AS INTEGER) AS decada,
            ROW_NUMBER() OVER (PARTITION BY CAST(((ano / 10) * 10) AS INTEGER) ORDER BY total DESC) AS rank
        FROM
            meubanco
        WHERE
            ano >= 1950
        )

        SELECT
            decada,
            nome,
            total
        FROM
            RankedNames
        WHERE
            rank <= 3
        ORDER BY
            decada,
            rank;
