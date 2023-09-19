#!C:/Users/carlo/AppData/Local/Microsoft/WindowsApps/python3.11
from functools import reduce
from operator import add

valores = [30, 10, 25, 70, 100, 94]

print(sorted(valores))
print(valores)

# valores.sort()
# print(valores)
print(min(valores))
print(max(valores))

print(sum(valores))
print(reduce(add, valores)) # Msm coisa da de cima 

print(reversed(valores))
print(list(reversed(valores)))
print(valores)

# valores.reverse()
# print(valores)
