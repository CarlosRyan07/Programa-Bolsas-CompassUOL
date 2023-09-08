class Data:
    def __init__(self, dia=1, mes=1, ano=1970):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data(5, 12, 2000)
# d1.dia = 5
# d1.mes = 12
# d1.ano = 2000
print(d1)

d2 = Data(ano=2023, mes=8)
d2.dia = 7
# d2.mes = 8
# d2.ano = 2023
print(d2)
