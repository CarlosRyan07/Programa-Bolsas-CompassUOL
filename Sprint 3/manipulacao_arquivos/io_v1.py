#!C:/Users/carlo/AppData/Local/Microsoft/WindowsApps/python3.11
# Em strings do Python, as barras invertidas são usadas como caracteres de escape, o que pode causar problemas
# quando você está especificando caminhos de arquivo no Windows, pois o
# Python interpreta as barras invertidas "(/)" como caracteres de escape em vez de caracteres literários de diretório.
#Existem algumas maneiras de resolver isso:

#Dupla Barra Invertida (\\)
#Barra Invertida Bruta (r"caminho\para\arquivo")
#Copiando o Relative Path da certooooo!!!!

#pra rodar pelo code runner direto!
arquivo = open('Sprint 3\manipulacao_arquivos\pessoas.csv') 

#arquivo = open('pessoas.csv') #para rodar assim acesse direto pelo terminal
dados = arquivo.read()
arquivo.close()
for registro in dados.splitlines():
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))
