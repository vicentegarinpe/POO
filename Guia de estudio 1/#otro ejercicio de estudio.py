class Usuario():
    def __init__(self, nombre, edad, peso, altura, t_membresia):
        self.__nombre = nombre
        self.__edad = edad
        self.__peso = peso
        self.__altura = altura
        self.t_membresia = t_membresia

    def __str__(self):
        return f"El nombre del cliente es {self.__nombre} y su edad es {self.__edad}"

    def imc(self):
        imc = self.__peso / self.__altura ** 2
        return imc  # Cambiado para devolver el valor de IMC sin mensaje

    def clasificar_imc(self):
        valor_imc = self.imc()  # Llamar al método imc() para obtener el valor
        if valor_imc < 18.5:
            return f"El IMC de {self.__nombre} indica bajo peso."
        elif 18.5 <= valor_imc < 24.9:
            return f"El IMC de {self.__nombre} indica peso normal."
        elif 25 <= valor_imc < 29.9:
            return f"El IMC de {self.__nombre} indica sobrepeso."
        else:
            return f"El IMC de {self.__nombre} indica obesidad."

    def tipo_membresia(self):
        if self.t_membresia <= 7:
            return f"La membresía de {self.__nombre} es de una semana (Estándar)."
        elif self.t_membresia <= 14:
            return f"La membresía de {self.__nombre} es de dos semanas (Normal)."
        elif self.t_membresia == 30:
            return f"La membresía de {self.__nombre} es de un mes (VIP)."
        else:
            return f"La membresía de {self.__nombre} tiene un tiempo no reconocido."

class PlanEntrenamiento():
    def __init__(self, usuario, ejercicios, duracion, frecuencia, objetivos):
        self.usuario = usuario
        self.ejercicios = ejercicios  # Lista de ejercicios
        self.duracion = duracion  # Duración en minutos
        self.frecuencia = frecuencia  # Frecuencia semanal
        self.objetivos = objetivos  # Objetivos del entrenamiento

    def mostrar_plan(self):
        return (f"Plan de entrenamiento para {self.usuario.__str__()}:\n"
                f"Ejercicios: {', '.join(self.ejercicios)}\n"
                f"Duración: {self.duracion} minutos\n"
                f"Frecuencia: {self.frecuencia} veces por semana\n"
                f"Objetivos: {self.objetivos}")

class Gimnasio():
    def __init__(self):
        self.usuarios = []  # Lista para almacenar usuarios

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)
        return f"Usuario {usuario.__str__()} agregado exitosamente."

    def mostrar_usuarios(self):
        return [usuario.__str__() for usuario in self.usuarios]

    def obtener_informe_usuario(self, usuario):
        return (f"{usuario.__str__()}\n"
                f"{usuario.clasificar_imc()}\n"
                f"{usuario.tipo_membresia()}")   

# Ejemplo de uso
gimnasio = Gimnasio()

# Crear usuarios
usuario1 = Usuario("Juan", 25, 70, 1.75, 14)
usuario2 = Usuario("María", 30, 80, 1.65, 30)

# Agregar usuarios al gimnasio
print(gimnasio.agregar_usuario(usuario1))
print(gimnasio.agregar_usuario(usuario2))

# Mostrar todos los usuarios
print(gimnasio.mostrar_usuarios())

# Crear un plan de entrenamiento para Juan
plan_juan = PlanEntrenamiento(usuario1, ["Correr", "Levantamiento de pesas"], 60, 3, "Aumentar masa muscular")
print(plan_juan.mostrar_plan())

# Obtener informe del usuario Juan
print(gimnasio.obtener_informe_usuario(usuario1))

print(Usuario.tipo_membresia(usuario2))
