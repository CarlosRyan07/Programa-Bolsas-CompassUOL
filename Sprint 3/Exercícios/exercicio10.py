# Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados.
# Utilize a lista a seguir para testar sua função.

lista = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']


def listaSemDuplicata(lista):
   return list(set(lista))

print(listaSemDuplicata(lista))