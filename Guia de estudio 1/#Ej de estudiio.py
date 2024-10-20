#Ej de estudiio
"""Problema: Sistema de Gestión de Empleados
Desarrolla un programa que gestione la información de los empleados de una empresa. Cada empleado tiene un nombre, un salario y un estado de empleo que indica si está activo o no.

Instrucciones:
Clase Empleado
Implementa la clase Empleado con los atributos privados nombre y salario, y el atributo público estado (booleano) que indica si el empleado está activo o no.
Crea un método mágico que muestre de manera legible el nombre, el salario y el estado del empleado.
Crea un método para modificar el salario del empleado de forma controlada.
Implementa un método que evalúe si un empleado está activo o inactivo y que imprima su estado.
Creación y manejo de empleados:

El programa debe permitir la creación de al menos tres empleados con sus respectivos nombres, salarios y estado.
Imprime la información de cada empleado utilizando el método mágico.
Simulación de actualización:

Simula una actualización de salario para uno de los empleados utilizando el método correspondiente.
Evalúa el estado de los empleados llamando al método que verifica si están activos o no, mostrando un mensaje personalizado con el resultado."""

class Empleado(): #inicialize la clase de Empkleado
    def __init__(self,nombre,salario,E_de_empleo):
        self.__nombre=nombre      # nombre tambien privado
        self.__salario=salario     # salario privado
        self.E_de_empleo=E_de_empleo    #estado de empleado
    
    def __str__(self):  
        estado = "activo" if self.E_de_empleo else "inactivo"         # aqui intente printear todo como cadena con el metodo de str
        return (f"El empleado {self.__nombre} cuyo salario es de {self.__salario},y el estado de del empleado es: {estado}")
    
    #def get_nombre(self): # intente consultar el nombre que es privado con get pero no sirvio
       #return self.__nombre

    def modificar_salario(self,nuevo_salario):
        self.__salario=nuevo_salario
        return print(f"El salario de {self.__nombre} ah sido modificado la cifra a:  {self.__salario}")
    
    def consultar_estado (self):   # aqui es , si estado es false entonces no esta actrivo 
        if self.E_de_empleo == False:
            print (f"El empleado {self.__nombre} , no esta disponible")
        else:
            print(f"El empleado {self.__nombre}, esta disponible para trabajar")

    
#CREAMOS LOS OBJETOS 

empleado1=Empleado("goliaht",3550,False)
empleado2=Empleado("almendra",2333,True)
empleado3=Empleado("leyia",2500,True)

print(empleado1)
print(empleado2)
print(empleado3)


empleado1.modificar_salario(5600)

empleado1.consultar_estado()
empleado2.consultar_estado()
empleado3.consultar_estado()

#con esto se puede ocupar el get para conusltar un dato privado 
#nombre_empleado1 = empleado1.get_nombre()
#print(f"El nombre del empleado 1 es: {nombre_empleado1}")

