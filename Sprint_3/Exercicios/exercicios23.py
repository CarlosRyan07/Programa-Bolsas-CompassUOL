# Crie uma classe  Calculo  que contenha um método que aceita dois parâmetros, X e Y, e retorne a soma dos dois. 
# Nessa mesma classe, implemente um método de subtração, que aceita dois parâmetros, X e Y, e retorne a subtração dos dois (resultados negativos são permitidos).

class Calculo:
    def somar(self,x,y):
        return x + y

    def subtrair(self,x,y):
        return x - y


calculadora = Calculo()

print(f"Somando: {calculadora.somar(4,5)}")
print(f"Subtraindo: {calculadora.subtrair(4,5)}")






