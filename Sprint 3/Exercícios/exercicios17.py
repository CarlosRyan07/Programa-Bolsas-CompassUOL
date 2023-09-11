# Escreva uma função que recebe como parâmetro uma lista e retorna 3 listas: 
# a lista recebida dividida em 3 partes iguais. Teste sua implementação com a lista abaixo


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def divide_lista(lista):
    # utilizei // para garantir que seja um número inteiro:
    tamanho_parte = len(lista) // 3  

    parte1 = lista[:tamanho_parte]
    parte2 = lista[tamanho_parte:2 * tamanho_parte]
    parte3 = lista[2 * tamanho_parte:]

    return parte1, parte2, parte3

parte1, parte2, parte3 = divide_lista(lista)

# Imprime as três partes separadas por espaços como pede na Questão
print(parte1, parte2, parte3)





