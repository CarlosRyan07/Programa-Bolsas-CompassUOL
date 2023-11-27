## Modelagem Relacional 

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


OBS❗:ABAIXO ALTERAÇÔES QUE EU FIZ E NÃO SEI SE ESTÃO CORRETAS: 

Na Tabela Locacao temos a coluna dataLocacao DATETIME porém tbm temos a coluna horas locacao. 

Vendo isso eu mudei o tipo de DATETIME para DATE ,pois no DATETIME também estão presentes os horarios, e já temos a coluna horasLocacao para isso, fazendo isso economiza mais memoria quando falamos de grandes estrutura de dados.

Ainda sobre essa coluna e também sobre a coluna dataEntrega,
os dados dessas tabelas estavam vindo desse jeito Ex: 20.150.101.
Então fiz uma lógica para elas ficarem no formato tradicional(YY-MM-DD).