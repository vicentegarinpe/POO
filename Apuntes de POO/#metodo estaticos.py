#metodo estaticos 
class Finanzas:
    @staticmethod
    def calcular_iva(precio, tasa_iva):
        return precio * (1 + tasa_iva)
class Validacion:
    @staticmethod
    def es_email_valido(email):
        return "@" in email and "." in email.split("@")[-1]
class Conversor:
    @staticmethod
    def celsius_a_fahrenheit(celsius):
        return (celsius * 9/5) + 32
class Estadisticas:
    @staticmethod
    def calcular_promedio(notas):
        return sum(notas) / len(notas) if notas else 0
import uuid

class GeneradorID:
    @staticmethod
    def generar_id_unico():
        return str(uuid.uuid4())
