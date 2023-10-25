## Análise de dados e Soluções de Avaliação de dados

Avaliação é um exame detalhado de algo para entender sua natureza ou determinar suas características essenciais. Avaliação de dados é o processo de compilar, processar e analisar dados para que você possa usá-los para tomar decisões.

Análise é a avaliação sistemática de dados. Análise de dados é o processo analítico específico sendo aplicado.

Sem os dados fornecidos por análise de dados, muitos responsáveis por tomar decisões se baseariam em intuição e pura sorte. 

À medida que as empresas começam a implementar soluções de avaliação de dados, surgem desafios. Esses desafios são baseados nas características dos dados e das análises necessárias para o caso de uso dessas empresas. No passado, esses desafios foram definidos como desafios de “big data”. Entretanto, no ambiente atual baseado na nuvem, esses desafios podem se aplicar a conjuntos de dados pequenos ou lentos quase tão frequentemente quanto a conjuntos de dados muito grandes e rápidos.

Este curso visá nos mostrar como identificar a solução de avaliação de dados que melhor atenda aos seus requisitos e como planejar e executar uma estratégia para implementá-la.

Big data é um termo do setor que mudou nos últimos anos. Muitas vezes, as soluções de big data fazem parte de soluções de avaliação de dados. 

---
                As organizações gastam milhões de dólares em armazenamento de dados.
                O problema não é encontrar os dados, mas deixar de fazer algo com eles. 

---

Benefícios de análise de dados em grande escala:

- **Personalização do cliente** -  Quais produtos devem ser mostrados ao cliente com base em seus hábitos de comprar?

- **Detecção de fraude** -  Quais transações são fraudulentas?

- **Modelagens e previsões financeiras** -  Quais tendências podem ser detectadas nesses terabytes de dados financeiros? Como isso pode ser usado para prever futuras mudanças de mercado?

- **Alerta em tempo real** -  Qual é o problema e quem precisa ser notificado?

- **Comportamento do usuário** -  Com base em feeds de redes sociais, qual o nível de influência que essa pessoa tem? Que tipos de produtos ou serviços essas pessoas teriam interesse em promover?

- **Detecção de Ameaças á segurança** - Quais padrões de uso indicam possíveis riscos de segurança de agentes mal‑intencionados?
---

### Componentes de uma solução de avaliação de dados

Uma solução de avaliação de dados tem os seguintes componentes.

1. **Dados brutos:** São os dados iniciais e não processados coletados de várias fontes. Esses dados podem ser estruturados ou não estruturados.

2. **Ingerir e coletar:** Refere-se à coleta e ingestão dos dados brutos. Isso envolve a captura dos dados de fontes diversas e sua transferência para um ambiente de armazenamento.

3. **Armazenar:** Os dados são armazenados em um sistema de gerenciamento de banco de dados ou em um armazenamento distribuído para acesso posterior. A escolha do local de armazenamento depende das necessidades do projeto.

4. **Processar e analisar:** Nesta etapa, os dados são processados e analisados para identificar tendências, padrões, anomalias e obter informações úteis. Isso pode envolver limpeza, transformação e análise estatística dos dados.

5. **Consumir e visualizar:** Os resultados da análise são disponibilizados para os usuários por meio de painéis, relatórios ou aplicativos. Isso permite que as informações sejam acessadas e interpretadas de maneira mais fácil.

6. **Resposta:** Com base nas informações obtidas, a solução pode acionar ações automáticas ou sugerir ações a serem tomadas pelos tomadores de decisão.

7. **Informações:** As informações obtidas a partir dos dados processados e analisados são a saída final da solução, fornecendo insights e orientando as decisões organizacionais.

Esses componentes são essenciais para criar uma solução de avaliação de dados eficaz, que pode ser usada em uma variedade de contextos, como análise de negócios, tomada de decisões estratégicas e monitoramento de sistemas.


                O componente de coleta é onde os serviços montam dados de várias fontes.

                O componente de armazenamento armazena dados em repositórios.

                O componente de processamento é onde os serviços manipulam dados nas formas necessárias.

                O componente de consumo é onde os dados são apresentados nos formatos necessários.


## Sobre o V de Volume

        Quando as empresas têm mais dados do que conseguem processar e analisar, elas têm um problema de volume.

