#!C:/Users/carlo/AppData/Local/Microsoft/WindowsApps/python3.11

try:
    arquivo = open('Sprint 3\manipulacao_arquivos\pessoas.csv')

    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
finally:
    arquivo.close()

if arquivo.closed:
    print('Arquivo já foi fechado!')
