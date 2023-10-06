## A resiliência operacional

 É o benefício conquistado com a melhoria na disponibilidade e na segurança. Isso representa mais tempo ativo, menos tempo de inatividade e risco reduzido. 
 Ao pensar em resiliência operacional, duas coisas vêm à mente: tempo ativo e segurança. Manter uma infraestrutura operacionalmente resiliente e disponível envolve vários componentes, da camada de rede, servidores e armazenamento, à camada de banco de dados. Cada componente de um aplicativo precisa estar disponível.



O tempo de inatividade resulta em efeitos macro para as empresas, muitas vezes com consequências significativas. Por exemplo:

Uma interrupção no data center de uma empresa aérea cancelou 2.000 voos e custou mais de 150 milhões de dólares. 
Um banco experimentou um longo tempo de inatividade por causa de um ataque de negação de serviço distribuído (DDoS), o que afetou a confiança dos clientes, e etc.

Esses eventos de tempo de inatividade custam às empresas da Fortune 1000 entre 1,25 e 2,5 bilhões de dólares anualmente, com prejuízos por falhas em aplicativos essenciais que chegam a 1 milhão de dólares por hora.

Em 2020, o tempo de inatividade médio de uma única interrupção foi de 79 minutos, a um custo médio de USD 84.650 por hora. 
A recuperação de ataques cibernéticos custa em média USD 4,6 milhões para as organizações, sem incluir qualquer pagamento de ransomware ao invasor.
 
Esses custos de tempo de inatividade incluem:

* Taxas de terceiros
* Substituição de equipamentos
* Custos incidentais após o ocorrido
* Atividades e custos de recuperação
* Custos de detecção associados à descoberta inicial e investigações subsequentes
* Equipe de TI improdutiva e custos de usuários finais
* Perda de receita
* Custos de interrupção dos negócios
* E muito mais 

Muitas vezes, as causas do tempo de inatividade não são os ataques externos. O tempo de inatividade costuma ocorrer porque a demanda de serviços excede a capacidade da infraestrutura para atendê-la. 
É por isso que o tempo de inatividade geralmente ocorre durante os horários de pico, enquanto o banco de dados está com um número excessivo de consultas.


Ao quantificar o impacto, usamos uma pesquisa líder de terceiros para ajudar a orientar os negócios. 
Aqui, uma informação interessante é que o custo da interrupção dos negócios é maior que o custo da perda de receita!! . Isso significa que o prejuízo para a marca da empresa, a rotatividade dos clientes e a perda de oportunidades são maiores que a perda da receita. Mesmo para aplicativos internos, os impactos na produtividade dos negócios geram custos de downstream muito elevados para uma empresa. Além disso, a interrupção dos negócios é equivalente às perdas econômicas, incluindo danos à reputação, rotatividade dos clientes e perda de oportunidades.

### Pilares da resiliência operacional

**Operações:** fala sobre as causas principais de falhas operacionais, estão inclusas:
 Erros humanos, erros de configuração, erros de procedimentos e acidentes comuns no data center. 
 
 Na AWS, a ênfase está na alta segurança e na gestão cuidadosa de regras para identificar ameaças antecipadamente e evitar desastres. A AWS utiliza automação, gerenciamento de serviços, visibilidade de todo o sistema, configurações de segurança e governança, e monitoramento de acesso à API para mitigar interrupções operacionais e desastres.


**Segurança:** fala sobre as causas de violações de segurança, incluindo:
 Malware, ataques de rede, falta de aplicação de patches em aplicativos ou sistemas operacionais, problemas de segurança relacionados a senhas e autenticação precária. O exemplo de Mike destaca como decisões subjetivas podem levar a violações de segurança.
 
 Na AWS, o modelo de segurança compartilha responsabilidades com os clientes, onde a AWS é responsável pela segurança desde o nível do hipervisor até o sistema operacional. Isso reduz os riscos de segurança, utilizando automação e ferramentas da AWS para minimizar riscos graves, oferecendo o serviço AWS Identity Access Management (IAM) para gerenciar usuários e credenciais centralmente e obtendo várias certificações de conformidade para criar ambientes seguros e em conformidade para os clientes.

**Software:** fala sobre as causas comuns de falhas na resiliência do software. Elas incluem:
 Esgotamento de recursos, como processos descontrolados, vazamentos de memória e aumento de arquivos
 Erros de computação ou de lógica, como referências incorretas, indicadores corrompidos e erros de sincronização
 Monitoramento inadequado, como inabilidade de identificar problemas
 Atualizações com falha, como intercompatibilidade e integrações
 A AWS oferece serviços para que os clientes possam aumentar ou reduzir os recursos necessários e fazer com que a AWS gerencie as alterações. 

 Para fornecer resiliência de software, a AWS:

 Oferece implantações azuis/verdes que permitem reversões rápidas
 Automatiza a integração e o fluxo de trabalho de entrega contínuos
 Executa implantações de código menores para reduzir bugs de unidade, de integração e do sistema
 Fornece recursos atuais e seguros com aplicação de patches do sistema operacional
 Cria e gerencia um conjunto de recursos relacionados da AWS

**Infraestrutura:** fala sobre as causas de falhas na infraestrutura. Elas incluem:

 Falha de hardware de servidores, armazenamento ou redes
 Desastres naturais, como furacões, inundações e terremotos
 Interrupções de energia, como falha no fornecimento de energia e nas baterias
 Ataques volumétricos, como DDoS e amplificação do Sistema de nomes de domínio (DNS)
 A AWS ajuda a reduzir falhas na infraestrutura de várias maneiras.

 A AWS continua a expandir nossa infraestrutura e lidera o setor em melhorias de data centers em grande escala.
 Nossos clientes podem executar aplicativos e fazer failover em várias zonas de disponibilidade e regiões.
 Os sistemas da AWS são criados para serem altamente disponíveis e duráveis.
 Como padrão, cada zona de disponibilidade em cada região é conectada de modo redundante a vários provedores de trânsito de camada 1.
 Cada instância de computação é atendida por duas fontes de energia independentes, cada uma com serviço público, fonte de alimentação ininterrupta e gerador de energia de backup. 