#!C:/Users/carlo/AppData/Local/Microsoft/WindowsApps/python3.11

with open('Sprint 3\manipulacao_arquivos\pessoas.csv') as arquivo:
    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

if arquivo.closed:
    print('Arquivo já foi fechado!')
