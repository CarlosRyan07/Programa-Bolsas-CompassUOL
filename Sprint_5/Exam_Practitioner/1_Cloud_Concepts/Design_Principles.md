Principios de projeto da Arquitetura:

Desing á prova de falhas: Enteda como e quais componentes falham e como arquitetar falhas para adicionar resistência.

ex: um exemplo simples seria algo como construir um aplicativo que poderia ser executado em um único servidor, mas usando pelo menos dois servidores.
Nesse cenario estariamos projetando sua arquitetura com a falha de seu servidor único como algo a se considerar. 

Componentes desacoplados versus arquitetura monolítica refere-se à forma como um sistema de software é estruturado e como seus diferentes módulos ou componentes interagem entre si. Aqui está uma explicação comparativa entre os dois:

1. Arquitetura Monolítica:
   - Na arquitetura monolítica, todo o aplicativo é construído como uma única unidade.
   - Todos os componentes, funcionalidades e camadas do aplicativo estão fortemente acoplados, o que significa que estão intimamente interconectados e dependem uns dos outros.
   - Qualquer mudança em uma parte do aplicativo pode afetar outras partes, tornando as atualizações e manutenções mais complexas.
   - Essa abordagem é adequada para aplicativos simples e pequenos, mas pode se tornar difícil de gerenciar à medida que cresce em tamanho e complexidade.

2. Componentes Desacoplados (ou Arquitetura de Microsserviços):
   - Na arquitetura de componentes desacoplados, o aplicativo é dividido em vários componentes ou microsserviços independentes.
   - Cada componente possui sua própria funcionalidade e é projetado para operar de forma independente, com sua própria lógica de negócios, banco de dados e interface de programação.
   - Os componentes se comunicam entre si por meio de interfaces bem definidas, como APIs, e não compartilham sua lógica interna.
   - Isso facilita a escalabilidade, o desenvolvimento, a manutenção e as atualizações, pois as mudanças em um componente não afetam os outros.
   - Essa abordagem é adequada para aplicativos complexos e de grande escala, onde a flexibilidade e a escalabilidade são essenciais.

A arquitetura monolítica é mais adequada para aplicativos pequenos e simples, onde a simplicidade de desenvolvimento e implantação é prioritária. Por outro lado, a arquitetura de componentes desacoplados, como os microsserviços, é preferida para aplicativos complexos e escaláveis, onde a manutenção e a escalabilidade são preocupações críticas. A escolha entre essas abordagens depende das necessidades específicas do projeto e dos requisitos de negócios.

Implemente elasticidade na nuvem versus on-premises:
A elasticidade na nuvem é geralmente mais simples de implementar e oferece maior flexibilidade, pois você pode dimensionar recursos sob demanda e pagar apenas pelo que usa. Por outro lado, a escalabilidade on-premises requer planejamento cuidadoso e investimentos em hardware que podem não ser tão eficientes quanto os recursos de nuvem sob demanda. A escolha depende das necessidades, recursos e estratégias específicas de uma organização.

pense paralelo: é parecido com desacoplar, mas você vai está analisando como pode dividir uma tarefa de forma mais facil e, entâo, distribuir essa carga para vários componentes para lidar com a demanda.

### Perguntas sobre AWS Desing Principles

Qual das opções representa um princípio de projeto de arquitetura da AWS Clou?

a - Implementar pontos únicos de falha
b - Implementar acoplamento fraco 🟢
c - Implementar projeto monolítico
d - Implementar scaling vertical

A e C são antipadrões ou conceitos que vão contra as praticas recomendadas,
O C é o antipadrão da nossa chave 
O D é quase um principio de design, exceto que o principio recomenda que devemos implementar o scaling horizontal e não o vertical.