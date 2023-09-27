
# E6

# Você foi encarregado de desenvolver uma nova feature  para um sistema de gestão de supermercados. 
# O analista responsável descreveu o requisito funcional da seguinte forma:

# - Para realizar um cálculo de custo, o sistema deverá permitir filtrar um determinado conjunto de produtos, de modo que apenas aqueles cujo valor unitário for superior à média deverão estar presentes no resultado. Vejamos o exemplo:

# Conjunto de produtos (entrada):
Arroz: 4.99
Feijão: 3.49
Macarrão: 2.99
Leite: 3.29
Pão: 1.99

# Produtos com valor acima da média:
Arroz: 4.99
Feijão: 3.49


# Observe que estamos definindo a assinatura de uma função como parte de sua resposta. 
# Você não pode mudá-la, apenas codificar seu corpo. 
# O parâmetro conteudo é um dicionário cuja chave contém o nome do produto e o valor,
# o respectivo preço (ponto flutuante).

# O retorno da função obrigatoriamente deve ser uma lista. 
# Cada elemento da lista é uma tupla em que a primeira posição contém o nome do produto e a segunda, o respectivo preço.
# Veja um exemplo de retorno:


# Importante: O retorno da função deve estar ordenado pelo preço do item (ordem crescente).
def maiores_que_media(conteudo):
    # Calcula a média dos preços dos produtos
    valores = list(conteudo.values())
    media = sum(valores) / len(valores)

    # Filtra os produtos cujo preço é superior à média
    produtos_acima_media = [(produto, preco) for produto, preco in conteudo.items() if preco > media]

    # Ordena a lista de produtos pelo preço em ordem crescente
    produtos_acima_media.sort(key=lambda x: x[1])

    return produtos_acima_media

conteudo = {
    "arroz": 4.99,
    "feijão": 3.49,
    "macarrão": 2.99,
    "leite": 3.29,
    "pão": 1.99
}

resultado = maiores_que_media(conteudo)
print(resultado)
