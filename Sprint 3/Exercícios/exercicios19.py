import random
# amostra aleatoriamente 50 números do intervalo 0...500
random_list = random.sample(range(500), 50)
# Obs.: Lembrem-se, para calcular a mediana a lista deve estar ordenada!

mediana = 0
media = 0
valor_minimo = 0
valor_maximo = 0

# Ordena a lista para calcular a mediana
random_list.sort()

# Calcula a mediana
tamanho = len(random_list)
# Para calcular a mediana, você verifica se o tamanho da lista é par ou ímpar.
if tamanho % 2 == 0:
    # Se for par, você calcula a média dos dois valores do meio, caso contrário, pega o valor do meio diretamente.
    mediana = (random_list[tamanho // 2 - 1] + random_list[tamanho // 2]) / 2
else:
    mediana = random_list[tamanho // 2]

# Calcula a média
media = sum(random_list) / len(random_list)

# Calcula o valor mínimo e máximo
valor_minimo = min(random_list)
valor_maximo = max(random_list)

print(f'Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}')
