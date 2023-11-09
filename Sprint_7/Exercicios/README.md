
# Exercícios

Aqui tivemos 2 Exercicios para fazer.

O 1° nos foi pedido para utilizarmos as bibliotecas Pandas e NumPy para responder a quatro exercícios.
Estes que você pode encontrar aqui: [Exercicio com Pandas e Numpy](https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_7/Exercicios/Python_Pandas_Numpy.ipynb)

A 2° foi a Contagem de a Palavras, neste atividade desenvolvemos um job de processamento com o framework Spark por meio de um container Docker.

        docker exec -it f45a008a8555bb22b7edd84aa72045dccd86248ab8654b7a45e89344b8e6e700 pyspark


Utilizei o seguinte código:

        spark-shell
        val textoRDD = sc.textFile("README.md")

        val palavrasRDD = textoRDD.flatMap(linha => linha.split(" "))
        val paresRDD = palavrasRDD.map(palavra => (palavra, 1))
        val contagemRDD = paresRDD.reduceByKey((a, b) => a + b)
        contagemRDD.collect().foreach(println)

E aqui esta a imagem do codigo sendo utilizado e a resposta da contagem:

<img src="https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_7/Exercicios/Evidencias/ContagemPalavras.png" width= 800>