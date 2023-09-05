PALAVRAS_PROIBIDAS = {'futebol', 'religião', 'pix'}
textos = [
    'João gosta de urubu do pix',
    'A praia foi divertida',
]

for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print('Texto possui palavras proibidas:', intersecao)
    else:
        print('Texto autorizado:', texto)
