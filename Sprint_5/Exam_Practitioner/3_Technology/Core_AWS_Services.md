

As principais categorias de serviços da AWS são: Computação, Armazenamento, Banco de Dados.

Saiba como classificar os serviços da AWS em categorias.

Saiba por que escolher serviços em categorias diferentes.
qual as vantagens de uma opção em relação a outra?

Quais subcategorias existem na categoria de serviços maiores?

---
## Core AWS Services

A Amazon Web Services (AWS) oferece uma ampla variedade de serviços em nuvem, e eles podem ser categorizados em três principais categorias: Computação, Armazenamento e Banco de Dados. Cada uma dessas categorias possui subcategorias e uma série de serviços individuais. Vamos explorar essas categorias, suas subcategorias e as vantagens de escolher serviços em categorias diferentes:

**1. Computação:**
   - **EC2 (Elastic Compute Cloud)**: É um serviço de computação em nuvem que permite criar e gerenciar instâncias virtuais.
   - **ECS (Elastic Container Service)**: Oferece uma plataforma para executar contêineres Docker na AWS.
   - **Lambda**: Um serviço de computação serverless que permite a execução de código em resposta a eventos sem a necessidade de provisionar servidores.
   - **Elastic Beanstalk**: Facilita a implantação e gerenciamento de aplicativos web.
   - **Batch**: Usado para executar cargas de trabalho de processamento em lote na nuvem.
   
**2. Armazenamento:**
   - **S3 (Simple Storage Service)**: Um serviço de armazenamento de objetos escalável e altamente disponível.
   - **EFS (Elastic File System)**: Fornece armazenamento de arquivos compartilhado entre instâncias EC2.
   - **Glacier**: Usado para armazenar dados de arquivamento de longo prazo.
   - **Storage Gateway**: Permite conectar a infraestrutura de TI local com o armazenamento em nuvem da AWS.
   
**3. Banco de Dados:**
   - **RDS (Relational Database Service)**: Oferece bancos de dados relacionais gerenciados, como MySQL, PostgreSQL, SQL Server, etc.
   - **DynamoDB**: Um banco de dados NoSQL totalmente gerenciado.
   - **Redshift**: Um serviço de data warehousing para análise de dados.
   - **Aurora**: Um banco de dados relacional compatível com MySQL e PostgreSQL, altamente disponível e escalável.
   
**Vantagens de escolher serviços em categorias diferentes:**
- **Flexibilidade**: Ao escolher serviços em categorias diferentes, você pode selecionar a combinação certa para atender às necessidades específicas de sua aplicação ou projeto.
- **Economia de custos**: Usar serviços especializados pode ser mais eficiente em termos de custos, pois você paga apenas pelo que usa.
- **Escalabilidade**: Diferentes categorias de serviços podem ser escaladas independentemente, permitindo que você dimensione recursos conforme necessário.
- **Alta Disponibilidade**: A diversificação entre categorias pode aumentar a disponibilidade geral do aplicativo, uma vez que falhas em uma categoria não afetarão necessariamente outras.

**Subcategorias em cada categoria maior:**
- **Computação**:
  - EC2 (máquinas virtuais)
  - Lambda (serverless)
  - ECS (contêineres)
  - Elastic Beanstalk (PaaS)
  - Batch (processamento em lote)

- **Armazenamento**:
  - S3 (armazenamento de objetos)
  - EFS (armazenamento de arquivos)
  - Glacier (armazenamento de arquivamento)
  - Storage Gateway (integração local-nuvem)

- **Banco de Dados**:
  - RDS (bancos de dados relacionais)
  - DynamoDB (NoSQL)
  - Redshift (data warehousing)
  - Aurora (bancos de dados de alto desempenho)

A escolha de serviços em categorias diferentes depende dos requisitos específicos do seu aplicativo, das considerações de custo e das necessidades de escalabilidade e disponibilidade. A AWS fornece flexibilidade para que você possa personalizar a infraestrutura de acordo com as demandas do seu projeto.

### Perguntas sobre Core AWS Services

Q - Qual é o serviço da AWS MAIS eficiente para importar exabytes de dados em um ambiente on-premises para a AWS Cloud?

OBS: Geralmente a melhor resposta é a solução mais direta a pergunta.

a - AWS Snowmobile🟢

b - AWS Storage Gateway

c - AWS Snowball

d - AWS Direct Connect

a melhor opção é a AWS Snowmobile, pois é um serviço de transferência de dados em massa que pode ser usado para importar ou exportar exabytes de dados para a AWS Cloud. Ele é especialmente projetado para esses casos.