#!C:/Users/carlo/AppData/Local/Microsoft/WindowsApps/python3.11
arquivo = open('Sprint 3\manipulacao_arquivos\pessoas.csv')

for registro in arquivo:
    print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

arquivo.close()
