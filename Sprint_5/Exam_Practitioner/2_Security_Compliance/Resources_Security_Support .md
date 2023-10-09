## Resources Security Support 

A Amazon Web Services (AWS) oferece vários recursos e serviços de suporte à segurança para ajudar os clientes a proteger seus ambientes na nuvem. Esses recursos são úteis em diferentes cenários e podem ser usados em várias etapas do ciclo de vida de segurança. Aqui estão alguns dos principais recursos de suporte à segurança da AWS e quando usá-los:

1. **AWS Trusted Advisor**:
   - O AWS Trusted Advisor é uma ferramenta que analisa sua infraestrutura na AWS em busca de oportunidades de economia de custos, desempenho, segurança e conformidade.
   - Usamos o Trusted Advisor para identificar configurações inseguras, como portas abertas não necessárias em grupos de segurança ou chaves de acesso não utilizadas.

2. **AWS Identity and Access Management (IAM)**:
   - O IAM é usado para gerenciar identidades e permissões na AWS.
   - Usamos o IAM para criar e gerenciar contas de usuário, grupos e papéis, definir políticas de acesso granular e implementar autenticação de vários fatores (MFA) para aumentar a segurança do acesso.

3. **AWS Key Management Service (KMS)**:
   - O KMS permite criar e gerenciar chaves criptográficas para proteger dados em serviços da AWS e em nossas próprias aplicações.
   - Usamos o KMS para criptografar dados sensíveis e gerenciar o acesso às chaves de criptografia.

4. **Amazon GuardDuty**:
   - O GuardDuty é um serviço de detecção de ameaças que monitora atividades maliciosas ou não autorizadas em sua conta da AWS.
   - Usamos o GuardDuty para identificar e responder a ameaças de segurança em tempo real.

5. **AWS Inspector**:
   - O AWS Inspector ajuda a avaliar a segurança de nossas aplicações executadas na AWS, identificando vulnerabilidades e violações de melhores práticas de segurança.
   - Usamos o Inspector para realizar varreduras de segurança regulares em nossas instâncias EC2 e aplicações.

6. **Amazon Macie**:
   - O Macie é um serviço de segurança que ajuda a proteger dados confidenciais, identificando automaticamente dados sensíveis em sua conta e monitorando o acesso a esses dados.
   - Usamos o Macie para proteger dados confidenciais e cumprir regulamentos de privacidade.

7. **AWS WAF (Web Application Firewall)**:
   - O AWS WAF protege nossas aplicações web contra ataques comuns, como injeção SQL e cross-site scripting (XSS).
   - Usamos o WAF para proteger nossas aplicações web contra ameaças online.

8. **AWS Organizations**:
   - O AWS Organizations permite criar e gerenciar várias contas AWS em uma hierarquia organizacional.
   - Usamos o Organizations para centralizar o gerenciamento de segurança em várias contas e aplicar políticas de segurança consistentes.

9. **AWS CloudTrail**:
   - O CloudTrail registra todas as ações realizadas em sua conta da AWS, permitindo a auditoria e trilha de atividades.
   - Usamos o CloudTrail para investigar atividades suspeitas e manter um registro de auditoria.

Devemos usar esses recursos de acordo com as necessidades específicas de segurança de sua organização e como parte de uma abordagem abrangente de segurança na nuvem. É importante monitorar regularmente e ajustar nossas configurações de segurança para garantir que você esteja protegendo eficazmente seus recursos na AWS.

### Resources Security Support

Q - Qual serviço ou recurso da AWS ppode ser usado para impdir ataques de injeção SQL?

a - Grupos de Segurança
(são firewalls no nível da instância para controlar o acesso às instâncias do amazon EC2, não podem impedir)
b -  AcLs de rede  
(são firewalls no nível da sub-rede para controlar o acesso ao tráfego de entrada e saída, não podem impedir)
c - AWS WAF🟢
(é um serviço de firewall de aplicativos da web que protege aplicativos web contra ataques comuns, como injeção SQL e cross-site scripting (XSS))
d - Politicas do AWS Identity and Access Management (IAM)
(permitem controlar o acesso a recursos da AWS, não podem impedir)



