#!C:/Users/carlo/AppData/Local/Microsoft/WindowsApps/python3.11
class Animal:
    @property
    def capacidades(self):
        return ('dormir', 'comer', 'beber')


class Homem(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('amar', 'falar', 'estudar')


class Aranha(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('fazer teia', 'andar pelas paredes')


class HomemAranha(Homem, Aranha):
    @property
    def capacidades(self):
        return super().capacidades + \
            ('bater em bandidos', 'atirar teias entre prédios') # com esse super ele vai chamar dos 2, Homem e Aranha


if __name__ == '__main__':
    john = Homem()
    print(f'John: {john.capacidades}')

    aranha = Aranha()
    print(f'Aranha: {aranha.capacidades}')

    peter = HomemAranha()
    print(f'Peter Parker: {peter.capacidades}')