## Amazon S3

O Amazon S3 é o armazenamento para a internet. Esse serviço foi projetado para facilitar a computação em escala web para os desenvolvedores. O Amazon S3 fornece uma interface simples de serviços da web que pode ser usada para armazenar e recuperar qualquer quantidade de dados, a qualquer momento e a partir de qualquer lugar. O serviço concede acesso a todos os desenvolvedores à mesma infraestrutura altamente escalável, confiável, segura, rápida e econômica que a Amazon utiliza para executar sua própria rede global de sites. O serviço tem como objetivo maximizar os benefícios de escala e repassar esses benefícios para os desenvolvedores.


Os benefícios do Amazon S3 são:


    - Armazenamento de qualquer coisa;
    - Armazenamento seguro de objetos;
    - Acesso HTTP nativamente on-line;
    - Escalabilidade ilimitada; 
    - Durabilidade de 99,999999999%.

Amazon S3 armazena dados como objetos em buckets.

Um objeto é composto por um arquivo e quaisquer metadados que descrevam esse arquivo. Para armazenar um objeto no Amazon S3, você faz o upload do arquivo que deseja armazenar no bucket. Ao fazer o upload de um arquivo, você pode definir permissões no objeto e adicionar metadados.

Buckets são contêineres lógicos para objetos. Você pode ter um ou mais buckets em sua conta e controlar o acesso a cada um individualmente. Você controla quem pode criar, excluir e listar objetos no bucket. Você também pode visualizar logs de acesso do bucket e seus objetos e escolher a região geográfica onde o Amazon S3 armazenará o bucket e o respectivo conteúdo.

Depois que os objetos foram armazenados em um bucket do Amazon S3, eles recebem uma chave de objeto. Use isso, juntamente com o nome do bucket, para acessar o objeto.

Veja abaixo um exemplo de URL para um único objeto em um bucket chamado doc, com uma chave de objeto composta pelo prefixo 2006-03-01 e o arquivo nomeado AmazonS3.html.

https://**doc**.s3.amazonaws.com/**2006-03-01/AmazonS3**.html

        Bucket: doc, Key: 2006-03-01/AmazonS3.html, Prefixo: 2006-03-01/ 

---

### Data Lake
Um data lake é um repositório centralizado que permite armazenar dados estruturados, semiestruturados e não estruturados em qualquer escala. Você pode armazenar seus dados como estão, sem ter que estruturá-los, e executar diferentes tipos de análise, desde painéis e visualizações até big data e aprendizado de máquina, para orientar melhores decisões.

### Benefícios de um data lake na AWS

* São uma solução de armazenamento de dados econômica. Você pode armazenar de forma durável uma quantidade quase ilimitada de dados usando o Amazon S3.
* Implemente a segurança e a conformidade líderes do setor. A AWS usa rigorosos mecanismos de segurança, conformidade, privacidade e proteção de dados.
* Permite que você aproveite muitas ferramentas diferentes de coleta e ingestão de dados para ingerir dados em seu data lake. Esses serviços incluem o Amazon Kinesis para dados de streaming e dispositivos AWS Snowball para grandes volumes de dados locais.
* Ajudam você a categorizar e gerenciar seus dados de forma simples e eficiente. Use o AWS Glue para entender os dados dentro do seu data lake, prepará-los e carregá-los de forma confiável em datastores. Depois que o AWS Glue cataloga seus dados, eles são imediatamente pesquisáveis, podem ser consultados e estão disponíveis para processamento de ETL.
* Ajuda você a transformar dados em informações significativas. Utilize o poder dos serviços analíticos criados para finalidades específicas em vários casos de uso, como avaliação interativa, processamento de dados usando o Apache Spark e o Apache Hadoop, data warehousing, análise em tempo real, análise operacional, painéis e visualizações.

Ou seja, um data lake na AWS pode ajudar a:

- Coletar e armazenar qualquer tipo de dados, em qualquer escala e com baixo custo;
- Proteger os dados e evitar acesso não autorizado;
- Catalogar, pesquisar e encontrar os dados relevantes em um repositório central;
- Executar novos tipos de avaliação de dados com rapidez e facilidade;
- Usar um amplo conjunto de mecanismos analíticos para análise única, streaming em tempo real, análise preditiva, IA e machine learning.

