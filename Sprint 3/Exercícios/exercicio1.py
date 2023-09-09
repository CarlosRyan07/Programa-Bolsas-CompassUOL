# Desenvolva um código Python que lê do teclado nome e a idade atual de uma pessoa.
# Como saída, imprima o ano em que a pessoa completará 100 anos de idade.

nome = input("Digite seu nome: ")
idade = int(input("Digite a sua idade: "))

ano_nascimento = 2023 - idade

print(ano_nascimento + 100)