## Exercicio 1 - TMDB 

Aqui nos Exercicios que tivemos o primerio que foi o seguinte:

## Etapa 1 -  Criando sua conta no TMDB

os passos para criar uma conta no TMDB são os seguintes:

- Acessar o portal pelo link https://www.themoviedb.org/

- Clique no botão Junte-se ao TMDB na barra de navegação no topo da página

- Preencha o formulário de inscrição com as informações solicitadas e clique em Registrar. Utilize seu e-mail pessoal neste passo.

-  Você irá receber um e-mail de confirmação. Siga o processo solicitado

- Faça login em sua nova conta no TMDB e vá para o seu perfil, clicando no ícone de usuário no canto superior direito da página

- Clique na guia  Visão geral, opção Editar Perfil

- Clique no menu API, à esquerda. A seguir, na opção Criar, escolhendo o tipo Developer

- Aceite os termos e preencha o formulário com as informações solicitadas sobre a aplicação.

----- Em Tipo de Uso, informe Pessoal

----- Em URL, você pode informar um endereço fictício.

----- No Resumo, informe que o objetivo é para estudos

E aqui esta a conta Criada:

<img src="https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_8/Exercicios/Evidencias/Conta_Criada_TMDB.png" width=600>

.
## Etapa 2 - Testando rapidamente as credenciais e a biblioteca


Uma vez que você tenha sua chave de API, você pode fazer solicitações à API usando a seguinte estrutura de URL:

https://api.themoviedb.org/3/{endpoint}?api_key={sua_chave_de_api}&{parâmetros_opcionais}



Onde {endpoint} é o recurso que você deseja acessar (por exemplo, movie/{movie_id} para obter detalhes de um filme específico) e {parâmetros_opcionais} são quaisquer parâmetros adicionais que você deseje incluir na solicitação (por exemplo, language=pt-BR para obter informações em português).





Aqui está o codigo python que utilizei: [código Python](https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_8/Exercicios/exer1.py)


E aqui o resultado obtido ao rodar o codigo:
<img src="https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_8/Exercicios/Evidencias/Resultado_Codigo.png" width=600>


Após isso fomos para o [Desafio Parte 2](https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_8/DesafioPart2-Ingestao_de_dados_TMDB)
Porém ainda não acabou os exercicios por aqui, logo após o desafio seguimos abaixo.

## Exercicio 2 - Gerar Massa de Dados

Aqui não tem muito segredo fizemos as tarefas que são pré-requisitos para a execução do laboratório de Apache Spark na sequência.

Tarefas essa que você pode acompanhar aqui: [Exercicios](https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_8/Exercicios/Gerar_Massa_de_Dados/exercicios.ipynb)


## Exercicio 3 - Apache Spark

Neste laboratório usaremos um arquivo CSV o da ultima questão do exercicios anterior 'nomes_aleatorios.txt para criar um Dataframe e testar comandos SQL(como o arquivo era muito grande não consegui coloca-lo no github, porém se for no exercicio anterior e roda-lo, você o criará). Iremos utilizar o arquivo nomes_aleatorios.txt gerado na tarefa anterior. Esse arquivo tem aproximadamente 10 milhões de nomes distintos e apresenta os nomes mais populares registrados em cada ano.

Teve um total de 10 questões nessa parte, que você pode acompanhar aqui: [sparkSession](https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_8/Exercicios/Apache_Spark/sparkSession.ipynb)