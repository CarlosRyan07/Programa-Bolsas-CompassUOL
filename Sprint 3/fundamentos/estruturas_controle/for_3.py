produto = {'nome': 'Caneta Bic', 'preco': 10.99,
           'importada': True, 'estoque': 500}

for chave in produto:
    print(chave)

for valor in produto.values():
    print(valor)

for chave, valor in produto.items():
    print(chave, '=', valor)

print(chave, valor)
