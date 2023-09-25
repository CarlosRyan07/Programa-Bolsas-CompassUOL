#!C:/Users/carlo/AppData/Local/Microsoft/WindowsApps/python3.11

pessoas = [
    {'nome': 'Carlos', 'idade': 23},
    {'nome': 'Maria', 'idade': 37},
    {'nome': 'Aristides', 'idade': 26},
    {'nome': 'Rebeca', 'idade': 6},
    {'nome': 'Tiago', 'idade': 19},
    {'nome': 'Gabriela', 'idade': 17},
]

# Dessa forma ele mostra as pessoas que tiverem menos de 18
menores = filter(lambda p: p['idade'] < 18, pessoas)
print(list(menores))

nomes_grandes = filter(lambda p: len(p['nome']) >= 7, pessoas)
print(tuple(nomes_grandes))
