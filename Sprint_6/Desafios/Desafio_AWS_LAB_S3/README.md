
Aqui iremos Explorar as capacidades do serviço AWS S3. Nesse desafio fizemos configurações necessárias para que um bucket do Amazon S3 funcione como hospedagem de conteúdo estático.

### Etapa 1: Criar um bucket

<img src="https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_6/Desafios/Desafio_AWS_LAB_S3/Evidencias/1_BucketCriado.png" witgh=600>

### Etapa 2: Habilitar hospedagem de site estático

<img src="https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_6/Desafios/Desafio_AWS_LAB_S3/Evidencias/2_SiteEstaticoHospedado.png" witgh=600>

### Etapa 3: editar as configurações do Bloqueio de acesso público

<img src="https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_6/Desafios/Desafio_AWS_LAB_S3/Evidencias/3_AcessoAoPublico.png" witgh=600>

### Etapa 4: Adicionar política de bucket que torna o conteúdo do bucket publicamente disponível

<img src="https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_6/Desafios/Desafio_AWS_LAB_S3/Evidencias/4_PoliticaDoBucket.png" witgh=600>

### Etapa 5: Configurar um documento de índice

aqui criamos um arquivo local com o nome index.html .O conteúdo do arquivo deverá ser:

        <html xmlns="http://www.w3.org/1999/xhtml" >
        <head>
            <title>Home Page do meu WebSite - Tutorial de S3</title>
        </head>
        <body>
        <h1>Bem-vindo ao meu website</h1>
        <p>Agora hospedado em Amazon S3!</p>
        <a href="nomes.csv">Download CSV File</a> 
        </body>
        </html>

<img src="https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_6/Desafios/Desafio_AWS_LAB_S3/Evidencias/5_AdicionandoItens.png" witgh=600>

Nessa etapa também foi pedido para criar uma pasta chamada dados e, após, fazer upload do conteúdo do site (arquivo CSV) para ela, e isso acabou acarretando em erros com a ultima etapa pois como adicionamos o arquivo na pasta dados, temos que alterar ali em cima o nomes.csv para dados/nomes.csv.

OBS: aqui ja está com todos os itens do final desse desafio pois, acabei esquecendo de tirar print dessa parte 😅.

### Etapa 6: Configurar documento de erros

<img src="https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_6/Desafios/Desafio_AWS_LAB_S3/Evidencias/6_erroAdicionado.png" witgh=600>

### Etapa 7: Testar o endpoint do site

<img src="https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_6/Desafios/Desafio_AWS_LAB_S3/Evidencias/7_SiteFuncionando.png" witgh=600>

E com isso agora temos um site hospedado no Amazon S3. Esse site está disponível publicamente no endpoint de site do Amazon S3.