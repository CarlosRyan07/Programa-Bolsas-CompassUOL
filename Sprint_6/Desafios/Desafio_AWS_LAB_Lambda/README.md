
Nesse Desafio usaremos AWS Lambda e criaremos função, camadas e pra mais detalhes segue abaixo.

### Etapa 1: Criar a função do Lambda


No console do AWS Lambda, selecione Criar uma função. Observação: o console só mostra esta página se não houver funções do Lambda criadas. Se já tiverem sido criadas funções, a opção será exibida a página Lambda > Funções.


<img src="https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_6/Desafios/DesafioAWS_LAB_Lambda/Evidencias/1_CriadaContagemLinhas.png" width="600">

### Etapa 2: Construir o código


A função será criada e você será redirecionado para o editor de funções do console. Por padrão, será criado o arquivo nomeado lambda_function.py com o código abaixo:



<img src="https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_6/Desafios/DesafioAWS_LAB_Lambda/Evidencias/2_CriadoTeste.png" width="600">

Substituimos por nosso nome do bucket e ficou assim:

```python
 
 
def lambda_handler(event, context):
    s3_client = boto3.client('s3')
 
    bucket_name = 'bucket-ryan-compass'
    s3_file_name = 'dados/nomes.csv'
    objeto = s3_client.get_object(Bucket=bucket_name, Key=s3_file_name)
    df=pandas.read_csv(objeto['Body'], sep=',')
    rows = len(df.axes[0])
 
    return {
        'statusCode': 200,
        'body': f"Este arquivo tem {rows} linhas"
    }

```

### Etapa3: Criar uma Layer


Afinal, o que são Layers (camadas)? De acordo com a documentação, as camadas do Lambda fornecem um modo conveniente de empacotar bibliotecas e outras dependências que você pode usar com suas funções Lambda. O uso de camadas reduz o tamanho dos arquivos de implantação carregados e acelera a implantação do código.

Uma camada  é um arquivo compactado (zip) que pode conter código ou dados adicionais. Uma camada pode conter bibliotecas, um tempo de execução personalizado, dados ou arquivos de configuração. As camadas promovem o compartilhamento de código e a separação de responsabilidades para que você possa ater-se à escrita da lógica de negócios.

É possível criar camadas usando o console da Lambda, a API do AWS Lambda, CloudFormation, ou AWS Serverless Application Model (AWS SAM). Aqui vamos usar o método do console da Lambda com comandos do prompt e arquivos no formato zip.

Usando esse método, estaremos instalando diretamente as bibliotecas python e suas dependências necessárias em pasta de um Conteiner Docker (sistema operacional Amazon Linux) e, em seguida, compactando-os para serem carregados na como camada à função Lambda.

Criamos uma pasta nova e nela um arquivo chamado Dockerfile. Vamos usar uma imagem de sistema operacional Linux específica da Amazon e instalar o python versão 3.7 e a ferramenta para fazer a compressão dos dados.

E Depois de uma serie de passos iremos ter uma pasta python, que deverá ter as bibliotecas instaladas, vamos compactar o diretório python.

Compactamos todos esses arquivos em um arquivo chamado minha-camada-pandas.zip e o adicionamos no nosso bucket do S3:

<img src="https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_6/Desafios/DesafioAWS_LAB_Lambda/Evidencias/3.0_AdicionandoZip.png" width="600">


Agora vamos criar a camada no Lambda, damos o nome de PandasLayer, escolhemos a opção Fazer upload de um arquivo do Amazon S3. Em outra aba retornamos ao S3, localizamos o arquivo minha-camada-pandas.zip que carregamos para o S3 anteriormente e copiamos a URL de objeto que está no S3. 
Retornando para a aba de criação da camada, colamos a URL em Link do URL do Amazon S3 e a criamos.


<img src="https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_6/Desafios/DesafioAWS_LAB_Lambda/Evidencias/3.1_CriadaCamada.png" width="600">



### Etapa 4: Utilizando a Layer

No menu, escolhemos Função e localizamos a função Lambda criada na Etapa 1
Localizamos o ícone Layers e nele: Clicamos em Adicionar uma camada, escolhemos Custom Layers (Camadas personalizadas), localizamos a camada e a versão criada na etapa anterior. Depois clicamos em Adicionar.

<img src="https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_6/Desafios/DesafioAWS_LAB_Lambda/Evidencias/4.0_AdicionandoCamada.png" width="600">



Na descrição do desafio tinha uma dica que era: Provavelmente será necessário aumentar o tempo limite e o tamanho da memória da Lambda.
e de fato foi necessario, aumentei o tempo limite e o tamanho da memoria para garantir que rodasse sem problemas.


E aqui esta o resultado final:

<img src="https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_6/Desafios/DesafioAWS_LAB_Lambda/Evidencias/4.1_TestandoCamada.png" width="600">