## Data Warehouse   

Um data warehouse é um repositório central de dados estruturados de muitas origens de dados. Esses dados são transformados, agregados e preparados para relatórios e avaliaçãos de negócios.

Para armazenar grandes volumes de dados, tanto os estruturados quanto não estruturados recomendamos a criação de um data lake na AWS.

Quando se trata de armazenar uma quantidade massiva de dados, pra efetuar análises complexas, recomendamos a utilização de um Data Warehouse no Amazon Redshift. E temos mais uma recomendação.

As empresas se perguntam: por quê? Por que devemos gastar muito tempo e dinheiro implementando um data lake quando já investimos tanto em um data warehouse? É importante lembrar que um data lake aumenta um data warehouse, mas não o substitui.

Data lakes são a extensão dos data warehouses

Os data lakes fornecem aos clientes um meio de incluir dados não estruturados e semiestruturados em sua análise. As consultas analíticas podem ser executadas em dados catalogados em um data lake. Isso amplia o alcance da análise para além dos limites de um único data warehouse.


## Amazon Redshift

O Amazon Redshift é uma solução de data warehousing especialmente projetada para cargas de trabalho de todos os tamanhos. O Amazon Redshift Spectrum ainda oferece a capacidade de consultar dados hospedados em um data lake do Amazon S3.

O Amazon Redshift é um data warehouse rápido e dimensionável que permite analisar todos os dados de data warehouses e data lakes de forma simples e econômica. O Amazon Redshift oferece desempenho 10 vezes mais rápido que qualquer outro data warehouse por meio de machine learning, além da execução paralela de consultas em massa e armazenamento colunar em discos de alto desempenho. Você pode configurar e implantar um novo data warehouse em minutos e executar consultas em petabytes de dados no data warehouse do Amazon Redshift e exabytes de dados no data lake criado no Amazon S3.

## Apache Hadoop

O Hadoop usa uma arquitetura de processamento distribuído, no qual uma tarefa é mapeada para um cluster de servidores convencionais para processamento. Cada bloco de trabalho distribuído aos servidores do cluster pode ser executado ou re-executado em qualquer um dos servidores. Os servidores do cluster usam frequentemente o Hadoop Distributed File System (HDFS) para armazenar dados localmente para processamento. Os resultados da computação realizada pelos servidores são reduzidos a um único conjunto de saída. Um nó, designado como nó principal, controla a distribuição de tarefas e pode lidar automaticamente com falhas dos servidores.

Benefícios do uso do Apache Hadoop

* LIDA MELHOR COM A INCERTEZA

* GERENCIA VARIEDADE DE DADOS

* TEM AMPLA SELEÇÃO DE SOLUÇÕES

* VISA AO VOLUME E À VELOCIDADE

## sobre o V de Velocidade

        Quando sua empresa não consegue processar dados com rapidez suficiente para atender às necessidades de negócios, você sabe que tem um problema de velocidade.

A pressão nos sistemas de processamento varia de acordo com os requisitos de velocidade.

Processamento em batch: processa grandes quantidades de dados de uma só vez. Isso requer um sistema que possa coletar e armazenar esses dados até que o sistema de processamento possa lidar com tudo isso.

Processamento periódico: processa cargas de trabalho irregulares imprevisíveis. A impossibilidade de prever essas cargas de trabalho sobrecarrega os sistemas de big data.

Processamento quase em tempo real: processa pequenos picos de dados que devem ser coletados e processados em minutos após a coleta.

Processamento em tempo real: processa pequenos picos de dados continuamente. Esses dados devem ser apresentados à fase de análise em instantes após a coleta.

### Serviços

O AWS Lambda é um serviço computacional sem servidor que pode ser usado para acionar operações de processamento em um sistema de processamento em batch.

O Amazon EMR é um serviço gerenciado para executar cargas de trabalho em batches altamente complexas e massivas. Esse serviço também permite operações analíticas altamente complexas.

O Amazon Redshift é um serviço de data warehouse gerenciado que armazena grandes quantidades de dados de transações para fins de análise.


## O Amazon Kinesis

