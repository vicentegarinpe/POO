#Invariante
#Imagina que tienes una alcancía donde guardas tus ahorros. 
#La regla es que nunca puedes tener menos de cero pesos en tu alcancía.
#  Eso significa que cada vez que quieras sacar dinero, debes asegurarte de que tengas suficiente.
#Si intentas sacar más dinero del que tienes, ¡eso no está permitido! Esta regla de no tener menos de cero pesos es como una invariante.
#Es una regla que siempre debe cumplirse para que tu alcancía funcione bien.
class CuentaBancaria:
    def __init__(self, saldo_inicial):
        assert saldo_inicial >= 0, "El saldo inicial no puede ser negativo."  # Invariante
        self.__saldo = saldo_inicial

    def depositar(self, cantidad):
        assert cantidad > 0, "La cantidad a depositar debe ser positiva."
        self.__saldo += cantidad
        self.__verificar_invariante()

    def retirar(self, cantidad):
        assert cantidad > 0, "La cantidad a retirar debe ser positiva."
        assert cantidad <= self.__saldo, "No se puede retirar más de lo que hay en la cuenta."  # Invariante
        self.__saldo -= cantidad
        self.__verificar_invariante()

    def obtener_saldo(self):
        return self.__saldo

    def __verificar_invariante(self):
        assert self.__saldo >= 0, "Invariante violada: el saldo no puede ser negativo."

# Uso del código
cuenta = CuentaBancaria(100)  # Crear una cuenta con un saldo inicial de 100
print(cuenta.obtener_saldo())   # Imprime: 100
cuenta.depositar(50)            # Deposita 50
print(cuenta.obtener_saldo())   # Imprime: 150
cuenta.retirar(200)             # Esto lanzará un error, ya que el saldo no puede ser negativo
