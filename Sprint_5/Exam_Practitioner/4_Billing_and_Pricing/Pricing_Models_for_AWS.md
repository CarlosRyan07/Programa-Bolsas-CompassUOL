## Pricing Models for AWS

Modelo de preço da Amazon EC2:

1. **Instâncias sob demanda:**
   - Este é o modelo mais flexível e sem compromisso oferecido pela Amazon EC2.
   - Os clientes pagam apenas pelo tempo em que as instâncias estão em execução, com preços normalmente expressos em termos de horas ou segundos de uso.
   - Não há contrato de longo prazo, pagamento adiantado ou compromisso de uso mínimo. Os clientes podem iniciar e encerrar instâncias conforme necessário.
   - Embora as instâncias sob demanda ofereçam flexibilidade, elas podem ser mais caras em comparação com outras opções, especialmente se você estiver usando-as continuamente a longo prazo. No entanto, elas ainda são consideradas econômicas para cargas de trabalho intermitentes ou variáveis.

2. **Instâncias reservadas:**
   - As instâncias reservadas permitem aos clientes reservar capacidade de computação em instâncias EC2 por um período fixo, geralmente 1 ou 3 anos.
   - Essas reservas normalmente resultam em um significativo desconto em comparação com as instâncias sob demanda. Quanto mais longo for o compromisso (por exemplo, um contrato de 3 anos), maior será o desconto.
   - As instâncias reservadas são ideais para cargas de trabalho previsíveis e estáveis, onde você pode antecipar o uso de recursos a longo prazo.
   - Elas estão disponíveis em diferentes tipos de instância (como instâncias de propósito geral, otimizadas para CPU ou otimizadas para memória) para atender às necessidades específicas de sua carga de trabalho.

3. **Instâncias spot:**
   - Pode dar descontos de até 90% em relação ao preço sob demanda, mas não garante que a instancia sera executada, pois o preço varia de acordo com a oferta e demanda.
   - As instâncias spot permitem que os clientes aproveitem os recursos de computação não utilizados disponíveis na nuvem a preços muito mais baixos do que as instâncias sob demanda.
   - No entanto, os preços das instâncias spot são altamente variáveis e dependem da oferta e da demanda na nuvem. Isso significa que o preço pode flutuar e que a Amazon pode interromper a instância spot com aviso prévio curto quando a capacidade é necessária para outros fins.
   - As instâncias spot são adequadas para cargas de trabalho tolerantes a interrupções, onde a execução não contínua da carga de trabalho não é crítica e pode ser retomada em outro lugar se a instância for interrompida.
   - É importante notar que as instâncias spot são mais econômicas, mas menos previsíveis do que as instâncias sob demanda ou reservadas.

A escolha entre essas opções de instância EC2 depende das necessidades específicas de sua aplicação ou carga de trabalho, bem como de seu orçamento. A Amazon EC2 oferece essa variedade de opções para que os clientes possam otimizar os custos de acordo com suas exigências individuais de computação na nuvem.

## Perguntas sobre Pricing Models for AWS

Q -  Uma empresa tem um aplicativo que só precisa ser executado por duas horas em algum momento do dia. Qual tipo de instância EC2 é mais econômico para esse aplicativo?

a - Instâncias dedicadas
b - Instâncias sob demanda
c - Instâncias reservadas
d - Instâncias spot🟢

A resposta é a letra D, pois as instâncias spot são mais econômicas podendo dar descontos de até 90%, mas menos previsíveis do que as instâncias sob demanda ou reservadas.