O Amazon Kinesis Data Firehose é a maneira mais fácil de capturar, transformar e carregar streams de dados em datastores da AWS para análises quase em tempo real usando ferramentas existentes de business intelligence.

O Amazon Kinesis Data Streams permite criar aplicativos personalizados e em tempo real para processar streams de dados usando frameworks comuns de processamento de streams.

O Amazon Kinesis Video Streams facilita o streaming seguro de vídeos a partir de dispositivos conectados à AWS, onde podem ser usados para análise, machine learning (ML) e outros processamentos.

O Amazon Kinesis Data Analytics é a maneira mais fácil de processar streams de dados em tempo real com SQL ou Java sem precisar aprender novas linguagens de programação ou frameworks de processamento.

## Casos de uso de processamento em stream

Construir aplicativos de análise de vídeo

Evoluir do processamento em batch para a análise em tempo real

Analisar dados de dispositivos IoT

---
## Sobre o V de Variedade

        Quando sua empresa fica sobrecarregada pelo grande número de origens dos dados para analisar e você não consegue encontrar sistemas para fazer a análise, sabe que tem um problema de variedade.

### Tipos de origem de dados

* **Dados estruturados:** são armazenados em um formato tabular, muitas vezes em um sistema de gerenciamento de banco de dados (DBMS). Esses dados são organizados com base em um modelo de dados relacional que define e padroniza elementos de dados e a relação deles entre si. Os dados são armazenados em linhas, com cada linha representando uma única instância de algo (por exemplo, um cliente). Essas linhas são bem compreendidas devido ao esquema da tabela, que explica o que cada campo na tabela representa. Isso facilita a consulta de dados estruturados.

A desvantagem dos dados estruturados é a falta de flexibilidade. Digamos que você decidiu que deseja acompanhar a idade dos seus clientes. Você deve reconfigurar o esquema para permitir esse novo dado e considerar todos os registros que não têm um valor para esse novo campo. Não é impossível, mas pode ser um processo muito demorado.

Exemplos de aplicativos de dados estruturados incluem Amazon RDS, Amazon Aurora, MySQL, MariaDB, PostgreSQL, Microsoft SQL Server e Oracle.

* **Dados semiestruturados:** são armazenados na forma de elementos em um arquivo. Esses dados são organizados com base nos elementos e atributos que os definem. Eles não estão em conformidade com modelos ou esquemas de dados. Os dados semiestruturados são considerados como tendo uma estrutura autodescritiva. Cada elemento é uma única instância de alguma coisa, como uma conversa. Os atributos dentro de um elemento definem as características dessa conversa. Cada elemento de conversa pode monitorar atributos diferentes. Isso torna os dados semiestruturados bastante flexíveis e capazes de escalar para atender às demandas dinâmicas de uma empresa com mais rapidez do que os dados estruturados.

A diferença é a análise. Pode ser mais difícil analisar dados semiestruturados quando os analistas não conseguem prever quais atributos estarão presentes em um determinado conjunto de dados.

Exemplos de datastores semiestruturados são CSV, XML, JSON, Amazon DynamoDB, Amazon Neptune e Amazon ElastiCache.

* **Dados não estruturados:** são armazenados na forma de arquivos. Esses dados não estão em conformidade com um modelo de dados predefinido nem organizados de maneira predefinida. Dados não estruturados podem ser arquivos de texto, fotografias, gravações de áudio ou até mesmo vídeos. Dados não estruturados estão cheios de informações irrelevantes, o que significa que os arquivos precisam ser pré-processados para fazer avaliaçãos significativas. Isso pode ser feito de várias maneiras. Por exemplo, os serviços podem adicionar tags aos dados com base em regras definidas para os tipos de arquivos. Os dados também podem ser catalogados para deixá-los disponíveis a serviços de consulta.

Exemplos de dados não estruturados incluem e-mails, fotos, vídeos, dados de clickstream, Amazon S3 e Amazon Redshift Spectrum.

        Dados estruturados são quentes, imediatamente prontos para serem analisados. 
        Dados semiestruturados são mornos. Alguns estarão prontos para uso e outros podem precisar de limpeza ou pré-processamento. 
        Dados não estruturados são um oceano congelado, repleto de tudo o que você precisa, mas separado por todo tipo de coisa de que você não precisa.

