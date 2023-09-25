#E1

# Você está recebendo um arquivo contendo 10.000 números inteiros, um em cada linha.
# Utilizando lambdas e high order functions, apresente os 5 maiores valores pares e a soma destes.

# Você deverá aplicar as seguintes funções no exercício:
# map
# filter
# sorted
# sum


# Seu código deverá exibir na saída (simplesmente utilizando 2 comandos `print()`):

# a lista dos 5 maiores números pares em ordem decrescente;

# a soma destes valores.

# os numeros estavam disponiveis na plateforma da udemy

with open('number.txt', 'r') as arquivo:
    numeros = list(map(int, arquivo.readlines()))

numeros_pares = filter(lambda x: x % 2 == 0, numeros)

# Ordena os números pares em ordem decrescente
numeros_pares_ordenados = sorted(numeros_pares, reverse=True)

# Pega os 5 maiores números pares
cinco_maiores_pares = numeros_pares_ordenados[:5]

# Calcula a soma dos 5 maiores números pares
soma_cinco_maiores = sum(cinco_maiores_pares)

# Os 5 maiores números pares em ordem decrescente
print(cinco_maiores_pares)
# A soma desses números
print(soma_cinco_maiores)
