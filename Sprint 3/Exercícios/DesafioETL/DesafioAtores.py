# Função para ler o arquivo actors.csv e retornar os dados como uma lista de dicionários
def ler_arquivo_csv(arquivo):
    dados = []
    with open(arquivo, 'r', encoding='utf-8') as file:
        linhas = file.readlines()
        colunas = linhas[0].strip().split(',')
        for linha in linhas[1:]:
            valores = linha.strip().split(',')
            linha_dict = {colunas[i]: valores[i] for i in range(len(colunas))}
            dados.append(linha_dict)
    return dados

def tratar_valor_monetario(valor):
    valor = valor.replace(',', '').replace('$', '').replace(' mil', '')
    try:
        return float(valor)
    except ValueError:
        return 0.0

def encontrar_maior_numero_filmes(dados):
    maior_numero_filmes = 0
    ator_maior_numero_filmes = ""
    for linha in dados:
        try:
            numero_filmes = float(linha['Number of Movies'])
            if numero_filmes > maior_numero_filmes:
                maior_numero_filmes = numero_filmes
                ator_maior_numero_filmes = linha['Actor']
        except ValueError:
            print(f"Erro: Não foi possível converter 'Number of Movies' para float em {linha['Actor']}. Valor: {linha['Number of Movies']}")
    return ator_maior_numero_filmes, maior_numero_filmes

def calcular_media_receita(dados):
    total_gross = 0
    total_filmes = 0
    for linha in dados:
        total_gross += tratar_valor_monetario(linha['Total Gross'])
        total_filmes += 1
    return total_gross / total_filmes

def encontrar_maior_media_receita(dados):
    maior_media_receita = 0
    ator_maior_media_receita = ""
    for linha in dados:
        try:
            media_receita = float(linha['Average per Movie'])
            if media_receita > maior_media_receita:
                maior_media_receita = media_receita
                ator_maior_media_receita = linha['Actor']
        except ValueError:
            print(f"Erro: Não foi possível converter 'Average per Movie' para float em {linha['Actor']}. Valor: {linha['Average per Movie']}")
    return ator_maior_media_receita, maior_media_receita

def contar_filmes_mais_lucrativos(dados):
    filmes_mais_lucrativos = {}
    for linha in dados:
        filme_mais_lucrativo = linha['#1 Movie']
        if filme_mais_lucrativo in filmes_mais_lucrativos:
            filmes_mais_lucrativos[filme_mais_lucrativo] += 1
        else:
            filmes_mais_lucrativos[filme_mais_lucrativo] = 1
    return filmes_mais_lucrativos

def ordenar_atores_por_receita(dados):
    return sorted(dados, key=lambda x: -tratar_valor_monetario(x['Total Gross']))

dados_atores = ler_arquivo_csv('actors.csv')

ator_maior_numero_filmes, maior_numero_filmes = encontrar_maior_numero_filmes(dados_atores)
media_receita = calcular_media_receita(dados_atores)
ator_maior_media_receita, maior_media_receita = encontrar_maior_media_receita(dados_atores)
filmes_mais_lucrativos = contar_filmes_mais_lucrativos(dados_atores)
atores_ordenados = ordenar_atores_por_receita(dados_atores)

# Escrever resultados nos arquivos
with open('etapa-1.txt', 'w', encoding='utf-8') as file:
    file.write(f'{ator_maior_numero_filmes} - {int(maior_numero_filmes)} filmes\n')

with open('etapa-2.txt', 'w', encoding='utf-8') as file:
    file.write(f'Média de receita bruta dos principais filmes: {media_receita:.2f} milhões de dólares\n')

with open('etapa-3.txt', 'w', encoding='utf-8') as file:
    file.write(f'{ator_maior_media_receita} - Média de receita bruta por filme: {maior_media_receita:.2f} milhões de dólares\n')

with open('etapa-4.txt', 'w', encoding='utf-8') as file:
    for filme, frequencia in sorted(filmes_mais_lucrativos.items(), key=lambda x: (-x[1], x[0])):
        file.write(f'{filme} - O filme {filme} aparece {frequencia} vez(es) no dataset\n')

with open('etapa-5.txt', 'w', encoding='utf-8') as file:
    for linha in atores_ordenados:
        file.write(f'{linha["Actor"]} - {linha["Total Gross"]} milhões de dólares\n')