### Sistema OLTP(Online Transaction Processing) e Sistema OLAP(Online Analytical Processing)

Em um sistema OLTP, as consultas mais comuns são chamadas de consultas de pesquisa. Essas consultas precisam retornar várias colunas de dados para cada registro correspondente. Os filtros nesses dados geralmente são baseados nas colunas de chave dessa tabela. Nesse tipo de sistema, você pode consultar para obter detalhes de uma ordem específica.

Em um sistema OLAP, as consultas mais comuns são consultas agregadas. Essas consultas utilizam um grande número de linhas e as reduzem a uma única linha agregando os valores em uma ou mais colunas. Nesse tipo de sistema, você pode consultar para descobrir o número total de itens vendidos em uma data específica.
Os bancos de dados OLAP são gerados a partir de dados em outros bancos de dados e geralmente são chamados de data warehouses.

Os sistemas OLTP e OLAP podem usar qualquer um dos métodos de indexação. No entanto, há vantagens em escolher o método mais adequado para os tipos de consultas que serão executadas na maior parte do tempo.

### Amazon RDS

O Amazon Relational Database Service (Amazon RDS) atende as necessidades de muitos sistemas de gerenciamento de banco de dados relacional diferentes. Ele é compatível com a maioria dos mecanismos de banco de dados mais conhecidos, incluindo Amazon Aurora, MySQL, PostgreSQL, MariaDB, Oracle e SQL Server.

O Amazon RDS facilita a configuração, operaração e scaling de um banco de dados relacional na nuvem. O serviço fornece capacidade econômica e redimensionável enquanto automatiza tarefas administrativas demoradas, como provisionamento de hardware, configuração de banco de dados, aplicação de patches e backups.

O Amazon RDS tem tudo o que você pode precisar para um banco de dados OLTP altamente eficiente. O serviço implementa a indexação baseada em linhas para alcançar o desempenho certo para cargas de trabalho transacionais.

### Vantagens e desvantagens do banco de dados relacional

O principal benefício de um banco de dados relacional usando SQL é ser uma tecnologia comprovada amplamente adotada e compreendida. Há menos risco envolvido com um banco de dados relacional, especialmente devido à conformidade com ACID e a uma grande comunidade de especialistas na área. Há uma expectativa de latência transacional muito boa, especialmente em hardware adequadamente dimensionado, e bancos de dados relacionais são considerados perfeitos para o OLTP para conjuntos de dados relativamente pequenos.

Existem preocupações de escalabilidade com um banco de dados relacional. À medida que os conjuntos de dados crescem, a única maneira de manter o desempenho é aumentar as capacidades de hardware dos servidores que executam o aplicativo. Outro problema importante é o esquema fixo de bancos de dados relacionais. É difícil fazer alterações sem interrupções nas arquiteturas básicas de banco de dados, o que pode afetar os tempos de desenvolvimento de novas funcionalidades.

        Os dados de arquivos de texto puro são armazenados sem estrutura rígida.
        Os dados OLTP são estruturados para fins de entrada de dados.
        Os dados OLAP são estruturados para fins de recuperação de dado

### Amazon DynamoDB e Amazon Neptune

O Amazon DynamoDB é para bancos de dados não relacionais ,de documentos e chave-valor que fornece desempenho inferior a 10 milissegundos em qualquer escala. O serviço é um banco de dados totalmente gerenciado que opera em várias regiões e com vários mestres e conta com recursos integrados de segurança, backup e restauração, bem como armazenamento em cache na memória para aplicativos na escala da internet. O DynamoDB pode processar mais de 10 trilhões de solicitações por dia e oferecer suporte a picos de mais de 20 milhões de solicitações por segundo.

### Vantagens e desvantagens do banco de dados não relacional

Os bancos de dados não relacionais têm o principal benefício de ir além das limitações dos bancos de dados relacionais, especialmente por meio de esquemas dinâmicos, que oferecem aos DBAs a capacidade de atualizar esquemas em tempo real. Isso leva a ciclos de desenvolvimento mais rápidos e menos tempo de inatividade. Além disso, como os bancos de dados não relacionais podem ser implantados em servidores de commodities distribuídos em massa, esses bancos de dados têm uma vantagem em scaling e podem lidar com conjuntos de dados muito maiores.

