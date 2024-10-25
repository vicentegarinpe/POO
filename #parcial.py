#parcial

class Cliente():
    def __init__(self,nombre):
        self.__nombre=nombre
    def nombre_cliente(self):
        return (f"El cliente {self.__nombre} a accedido al cafe")
    
class Gato:
    def __init__(self,nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
        self.__nivel_energia = 100  
        self.__nivel_hambre = 0 
    def obtener_nombre(self):
        return self.__nombre
    
    def obtener_edad(self):
        return self.__edad

    def obtener_nivel_energia(self):
        return self.__nivel_energia

    def obtener_nivel_hambre(self):
        return self.__nivel_hambre
    
    
    def jugar(self):
        if self.__nivel_energia > 20:
            print(f"EL GATO {self.__nombre} está jugando.")
            self.__nivel_energia -= 20
            self.__nivel_hambre += 10
        else:
            print(f"EL gato{self.__nombre} está demasiado cansado para jugar.")
    
    # Método que alimenta el gato 
    def alimentar(self):
        print(f"Alimentando a {self.__nombre}.")
        self.__nivel_hambre = max(0, self.__nivel_hambre - 30)
        self.__nivel_energia = min(100, self.__nivel_energia + 40)
    
    # Método mágicostr para el estado del gato
    def __str__(self):
        estado_animo = "contento"
        if self.__nivel_energia < 30:
            estado_animo = "cansado"
        if self.__nivel_hambre > 50:
            estado_animo = "hambriento"
        
        return (f"Gato: {self.__nombre}, Edad: {self.__edad}\n"
                f"Energía: {self.__nivel_energia}, Hambre: {self.__nivel_hambre}\n"
                f"Estado general: {estado_animo}")


class Gestion_gatos():
    def __init__(self):
        self.area1=[]
        self.area2=[]
        self.area3=[]
        self.gatos=[]
    
    def agregar_gato(self, gatos):
        self.gatos.append(self.area1)
        return f"Usuario {gatos.__str__()} agregado exitosamente."
    

    def __str__(self):
        return (F"GATOS EN AREA DE JUEGO {self.area1}\n"
                f"GATOS EN EL AREA DE DESCANSO {self.area2}\n"
                f"GATOS EN EL AREA DE COMIDA{self.area3}\n")
    
class Inventario():
    def inventario(self):
        self.churu=[]
    
    def agregar_comida (self,alimento ):
        self.alimento.append(self.churu)
        return f"Usuario {alimento.__str__()} agregado exitosamente al inventario."

# creacion de objetos
cliente1=Cliente("juan perez")
print(Cliente.nombre_cliente(cliente1))

#CREAMOS GATOS
gestion=Gestion_gatos
gato1 = Gato("agustin", 3)
print(gato1)  
gato1.jugar()
print(gato1)  
gato1.alimentar()
print(gato1)  


gato2 = Gato("sloan", 5)
print(gato2)  
gato2.jugar()
print(gato2)  
gato2.alimentar()
print(gato2)  


gato3= Gato("mer", 2)
print(gato3)  
gato3.jugar()
print(gato3)  
gato3.alimentar()
print(gato3) 

gato4= Gato("joe", 9)
print(gato4)  
gato4.jugar()
print(gato4)  
gato4.alimentar()
print(gato4)  

gato5= Gato("benja", 7)
print(gato5)  
gato5.jugar()
print(gato5)  
gato5.alimentar()
print(gato5)  

gato6= Gato("juan", 6)
print(gato6)  
gato6.jugar()
print(gato6)  
gato6.alimentar()
print(gato6)  




# agregar_gatos.




#creacion de inventario      no agrega nada al inventario
#disponibilidad=Inventario
#alimento1=Inventario(1)
#alimento2=Inventario(3)

#disponibilidad.agregar_comida(alimento1)




  
