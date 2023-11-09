
Aqui vão estar organizado os passo a passo que nos foi pedido no Lab Glue.

## Criando um Usuario IAM

<img src="https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_7/Lab_Glue/Evidencias/Criando_Usuario_IAM.png" width=600>


Atualizamos a função de serviço padrão do AWS Glue e a definimos como padrão:

<img src="https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_7/Lab_Glue/Evidencias/FuncaoCriada.png" width=600>


### Criando a IAM Role para os jobs do AWS Glue

<img src="https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_7/Lab_Glue/Evidencias/IAM_Role_Criado.png" width=600>


### Configurando as permissões no AWS Lake Formation


<img src="https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_7/Lab_Glue/Evidencias/DarPermissoesLAB4.png" width=600>


Criamos também um banco de Dados chamado glue-lab.

<img src="https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_7/Lab_Glue/Evidencias/GlueLab_Criado.png" width=600>

### Criando novo job no AWS Glue

<img src="https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_7/Lab_Glue/Evidencias/JobCriadoAtualizado.png" width=600>

### Sua vez!

Aqui com o Job criado vamos começar a rodar os scripts:

<img src="https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_7/Lab_Glue/Evidencias/JobRuns_Script.png" width=600>

Tivemos uma série de passos para criar um job Glue.
Esses foram os passos para nós desenvolvermos:

* Ler o arquivo nomes.csv no S3 (lembre-se de realizar upload do arquivo antes).
* Imprima o schema do dataframe gerado no passo anterior.
* Escrever o código necessário para alterar a caixa dos valores da coluna nome para MAIÚSCULO.
* Imprimir a contagem de linhas presentes no dataframe.
* Imprimir a contagem de nomes, agrupando os dados do dataframe pelas colunas ano e sexo.
* Ordene os dados de modo que o ano mais recente apareça como primeiro registro do dataframe.
* Apresentar qual foi o nome feminino com mais registros e em que ano ocorreu.
* Apresentar qual foi o nome masculino com mais registros e em que ano ocorreu.
* Apresentar o total de registros (masculinos e femininos) para cada ano presente no dataframe. Considere apenas as primeiras 10 linhas, ordenadas pelo ano, de forma crescente.
* Escrever o conteúdo do dataframe com os valores de nome em maiúsculo no S3. Atenção aos requisitos❗: A gravação deve ocorrer no subdiretório frequencia_registro_nomes_eua do path s3://<BUCKET>/lab-glue/, o formato deve ser JSON, o particionamento deverá ser realizado pelas colunas sexo e ano (nesta ordem)

Era para utilizar o script e rodar, mas por conta de alguns problemas acabei fazendo pelo notebook, o que acabou sendo mais pratico. 

Esse passo a passo você pode observar aqui: [Job Passo á Passo](https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_7/Lab_Glue/JobPassoAPasso.ipynb).

Aqui está gravação dos arquivos que deviam ocorrer no subdiretório frequencia_registro_nomes_eua do path s3:

<img src="https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_7/Lab_Glue/Evidencias/Arquivos_Gravados_Json.png" width=600>


### Crawler

Crawlers são mecanismos que podemos utilizar para monitorar nosso armazenamento de dados de modo a criar/atualizar metadados no catálogo do Glue de forma automática. Na sequência iremos desenvolver um crawler para automaticamente criar uma tabela chamada frequencia_registro_nomes_eua a partir dos dados escritos no S3.

<img src="https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_7/Lab_Glue/Evidencias/Crawler_Criado.png" width=600>

Crawler criado, agora vamos executá-lo. Na tela inicial selecionamos FrequenciaRegistroNomesCrawler e clicamos em Run:

<img src="https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_7/Lab_Glue/Evidencias/Crawler_Iniciado.png" width=600>

Se a execução for bem sucedida, nós esperamos que uma nova tabela, de nome frequencia_registro_nomes_eua tenha sido criada na base glue-lab. 

E aqui está:

<img src="https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_7/Lab_Glue/Evidencias/Crawler_TabelaCriada.png" width=600>

Depois de darmos as devidas Permissões necéssarias, agora consultamos os dados:

<img src="https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_7/Lab_Glue/Evidencias/Crawler_Consultado_Dados.png" width=600>