A distribuição massiva tem uma desvantagem, na forma de “consistência eventual”, o que significa que os dados não são atualizados instantaneamente a cada alteração e, em vez disso, alcançam a atualização como uma tarefa em segundo plano. Embora seja aceitável em muitas circunstâncias, isso dificulta atingir a conformidade com ACID. Observe que o DynamoDB oferece suporte à conformidade com ACID.

Outra desvantagem é que os bancos de dados não relacionais não têm desempenho tão bom quanto os bancos de dados relacionais em aplicativos que exigem latência transacional extremamente baixa. Por fim, embora as plataformas não relacionais estejam evoluindo e crescendo constantemente, praticamente não há a mesma maturidade que as tecnologias relacionais ou o mesmo nível de especialização em campo.

O Amazon Neptune é um serviço de banco de dados de grafo rápido, confiável e totalmente gerenciado que facilita a criação e a execução de aplicativos que funcionam com conjuntos de dados altamente conectados. Ele é um mecanismo de banco de dados de grafo de alto desempenho e criado especificamente para armazenar bilhões de relações e consultar os grafos com latência de milissegundos.

        Um data warehouse multidimensional é mais adequado para um banco de dados relacional.

        Os arquivos de log são geralmente produzidos na forma de arquivos XML ou JSON, que são muito adequados para armazenamento em um banco de dados de documentos.

        Os dados coletados de sites de jogos on-line geralmente são muito rápidos em geração e temporários por natureza. Esses dados são adequados para um banco de dados de chave-valor.

        Os dados transacionais de um serviço de assinatura social podem ser armazenados em um banco de dados relacional, mas devido ao componente social, seriam mais adequados às vantagens obtidas usando um banco de dados de grafo.

Os bancos de dados não relacionais são otimizados para computação e são bons em scaling horizontal. O design de dados para bancos de dados não relacionais é um documento desnormalizado, uma coluna ampla ou com base em chave-valor. Por fim, bancos de dados não relacionais são comumente usados para aplicativos móveis e web OLTP, mas não para sistemas de negócios OLTP.

## Sobre o V de Veracidade

        Quando se tem dados que não são controlados, provenientes de vários sistemas diferentes e não consegue fazer curadoria dos dados de maneiras significativas, você sabe que tem um problema de veracidade.


**O problema da veracidade**

Os dados sofrem alterações ao longo do tempo. À medida que são transferidos de um processo para outro, e por um sistema e outro, há oportunidades para que a integridade dos dados seja afetada negativamente. Você deve garantir a manutenção de um alto nível de certeza de que os dados que está analisando são confiáveis.

### Definições

Limpeza de dados é o processo de detecção e correção de corrupções nos dados.
Integridade referencial é o processo para garantir que as restrições das relações da tabela sejam impostas.
Integridade do domínio é o processo para garantir que os dados inseridos em um campo correspondam ao tipo de dados definido para esse campo.
Integridade da entidade é o processo para garantir que os valores armazenados em um campo correspondam às restrições definidas para esse campo.

Aqui algumas das práticas recomendadas para ajudar a identificar problemas de integridade dos dados.

* Saiba qual deve ser a limpeza

* Saiba de onde os erros vêm

* Saiba quais são as alterações aceitáveis

* Saiba se os dados originais têm valor

### Esquemas de banco de dados

**Um esquema de dados** é o conjunto de metadados usado pelo banco de dados para organizar objetos de dados e impor restrições de integridade. O esquema define os atributos do banco de dados, fornecendo as descrições de cada objeto e como ele interage com outros objetos no banco de dados. Um ou mais esquemas podem residir no mesmo banco de dados.

Há dois tipos de esquemas: lógico e físico.

**Os esquemas lógicos** se concentram nas restrições a serem aplicadas aos dados no banco de dados. Isso inclui a organização de tabelas, visualizações e verificações de integridade.

Tabelas e exibições podem ser relacionadas entre si. O esquema define as informações de cada relação e como ela deve ser imposta. O esquema também pode fornecer integridade de domínio definindo restrições sobre os valores permitidos em campos específicos dentro da tabela que fornece integridade de domínio.

