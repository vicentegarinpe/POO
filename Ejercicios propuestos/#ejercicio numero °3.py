#ejercicio propuesto

class Fraccion:
    
    def __init__(self,numerador,denominador) :
        self.numerador=numerador
        self.denominador=denominador
    
    def __str__(self) :       # representacion de cadena
        return f"{self.numerador} {self.denominador}"
    
    def __add__(self,frac):      #suma de las dos fracciones
        return (self.numerador/self.denominador)+(frac.numerador/frac.denominador)
    
    def __mul__(self,frac):
        return(self.numerador/self.denominador)*(frac.numerador/frac.denominador)
    
    def __eq__(self,frac):
        return(self.numerador/self.denominador)==(frac.denominador)