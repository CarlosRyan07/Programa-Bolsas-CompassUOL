# E2

# Utilizando high order functions, implemente o corpo da função conta_vogais.
# O parâmetro de entrada será uma string e o resultado deverá ser a contagem de vogais presentes em seu conteúdo.

# É obrigatório aplicar as seguintes funções:

# len
# filter
# lambda

# Desconsidere os caracteres acentuados. Eles não serão utilizados nos testes do seu código.

def conta_vogais(texto):
    is_vogal = lambda char: char.lower() in 'aeiou'
    vogais = filter(is_vogal, texto.lower())
    quantidade_vogais = len(list(vogais))
    
    return quantidade_vogais


texto = "Acerto é me contratar haha"
resultado = conta_vogais(texto)
print(f"O número de vogais no texto é: {resultado}")
