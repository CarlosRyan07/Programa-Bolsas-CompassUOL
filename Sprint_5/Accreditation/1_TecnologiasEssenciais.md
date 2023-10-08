### Computação

EC2 são nossos blocos de criação de comoputador na aws.
Instancias de EC2 = Componentes basicos
São oferecidos em uma vasta variedade de recursos de hardware para atender á demandas de qualquer carga de trabalho.

Podemos aplicar Amazon Machine Images(AMIs) para personalizar a instalação do software quando iniciado. 

Podemos configurar o Auto Scaling e o balanceamento e carga, para que a nossa aplicação esteja sempre execultando a quantidade adequada de instâncias, de acordo com as necessidades do aplicativo em um determinado momento.
Seja em alta ou baixa demanda só estarei execultando e pagando somente o que é necessário.

Elastic Load Balance: Distribui trafégo de entrada.

Amazon Elastic Container Service: Executa aplicativos em cluster gerenciado.

Amazon Elastic Kubernet Service: Executa aplicativos kubernet na aws e no local.

AWS Lambda: Executa código em resposta á eventos.


### Armazenamento

Amazon Elastic Block Store(EBS): fornece disco para nossas instâncias, replicam cada volume de EBS após a criação. O armazenamento persiste a nivel de Bloco.

Amazon S3: é o Armazenamento de objetos duráveis e dimensionais, otimo para armazenamento em massa como: imagens, videos, códigos. Tem uma alta disponibilidade e velocidade de acesso.

Amazon Glacier: é focado no arquivamento e backup de dados, é uma alternativa econômica de backup a longo prazo.

AWS Storage Gateway: Integar armazenamento na nuvem com carga de trabalho local.

Amazon Elastic File System: Armazenamento de arquivos para instânciuas do Amazon EC2.

Amazon FSx: Armazenamento de arquivos para sistema de arquivos amplamente usados.


### Banco de Dados

Desenvolvido especialmente para casos de uso de aplicativos especificos, descarregar tarefas de gerenciamento demorados.

Amazon RDS: Capacidade econômica e redimensionavel.

Amazon DynamoDB: Desempenho rápido e previsível.

Amazon ElasticCache: Recuperação rápida e gerenciada de informações

### Redes

Primeira coisa que faremos aqui é a criação de uma VPC que é uma rede virtual na nuvem.
Atribuimos á um VPC um intervalo de endereços IP e configuro sub-redes públicas e privadas dentro da rede maior.

Utilizando ACls de redes podemos proteger as sub-redes, e assim criar outra camada de segurança no nível da instância usando grupos de segurança

### Segurança

Aqui segue o modelo de responsabilidade compartilhada da AWS. A AWS processa a parte da infraestrutura e seus serviços gerenciados, enquanto os clientes são responsáveis por proteger os dados e os recursos que eles criam na nuvem.

A AWS disponibiliza as ferramentas necessárias para essa finalidade, mas cabe aos clientes implementa-ás.

O AWS IAM ajudará a proteger seus serviços e recursos da AWS.

Se os Clientes tiverem dúvidas sobre a conformidade, a AWS fornecerá orientações sobre como eles podme resolvê-las.