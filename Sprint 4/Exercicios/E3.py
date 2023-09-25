from functools import reduce

# E3
# A função calcula_saldo recebe uma lista de tuplas, correspondendo a um conjunto de lançamentos bancários.
# Cada lançamento é composto pelo seu valor (sempre positivo) e pelo seu tipo (C - crédito ou D - débito). 

# Abaixo apresentando uma possível entrada para a função.

lancamentos = [
    (200,'D'),
    (300,'C'),
    (100,'C')
]

# A partir dos lançamentos, a função deve calcular o valor final, somando créditos e subtraindo débitos.
# Na lista anterior, por exemplo, teríamos como resultado final 200.

# Além de utilizar lambdas, você deverá aplicar, obrigatoriamente, as seguintes funções na resolução:

#reduce (módulo functools)
#map

def calcula_saldo(lancamentos):
    
    # Função lambda para mapear os créditos (C) como valores positivos e débitos (D) como negativos
    mapeamento = lambda x: x[0] if x[1] == 'C' else -x[0]
    
    # Use a função map para aplicar o mapeamento a cada lançamento
    valores = map(mapeamento, lancamentos)
    
    # Use a função reduce para somar todos os valores
    saldo_final = reduce(lambda x, y: x + y, valores)
    
    return saldo_final

saldo = calcula_saldo(lancamentos)
print("O saldo final é:", saldo)