#ejercicio 1 propuesto

class Persona():

    def __init__(self,nombre,apellido,edad,peso,altura):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.peso=peso
        self.altura=altura

        
    #atributos(variables)
    #nombre="cristina"
    #apellido="torres"
    #edad=23
    #metodos (comportamientos)
    
    def hablar(self):
        print(f"{self.nombre} esta hablando")

    def caminar(self):
        print(f"{self.nombre} esta caminando")
    
    def Imc(self):
        print(f"el IMC de {self.nombre} es:",(self.peso)/(self.altura)**2)
    
    def promedio_asignatura(self, nota1: float, nota2: float, nota3: float):
        promedio = (nota1 + nota2 + nota3) / 3
        if promedio >= 4.0:
            print(f"{self.nombre} aprobó con un promedio de {promedio}.")
        else:
            print(f"{self.nombre} no aprobó. Su promedio es {promedio}.")

#instancioando la clase (creando objetos)
persona1=Persona("cristina","torres",23,63,1.60)

persona2=Persona("benjamin","hada",20,73,1.70,)

#acceso a los atributos y metodos del objeto
print(f"nombre:{persona1.nombre}")
print(f"apellido:{persona1.apellido}")
print(f"edad:{persona1.edad}")

#promedio notas

persona1.promedio_asignatura(3.5, 4.0, 5.0)  
persona2.promedio_asignatura(4.5, 4.5, 3.0)

#calcular imc
persona1.Imc()
persona2.Imc()
