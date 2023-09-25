# Escreva uma função que recebe um número variável de parâmetros não nomeados e 
# um número variado de parâmetros nomeados e imprime o valor de cada parâmetro recebido.
# Teste sua função com os seguintes parâmetros: 
# (1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)

def imprimir_parametros(*args, **kwargs):
    # Imprime os valores dos parâmetros não nomeados
    for parametro in args:
        print(parametro)
    
    # Imprime os valores dos parâmetros nomeados
    for valor in kwargs.values():
        print(f"{valor}")

# Teste da função com diferentes parâmetros
imprimir_parametros(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)