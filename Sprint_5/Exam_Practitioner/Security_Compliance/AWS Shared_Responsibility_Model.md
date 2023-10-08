## O AWS Shared Responsibility Model

O AWS Shared Responsibility Model (Modelo de Responsabilidade Compartilhada da AWS) é um conceito fundamental na plataforma de serviços em nuvem da Amazon Web Services (AWS). Esse modelo define as responsabilidades de segurança compartilhadas entre a AWS e seus clientes, delineando claramente quem é responsável por proteger quais componentes da infraestrutura em nuvem. É essencial para entender como a segurança funciona na AWS. Aqui está uma visão geral:

1. **Responsabilidade da AWS (Fornecedora de Nuvem):**
   - A AWS é responsável pela segurança da infraestrutura física e da virtualização subjacente, incluindo servidores, armazenamento e rede.
   - Isso inclui a proteção dos data centers, a segurança física, a segurança dos sistemas de virtualização e a garantia de que os serviços em nuvem da AWS estejam disponíveis e funcionando adequadamente.

2. **Responsabilidade do Cliente:**
   - Os clientes da AWS são responsáveis pela segurança de tudo o que eles constroem ou armazenam na nuvem, o que inclui seus dados, aplicativos e configurações.
   - Isso envolve a configuração e o gerenciamento adequados dos recursos em nuvem, como instâncias EC2, bancos de dados RDS, redes VPC, etc.
   - Os clientes também são responsáveis por configurar e gerenciar o acesso e as credenciais, bem como implementar medidas de segurança específicas em seus próprios sistemas e aplicativos.

Resumindo, a AWS cuida da segurança da infraestrutura física e dos serviços em nuvem que ela oferece, enquanto os clientes são responsáveis por proteger os dados e os sistemas que constroem e operam na plataforma da AWS. Isso significa que os clientes precisam configurar suas instâncias, redes e sistemas adequadamente, bem como implementar boas práticas de segurança, como o gerenciamento de identidade e acesso, criptografia, monitoramento e auditoria, para garantir a segurança de suas cargas de trabalho na nuvem.

É importante entender essa divisão de responsabilidades ao planejar e implementar soluções na AWS para garantir que todos os aspectos da segurança sejam tratados de forma apropriada e eficaz.

A imagem abaixo ajuda a entender o quem é responsavel pelo o que:

(Responsabilidades Cliente/AWS)[https://github.com/CarlosRyan07/Programa-Bolsas-CompassUOL/blob/main/Sprint_5/Exam_Practitioner/img/Captura%20de%20tela%202023-10-08%20162404.png]