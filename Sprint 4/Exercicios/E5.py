# E5

# Um determinado sistema escolar exporta a grade de notas dos estudantes em formato CSV.
# Cada linha do arquivo corresponde ao nome do estudante, acompanhado de 5 notas de avaliação, no intervalo [0-10].
# É o arquivo estudantes.csv de seu exercício.

# Precisamos processar seu conteúdo, de modo a gerar como saída um relatório em formato textual contendo as seguintes informações:

# Nome do estudante

# Três maiores notas, em ordem decrescente

# Média das três maiores notas, com duas casas decimais de precisão

# O resultado do processamento deve ser escrito na saída padrão (print), 
# ordenado pelo nome do estudante e obedecendo ao formato descrito a seguir:


# Nome: <nome estudante> Notas: [n1, n2, n3] Média: <média>

# Exemplo:

# Nome: Maria Luiza Correia Notas: [7, 5, 5] Média: 5.67
# Nome: Maria Mendes Notas: [7, 3, 3] Média: 4.33

# Em seu desenvolvimento você deverá utilizar lambdas e as seguintes funções: round, map, sorted

import csv

# Função lambda para calcular a média das notas
calcular_media = lambda notas: round(sum(notas) / len(notas), 2)  # Use 2 casas decimais

with open('estudantes.csv', 'r') as arquivo:
    leitor_csv = csv.reader(arquivo)

    
    resultados = []

    for linha in leitor_csv:
        nome, *notas = linha  # Use o operador * para pegar todas as notas restantes como uma lista
        notas = list(map(int, notas))  # Converter para inteiros
        
        # Classifique as notas em ordem decrescente
        notas_ordenadas = sorted(notas, reverse=True)
        
        # Pegue as três melhores notas
        tres_melhores = notas_ordenadas[:3]
        
        media = calcular_media(tres_melhores)
        
        # Use a função format para formatar a média com duas casas decimais
        media_formatada = "{:.2f}".format(media)  # Formato de ponto flutuante com 2 casas decimais
        if media_formatada.endswith('.00'):
            media_formatada = media_formatada[:-1] 
        
        resultados.append((nome, tres_melhores, media_formatada))

    resultados_ordenados = sorted(resultados, key=lambda x: x[0])
    
    for nome, notas, media in resultados_ordenados:
        print(f"Nome: {nome} Notas: {notas} Média: {media}")
