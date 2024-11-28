"""Implementar un sistema básico para gestionar personajes de un
videojuego utilizando programación orientada a objetos.
Cada personaje tendrá un nombre, nivel de vida y puntos de ataque. La
idea es que los personajes puedan interactuar entre ellos, permitiendo
que un personaje ataque a otro, lo que disminuirá su vida. Además,
deberás verificar si un personaje está vivo o no.
Requerimientos:
1. Clase Personaje:
○ Atributos: el nombre del personaje, el nivel de vida del personaje y los
puntos de ataque del personaje.
○ Métodos: un método que permita que el personaje ataque a otro,
disminuyendo la vida del otro personaje según los puntos de ataque del
atacante. Un segundo método, que verifique si el personaje sigue vivo. Debe
devolver True si el nivel de vida es mayor a 0, y False si no. Por último
implementar un método mágico que permita devolver un string que muestre
el estado del personaje (nombre, vida, y ataque).
Instrucciones:
1. Implementar la clase Personaje con los atributos y métodos descritos
anteriormente.
2. Crear al menos dos personajes. Cada personaje debe tener un nombre, vida inicial y
puntos de ataque.
3. Simula un combate entre los personajes haciendo que uno ataque al otro. Después
de cada ataque, se debe mostrar el estado de ambos personajes.
4. Repetir los ataques hasta que uno de los personajes quede sin vida. Utiliza un
método para verificar si el personaje sigue en pie."""
#ej1

class Personaje:
    def __init__(self, nombre, vida, ataque):  #creamos los atributos con cuales manejaremos los personajes
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque

    def atacar(self, otro):     #metodo atacar para que si esta vivo el personaje entonces el atque le restara vida
        if self.esta_vivo():
            print(f"{self.nombre} ataca a {otro.nombre} y causa {self.ataque} puntos de daño.")
            otro.vida -= self.ataque
            if otro.vida < 0:
                otro.vida = 0  # qurEno sea negativa 
        else:
            print(f"{self.nombre} no puede atacar porque está muerto.")

    def esta_vivo(self): #metodo solamente para ver si esta vivo o muerto el personaje si vida es menor a cero entonces murio
        return self.vida > 0

    def __str__(self):   #metodo magico cadena de que devuelve una cadena de texto
        estado = "vivo" if self.esta_vivo() else "muerto"
        return f"Personaje: {self.nombre}, Vida: {self.vida}, Ataque: {self.ataque} ({estado})"

# Creacion de los objetos en este caso dos personajes
personaje1 = Personaje("juan", 1000, 200)
personaje2 = Personaje("juana", 800, 300)

# Simular un combate
while personaje1.esta_vivo() and personaje2.esta_vivo():
    personaje1.atacar(personaje2)
    print(personaje1)
    print(personaje2)
    
    if personaje2.esta_vivo():
        personaje2.atacar(personaje1)
        print(personaje1)
        print(personaje2)

# Resultado final del combate
print("Combate finalizado.")
print(personaje1)
print(personaje2)