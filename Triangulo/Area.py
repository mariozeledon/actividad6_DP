import math

class Areas:
    #atributos
    numA=0
    numB=0
    resultado=0
    
    #metodos
    def asignarCatA(self,base):
        self.numA = base

    def asignarCatB(self,altura):
        self.numB = altura

    def hipotenusa(self):
        self.resultado=(self.numA*self.numB)/2
        print("El área del triángulo es: ",self.resultado)