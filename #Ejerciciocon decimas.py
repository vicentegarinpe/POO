class Cafeteria:
    # Variable de clase para la tasa de descuento fijo
    tasa_descuento = 0.10  # 10%

    def __init__(self, nombre):
       
        self.__nombre = nombre
        self.__menu = {}
        self.__pedidos = []

    # Método para verificar si un producto ya está en el menú usando el mientras
    def existe_en_menu(self, producto):
        # Convertimos las claves del diccionario en una lista para usar un índice
        keys = list(self.__menu.keys())
        i = 0
        while i < len(keys):
            if keys[i] == producto:
                return True
            i += 1
        return False

    # Método para agregar un producto al menú, garantizando que el precio sea positivo
    def agregar_producto_menu(self, producto, precio):
        assert precio > 0, "El precio debe ser mayor a cero."
        if self.existe_en_menu(producto) is False:
            self.__menu[producto] = precio
            print(f"Producto '{producto}' agregado al menú con precio {precio}.")
        else:
            print(f"El producto '{producto}' ya está en el menú.")

    # Método para tomar pedido de un producto, asegurando que solo productos en el menú se agreguen
    def pedir_producto(self, producto):
        assert self.existe_en_menu(producto), f"El producto '{producto}' no está en el menú."
        self.__pedidos.append(producto)
        print(f"Producto '{producto}' agregado al pedido.")

    # Método para calcular el total del pedido, con descuento si el cliente es frecuente
    def calcular_total_pedido(self, frecuente=False):
        total = sum(self.__menu[producto] for producto in self.__pedidos)
        if frecuente:
            total -= total * Cafeteria.tasa_descuento
        return total

    # Método estático para actualizar la tasa de descuento
    @staticmethod
    def actualizar_descuento(nueva_tasa):
        assert 0 <= nueva_tasa <= 1, "La tasa de descuento debe estar entre 0 y 1."
        Cafeteria.tasa_descuento = nueva_tasa
        print(f"Tasa de descuento actualizada a {nueva_tasa * 100}%.")

# Ejemplo de uso de la clase
cafeteria = Cafeteria("Café Bonito")

# Agregar productos al menú con validación de precio positivo
cafeteria.agregar_producto_menu("Café", 1500)
cafeteria.agregar_producto_menu("Té", 1000)
cafeteria.agregar_producto_menu("Torta", 2500)

# Pedir productos asegurando que estén en el menú
cafeteria.pedir_producto("Café")
cafeteria.pedir_producto("Té")

# Calcular total sin descuento
print("Total sin descuento:", cafeteria.calcular_total_pedido())

# Calcular total con descuento para cliente frecuente
print("Total con descuento (cliente frecuente):", cafeteria.calcular_total_pedido(frecuente=True))

# Actualizar la tasa de descuento
Cafeteria.actualizar_descuento(0.15)
