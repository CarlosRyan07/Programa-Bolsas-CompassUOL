## Account Structures with AWS Billing and Pricing

Reconheça as diferentes estruturas de conta em relação a cobrança e preços da AWS.

Explique como várias contas ajudam a alocar custos e em departamentos diferentes

---
A AWS oferece várias opções de estruturas de conta para organizações que desejam alocar custos e gerenciar recursos em departamentos diferentes. Essas estruturas de conta ajudam a controlar os gastos, facilitam o monitoramento e a alocação de recursos, e oferecem flexibilidade para atender às necessidades específicas de uma organização. Aqui estão algumas das principais estruturas de conta em relação à cobrança e preços da AWS:

1. **Conta Consolidada (Consolidated Billing):** Essa é a estrutura mais comum para organizações com várias equipes ou departamentos. Nesse modelo, uma conta principal (a conta de pagamento) é vinculada a várias subcontas (contas associadas). Cada subconta é tratada como uma unidade de faturamento separada, mas os custos são consolidados em uma única fatura. Isso facilita a centralização do pagamento e a obtenção de uma visão unificada dos gastos da organização.

2. **Contas Separadas (Separate Accounts):** Algumas organizações preferem manter contas totalmente independentes para cada departamento ou equipe. Isso oferece um alto grau de isolamento, mas pode ser mais desafiador para gerenciar centralmente os custos. Cada conta tem seu próprio método de pagamento e é faturada separadamente.

3. **Organizações da AWS (AWS Organizations):** A AWS Organizations é um serviço que permite criar grupos de contas e hierarquias de contas para organizações complexas. Isso é útil para organizações que desejam ter várias contas associadas a uma conta principal e aplicar políticas de gerenciamento de recursos e segurança em toda a organização.

A alocação de custos e o gerenciamento de departamentos diferentes podem ser facilitados da seguinte forma em estruturas de conta da AWS:

- **Identificação de recursos:** Cada recurso AWS (por exemplo, instâncias EC2, bancos de dados RDS, buckets S3) pode ser marcado com etiquetas (tags) que indicam o departamento ou equipe responsável. Isso ajuda a identificar facilmente a origem dos custos em cada fatura.

- **Acesso controlado:** Com o AWS Identity and Access Management (IAM), você pode configurar permissões granulares para que apenas as equipes relevantes tenham acesso às contas e recursos apropriados. Isso garante que os departamentos não acessem ou gastem recursos de outros departamentos.

- **Relatórios e monitoramento:** A AWS oferece ferramentas como o AWS Cost Explorer e o AWS Cost and Usage Report, que permitem gerar relatórios detalhados de custos e uso. Você pode segmentar esses relatórios com base em etiquetas, contas ou departamentos, facilitando a alocação de custos.

- **Políticas de orçamento:** Através do AWS Budgets, você pode definir orçamentos para cada conta ou departamento. Isso ajuda a monitorar os gastos e a receber alertas quando os custos atingem limites definidos.

A escolha da estrutura de conta da AWS depende das necessidades e da complexidade da organização. Independentemente do modelo escolhido, é importante utilizar boas práticas de etiquetagem, permissões de acesso adequadas e ferramentas de relatórios para garantir uma gestão eficaz dos custos e recursos da AWS em diferentes departamentos.

### Perguntas sobre Account Structures with AWS Billing and Pricing

Q - Qual é o serviço da AWS que as empresas usam para ver, entender e gerenciar custos e uso da AWS ao ongo do tempo?

a - AWS Budgets

b - AWS Cost Explorer🟢

c - AWS Organizations

d - Cobrança Consolidada (Consolidated Billing)

A resposta é a letra B, pois o AWS Cost Explorer é uma ferramenta de visualização de custos que permite analisar e gerenciar os custos e o uso AWS ao longo do tempo.

A letra A é um serviço que permite definir orçamentos personalizados que enviam alertas quando o uso ou custos excedem ou tenham prewvisão de exceder o orçamento. Ele não permite visualizar os custos e uso da AWS ao longo do tempo.

A letra C é um serviço que permite criar grupos de contas e hierarquias de contas para organizações complexas. Ele não permite visualizar os custos e uso da AWS ao longo do tempo.

A letra D é uma estrutura de conta da AWS que permite que uma conta principal (a conta de pagamento) seja vinculada a várias subcontas (contas associadas). Ele não permite visualizar os custos e uso da AWS ao longo do tempo.