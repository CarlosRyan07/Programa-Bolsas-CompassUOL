## Ingestão de dados no S3 com Lambda

Aqui criamos a função lambda:

<img src="https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_8/DesafioPart2-Ingestao_de_dados_TMDB/Evidencias/1_FuncaoLambda_Criada.png" width=600>


Aqui damos as devidas permições que no caso é PutObject e criamos uma nova Politica:

<img src="https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_8/DesafioPart2-Ingestao_de_dados_TMDB/Evidencias/2_Permissoes_Dadas.png" width=600>

E então a Anexamos:

<img src="https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_8/DesafioPart2-Ingestao_de_dados_TMDB/Evidencias/3_Politica_Anexada.png" width=600>

Código utilizado no Lambda você o encontra clicando aqui: [ingestãoLambda.py](https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_8/DesafioPart2-Ingestao_de_dados_TMDB/ingestaoLambda.py)

Apos rodarmos o codigo da função lambda, vamos ver os logs da sua execução  no CloudWatch Logs:

<img src="https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_8/DesafioPart2-Ingestao_de_dados_TMDB/Evidencias/Resultado_Logs.png" width=600>

Aqui podemos observar os arquivos JSON no nosso bucket do S3:
<img src="https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_8/DesafioPart2-Ingestao_de_dados_TMDB/Evidencias/Objetos_no_Bucket.png" width=600>

Aqui um exemplo de um dos arquivos presente dentro dos arquivos JSON: [filmes_arquivo_1.jason](https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_8/DesafioPart2-Ingestao_de_dados_TMDB/filmes_arquivo_1.json)

Os arquivos de filmes que eu selecionei da página do TMDB foram com o seguinte filtro: 
        
        Filmes do gênero Crimes, mais populares de 2018 até os dias atuais, com uma quantidade minima de votos a partir de 10.