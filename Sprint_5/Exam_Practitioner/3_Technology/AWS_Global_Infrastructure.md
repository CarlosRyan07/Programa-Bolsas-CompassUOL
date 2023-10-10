## Infraestructura Global de AWS: zonas de disponibilidade, regiões e locais de Borda da AWS

1. **Regiões AWS**: As regiões AWS são áreas geográficas geograficamente separadas que contêm um ou mais data centers, conhecidos como "zonas de disponibilidade". Cada região é projetada para ser independente das outras em termos de falhas físicas, como terremotos ou desastres naturais. Isso significa que, se um problema ocorrer em uma região, as outras regiões continuarão funcionando normalmente. A AWS tem regiões em todo o mundo, incluindo América do Norte, América do Sul, Europa, Ásia-Pacífico, Oriente Médio e África.

2. **Zonas de Disponibilidade**: Cada região AWS é composta por várias zonas de disponibilidade (AZs). Uma zona de disponibilidade é essencialmente um ou mais data centers físicos separados dentro de uma região. As AZs são conectadas por redes de alta velocidade e baixa latência, mas são projetadas para serem independentes umas das outras em termos de energia, resfriamento e infraestrutura física. Isso proporciona alta disponibilidade e redundância aos serviços da AWS. Os clientes podem implantar recursos em uma ou mais zonas de disponibilidade para criar aplicativos altamente disponíveis e tolerantes a falhas.

3. **Locais de Borda AWS**: Além das regiões e zonas de disponibilidade, a AWS também possui uma rede global de "Locais de Borda" (Edge Locations). Esses locais de borda são distribuídos em todo o mundo e são usados para armazenar em cache conteúdo e acelerar a entrega de dados para os usuários finais por meio da CDN (Content Delivery Network) da AWS, chamada Amazon CloudFront. Os locais de borda ajudam a reduzir a latência e melhorar o desempenho de aplicativos e serviços que dependem da entrega rápida de conteúdo, como streaming de vídeo, sites e aplicativos da web.
São endpoints que veiculam conteudo de armazenamento em cache e dão acesso a serviços da AWS.

Em resumo, a Infraestrutura Global da AWS é uma rede altamente distribuída e redundante que abrange várias regiões, zonas de disponibilidade e locais de borda em todo o mundo. Essa arquitetura permite que os clientes da AWS implantem seus aplicativos e serviços em uma infraestrutura altamente escalável e confiável, garantindo alta disponibilidade e desempenho para atender às suas necessidades de negócios.

### Perguntas sobre Infraestructura Global de AWS

Q -Qual é o aspecto da infraestrutura global de computação e de armazenamento?

a - Zonas de disponibilidade 
(as zonas de disponibilidade são data centers físicos separados dentro de uma região)

b - Regiões🟢
(as regiões são áreas geográficas isoladas que contêm uma ou mais zonas de disponibilidade)

c - Tags
(as tags são usadas para organizar e gerenciar recursos na AWS, mas não fazem parte da infraestrutura global)

d - Resource Groups
(ele pode facilitar o gereciamento de recursos, mas não permite implantação global de recursos)