As verificações de integridade vêm em diferentes formas, mas o objetivo é garantir que quaisquer alterações feitas no banco de dados não resultem em perda de consistência de dados.

**Os esquemas físicos** se concentram no armazenamento real de dados em disco ou em um repositório de nuvem. Esses esquemas têm detalhes sobre os arquivos, índices, tabelas particionadas, clusters e muito mais.

Em geral, os analistas podem usar esquemas físicos para calcular estimativas sobre o espaço de armazenamento necessário e o crescimento potencial do sistema. Esses esquemas também são importantes para a recuperação de desastres e o planejamento da infraestrutura.

**Um esquema de informações** é um banco de dados de metadados que armazena informações sobre os objetos de dados em um banco de dados.

O Microsoft SQL Server chama seu esquema de informações de banco de dados mestre. A Oracle usa tabelas de dicionário de dados e um registro de metadados. O Apache Hadoop usa um metastore. Cada DBMS pode ter nomes diferentes para a estrutura de dados que armazena os metadados, mas a finalidade é a mesma: definir quais são todos os objetos no banco de dados e registrar informações vitais sobre eles. Esses bancos de dados armazenam informações como o nome e o tamanho de uma tabela, os índices na tabela e as restrições de dados na tabela. As configurações de segurança para usuários, ativos de dados externos e configurações de gerenciamento também podem ser incluídas.


No ciclo de vida de um dado o estágio de compartilhamento é aquele em que os consumidores obtêm acesso aos dados na forma de relatórios. A maioria dos consumidores terá uma boa ideia de quais números devem ser. Se os consumidores não encontrarem o que esperam, questionarão a validade dos dados.

A integridade relacional garante que ambos os membros de uma relação permaneçam consistentes.
A integridade da entidade garante que os valores em um campo permaneçam consistentes.

Um esquema de informações é um banco de dados de metadados que contém informações sobre todos os objetos do banco de dados.

Um esquema lógico lista as restrições, relações e propriedades de tabelas e exibições em um banco de dados.

## ACID

ACID é um acrônimo para Atomicidade, Consistência, Isolamento e Durabilidade. É um método para manter a consistência e a integridade em um banco de dados estruturado.

ACID é o bastião de longa duração da integridade dos dados relacionais. Em um banco de dados como o Amazon RDS, uma sequência de instruções executadas em conjunto é chamada de transação. Milhões de transações podem ser executadas consecutivamente. Os dados e as restrições nesses dados são muito ativos em bancos de dados relacionais.

O objetivo de um banco de dados compatível com ACID é retornar a versão mais recente de todos os dados e garantir que os dados inseridos no sistema atendam a todas as regras e restrições atribuídas em todos os momentos.

## BASE

BASE é um acrônimo para BAsicamente disponível, eStado flexível, Eventualmente consistente. É um método para manter a consistência e a integridade em um banco de dados estruturado ou semiestruturado.

O BASE promove a integridade de dados em bancos de dados não relacionais, às vezes são chamados de bancos de dados NoSQL. Bancos de dados não relacionais, como o Amazon DynamoDB, ainda usam transações para processar solicitações. Esses bancos de dados são hiperativos e a principal preocupação é a disponibilidade dos dados em relação à consistência dos dados. Para garantir que os dados estejam altamente disponíveis, as alterações nos dados são disponibilizadas imediatamente na instância em que a alteração foi feita. No entanto, pode levar algum tempo para que essa alteração seja replicada em toda a frota de instâncias. O objetivo é que a alteração acabe sendo totalmente consistente em toda a frota. 

        Conformidade com ACID                           Conformidade BASE

        Consistência forte                              Consistência fraca - dados obsoletos são considerados OK

        O isolamento é essencial                        A disponibilidade é essencial

        Foco nos resultados confirmados                 Resultados do melhor esforço

        Disponibilidade conservadora (pessimista)       Disponibilidade agressiva (otimista)


### Amazon EMR e AWS Glue

Quando se trata de executar o componente de transformação de dados do ETL, há duas opções na AWS: o Amazon EMR e o AWS Glue. Esses dois serviços fornecem resultados semelhantes, mas exigem diferentes quantidades de conhecimento e investimento de tempo.

