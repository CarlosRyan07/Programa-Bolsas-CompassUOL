#!C:/Users/carlo/AppData/Local/Microsoft/WindowsApps/python3.11
class Potencia:
    # Calcula uma potência específica
    def __init__(self, expoente):
        self.expoente = expoente

    def __call__(self, base):
        return base ** self.expoente


if __name__ == '__main__':
    quadrado = Potencia(2)
    cubo = Potencia(3)

    if callable(quadrado) and callable(cubo):
        print(f'9² => {quadrado(9)}')
        print(f'6³ => {cubo(6)}')
        print(Potencia(2)(5))
