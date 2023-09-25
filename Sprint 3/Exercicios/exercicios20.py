# Imprima a lista abaixo de trás para frente.

a = [1, 0, 2, 3, 5, 8, 13, 21, 34, 55, 89]
a_inversa = []
for i in range(len(a) - 1, -1, -1):
    a_inversa.append(a[i])
    
print(a_inversa)