O Amazon EMR é uma abordagem mais prática para criar seu pipeline de dados. Esse serviço fornece uma plataforma robusta de coleta e processamento de dados. Para usar esse serviço, sua equipe deve ter sólido conhecimento técnico e know‑how. A vantagem dele é que você pode criar um pipeline personalizado para atender às suas necessidades de negócios. Além disso, os custos de infraestrutura podem ser menores do que executar a mesma carga de trabalho no AWS Glue.

O AWS Glue é uma ferramenta de ETL gerenciada sem servidor que oferece uma experiência muito mais simplificada do que o Amazon EMR. Isso torna o serviço ideal para tarefas simples de ETL, mas você não terá tanta flexibilidade quanto teria com o Amazon EMR. Você também pode usar o AWS Glue como um metastore para seus dados transformados finais usando o AWS Glue Data Catalog. Esse catálogo é uma substituição de uma metastore do Hive.

## Sobre o V de Valor

        Quando há grandes volumes de dados usados para corroborar algumas informações valiosas, você pode estar perdendo o valor dos seus dados.

        “Acreditamos que os dados são o nosso petróleo, o nosso ouro. Mas ter centenas de milhões de terabytes de dados que não são acionáveis não significa nada para mim.”
        - Rob Roy, diretor executivo digital da Sprint


### Análise de informações

Análise de informações é o processo de análise de informações para encontrar o valor contido nelas. Esse termo geralmente é sinônimo de análise de dados.

        “É um erro grave teorizar antes de ter dados. 
        Insensivelmente, começa-se a distorcer os fatos para se adequar às teorias, 
        em vez de moldar as teorias aos fatos”. – Sherlock Holmes

Tipos de Análises:

1. **Análises Descritivas**:
   - Descrevem e resumem dados passados, revelando informações sobre o que aconteceu. Exemplos incluem médias, gráficos de barras e estatísticas resumidas.

2. **Análises de Diagnóstico**:
   - Identificam a causa de eventos passados, ajudando a entender por que algo aconteceu. Isso envolve a investigação de relações entre variáveis.

3. **Análises Preditivas**:
   - Usam dados históricos para fazer previsões sobre eventos futuros. Modelos estatísticos e de machine learning são usados para prever tendências ou resultados.

4. **Análises Prescritivas**:
   - Oferecem recomendações e orientações sobre ações futuras com base em análises preditivas. Ajudam na tomada de decisões, indicando o que deve ser feito para alcançar resultados desejados.

5. **Análises Cognitivas**:
   - Envolvem a simulação de processos de pensamento humanos. Isso pode incluir análises de linguagem natural e reconhecimento de padrões para entender e imitar a cognição humana.

6. **Inteligência Artificial (IA)**:
   - Envolve sistemas que podem aprender e realizar tarefas de forma autônoma, sem programação explícita. A IA abrange uma ampla gama de tecnologias, incluindo aprendizado de máquina, redes neurais, visão computacional e processamento de linguagem natural.

Esses tipos de análises são frequentemente usados em conjunto para obter insights e tomar decisões informadas com base em dados, dependendo das necessidades específicas de uma situação ou problema.


* Quais foram as vendas totais em abril?
As perguntas relacionadas a eventos anteriores são respondidas usando avaliação descritiva.

* Quais são as vendas totais do ano a ano para a região Ásia-Pacífico?
As perguntas que comparam conjuntos de dados atuais com conjuntos de dados anteriores são respondidas usando avaliação diagnóstica.

* Qual é o crescimento projetado para internações relacionadas a tabagismo no próximo ano?
As perguntas que procuram previsões de eventos futuros são respondidas usando avaliação preditiva.

* Quais produtos devo comprar se gosto do time Seattle Seahawks?
Perguntas que buscam recomendações com base em preferências ou histórico de compras anteriores são respondidas usando avaliação prescritiva.

* Qual é o número médio de veículos detectados pela minha campainha de vídeo?
Perguntas que exigem avaliação de vídeo, imagens e voz são respondidas usando avaliação cognitiva.
---

## Certificado de conclusão🥇:

<img src="https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_6/Data_Analytics_Fundamentals/Certificado/Certificado_Data_Analytics_Fundamentals.png" width="600"> 

