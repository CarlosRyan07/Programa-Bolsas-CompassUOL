# Escreva um código Python para verificar se três números digitados na entrada padrão são pares ou ímpares.
# Para cada número, imprima como saída Par: ou Ímpar: e o número correspondente (um linha para cada número lido).
# Importante: Aplique a função range() em seu código.

numeros = [int(input(f"Digite o {i + 1}° número: ")) for i in range(3) ]
    
for numero in numeros:
    tipo = "Par" if numero % 2 == 0 else "Ímpar"
    print(f"{tipo}: {numero}")
