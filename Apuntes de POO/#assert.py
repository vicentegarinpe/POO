#assert
condicion=0
assert condicion, "Mensaje de error si la condición es falsa"
class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def retirar(self, cantidad):
        # Asegura que la cantidad a retirar no haga que el saldo sea negativo
        assert cantidad <= self.saldo, "No se puede retirar más de lo que hay en la cuenta."
        self.saldo -= cantidad
def establecer_edad(edad):
    assert edad >= 0, "La edad no puede ser negativa."
class Producto:
    def __init__(self, precio):
        assert precio >= 0, "El precio no puede ser negativo."
        self.precio = precio
class Calculadora:
    def dividir(self, a, b):
        assert b != 0, "No se puede dividir por cero."
        return a / b
#los asertos ayudan a prevenir errores en el código verificando condiciones críticas 
# y asegurando que se cumplan las expectativas
#  evitando así la necesidad de crear soluciones adicionales para manejar esos errores.
