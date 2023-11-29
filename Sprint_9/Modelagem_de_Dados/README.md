## Tarefa 1 - Modelagem Relacional 

Nessa tarefa prática relacionado a modelagem relacional, recebemos um modelo desnormalizado para aplicarmos as formas normais.

O modelo que recebi estava assim:

![Modelo Desnormalizado](https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_9/Modelagem_de_Dados/Evidencias/Modelo_Desnormalizado.png)


E agora temos de aplicar as Formas de Normalização. 

A normalização é um processo de organização de dados em um banco de dados relacional para reduzir a redundância e melhorar a integridade dos dados. As formas normais (FN) são diretrizes para a normalização. Aqui, aplicaremos até a Terceira Forma Normal (3NF):

## 1ª Forma Normal (1NF)

Garantir que cada célula da tabela contenha apenas valores atômicos. A nossa tabela tb_locacao já está na 1NF, pois cada coluna contém apenas valores individuais e atômicos.

## 2ª Forma Normal (2NF)

Se ja estiver garantido que a nossa tabela esteja na 1NF, vamos remover dependências parciais, ou seja, garantir que todos os atributos não chave dependam totalmente da chave primária.

Em outras palavras as informações relacionadas ao cliente como:
(nomeCliente, cidadeCliente, estadoCliente, paisCliente) foram movidas para a tabela Cliente.
As informações relacionadas ao combustivel foram movidas para a tabela Combustivel.
As informações relacionadas ao carro foram movidas para a tabela Carro.
As informações relacionadas ao vendedor foram movidas para a tabela Vendedor.

## 3ª Forma Normal (3NF)

Garantir que a tabela esteja na 2NF e remover dependências transitivas, ou seja, garantir que todos os atributos não chave sejam independentes uns dos outros.

Na tabela original, não havia dependências transitivas a serem tratadas. As dependências foram tratadas na 2NF, e a tabela resultante já atende aos requisitos da 3NF.

E após aplicar as formas normais, o modelo ficou assim:

![Modelo Normalizado](https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_9/Modelagem_de_Dados/Evidencias/Modelo_Nomalizado.png)


OBS❗: abaixo vou deixar algumas observações que fiz durante a tarefa, observações que estão presentes no  arquivo.sql [tarefa 1](https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/7bc5fa531341815df516ef3c245334d68de92937/Sprint_9/Modelagem_de_Dados/tarefa1_Modelo_Relacional.sqlite), porém resolvi dar um destaque pra eles aqui também.

Na Tabela Locacao temos a coluna dataLocacao DATETIME porém também temos a coluna horas locacao. 

Vendo isso eu mudei o tipo de DATETIME para DATE, pois no DATETIME também estão presentes os horarios, e já temos a coluna horasLocacao para isso, fazendo isso economiza mais memoria quando falamos de grandes estrutura de dados.

Ainda sobre essa coluna e também sobre a coluna dataEntrega,
os dados dessas tabelas estavam vindo desse jeito Ex: 20.150.101.
Então fiz uma lógica para elas ficarem no formato tradicional(YY-MM-DD).


## Tarefa 2 - Modelagem Dimensional 


As tabelas dimensionais em um modelo dimensional, como parte de um Data Warehouse, são projetadas para responder a perguntas analíticas sobre os dados armazenados. Especificamente, as tabelas dimensionais facilitam a análise de dados em várias dimensões, permitindo que os usuários façam perguntas complexas e explorem padrões nos dados. Aqui estão alguns exemplos de perguntas que podem ser respondidas usando tabelas dimensionais:

**Quem? (Dimensão Cliente e Dimensão Vendedor)**

Quem são nossos clientes mais frequentes?
Quem são os vendedores mais bem-sucedidos em termos de vendas?

**O quê? (Dimensão Carro)**

Quais são os modelos de carro mais alugados?
Qual é a média de quilometragem dos carros alugados?

**Quando? (Dimensão Tempo)**

Quais são os padrões sazonais nas locações ao longo do ano?
Em que dias da semana as locações são mais frequentes?

**Quanto? (Medidas na Tabela FatoLocacao)**

Qual é o valor total das locações em um determinado período?
Qual é a quantidade média de diárias por locação?

usando essa logica criei as [Views](https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_9/Modelagem_de_Dados/tarefa2_ModeloDimensional_Views.sqlite).

E depois com base nelas, criamos nossas [Tabelas](https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_9/Modelagem_de_Dados/tarefa2_ModeloDimensional_Tables.sqlite). 

Assim formando o nosso **Modelo Estrela**, É um modelo dimensional comumente implantado em banco de dados relacionais. Caracteriza-se por tabelas fatos associadas à dimensões por meio de chaves estrangeiras.
O nome “Estrela” se dá devido à disposição em que se encontram as tabelas, sendo a tabela fato centralizada relacionando-se com diversas outras tabelas de dimensão. 

Esse tipo de modelo é eficiente para consultas analíticas e relatórios, pois facilita a análise de dados em várias dimensões. Além disso, o modelo estrela é flexível e escalável, o que o torna uma escolha popular em ambientes de data warehousing.

E aqui esta como ficou nosso Modelo Estrela:

![Modelo Estrela](https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_9/Modelagem_de_Dados/Evidencias/Modelo_Dimensional_Estrela.png)

OBS: não sei se era pra ter criado as tabelas mesmo ou apenas ligar as relaçoes nas views desse jeito:

![Modelo Estrela](https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_9/Modelagem_de_Dados/Evidencias/View_estrela.png)

Duvida aqui Isa❗❗❗

