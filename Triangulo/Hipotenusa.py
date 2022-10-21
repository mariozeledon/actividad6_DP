import math

class Hipotenusa:
    #atributos
    numA=0
    numB=0
    resultado=0
    
    #metodos
    def asignarCatA(self,catetoA):
        self.numA = catetoA

    def asignarCatB(self,catetoB):
        self.numB = catetoB

    def hipotenusa(self):
        self.resultado=math.sqrt(self.numA**2+self.numB**2)
        print("La hipotenusa del triángulo es: ",self.resultado)