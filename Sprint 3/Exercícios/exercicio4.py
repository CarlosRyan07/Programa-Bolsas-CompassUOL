# Escreva um código Python para imprimir todos os números primos entre 1 até 100.
# Lembre-se que você deverá desenvolver o cálculo que identifica se um número é primo ou não.

# Função para verificar se um número é primo
def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Itera de 2 a 100 e imprime os números primos
for numero in range(2, 101):
    if eh_primo(numero):
        print(numero)