#ejrcicio 2 
"""Desarrollar un sistema de gestión de contactos, en el cual se debe crear dos clases,
Contacto y Agenda, para gestionar los contactos de una agenda. El objetivo es permitir al
usuario realizar operaciones básicas como añadir, buscar, editar y listar contactos. Además,
el programa debe finalizar correctamente cuando el usuario lo solicite.

Clase Contacto
La clase debe tener los atributos privados de nombre, teléfono y email.
Métodos de la clase
● Constructor
● Método mágico que retorne una cadena con el nombre, teléfono y email del
contacto.
● Otro método que permite modificar el nombre, teléfono o email de un contacto. Solo
los datos que se proporcionen deben ser modificados.

Clase Agenda
La clase debe tener un atributo que almacene una lista pública de contactos.
Métodos de la clase
● Crear método que permita añadir un nuevo contacto a la agenda.
● Agregar método que muestre todos los contactos en la agenda.
● Un método para buscar un contacto en la agenda por nombre y lo muestra.
● Agregar un método para buscar un contacto por nombre y editar sus datos.
● Por último, crear un método que finalice el programa.
El programa debe mostrar un menú con las siguientes opciones: ● Añadir contactos ● Listar contactos ● Buscar contactos ● Editar contactos ● Cerrar agenda"""
class Contacto():
    def __init__(self,__nombre,__telefono,__email):
        self.__nombre=__nombre
        self.__telefono=__telefono
        self.__email=__email
    def __str__(self):
        return (f"El contacto cuyo nombre es :{self.__nombre}, telefono: {self.__telefono}, Email: {self.__email}")
    def modificar_datos(self,nuevo_nom,nuevo_tel,nuevo_email):
        self.__nombre=nuevo_nom
        self.__telefono=nuevo_tel
        self.__email=nuevo_email
        return (f"datos actualizados{nuevo_nom},telefono{nuevo_tel},Email{nuevo_email}")

class Agenda():

    contactos=[]

    def añadir_contacto(self,contacto):
        self.contactos.append(contacto)
        print(f"Contacto {contacto} añadido a la agenda.")

    def mostrar_contactos(self):
        if len(self.contactos) == 0:
            print("No hay contactos en la agenda.")
        else:
            print("Contactos en la agenda:")
            for contacto in self.contactos:
                print(contacto)
    
    def buscar_contactos(self):
        pass
