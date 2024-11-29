##lab

class Cliente():
    descuento_estudiante=0.2     #1 definicion de descuentos 
    descuento_academico=0.1  #1 b declare los descunetos como variable de instancia para mas clardad del sistema ademas que es un descuneto que no cambiara osea que sea constante
    
    def __init__(self,nombre_cliente,tipo_cliente,precio_compra) :        
        self.__nombre_cliente=nombre_cliente
        self.__tipo_cliente=tipo_cliente
        self.__precio_compra=precio_compra    

        assert precio_compra <= 0 , " El valor de la compra no puede ser negativa" #
                        
        #1 A los datos que deberia guardar del cliente soon nombre ,tipo de cliente,el precio de su compra
        #1 A los atributos puestos en el constructor deberan ser todos privados para guaradar la privacidad del comprador y del vendedor

        #2A lo mejor seria organizar en un diccionario privado ya que es una forma de mejor organizacion a una lista 
        #2b no exponer los desceuntos directamente para no perder la privacidad de los precios , para despues calcularlos mas adelante y ya
    
    def descuento (self):
        self.__descuento={
            "estudiante",self.descuento_estudiante,
            "academico",self.descuento_academico
        } 
    @staticmethod
    def aplicar_descuento (self):
        if self.__tipo_cliente =="estudiante": 
            Precio_Final=self.precio_compra*self.descuento_academico/100
        
    
    def set_PrecioCompra(self, precio):  # 1A ocupamos setter para confirmar que los precios no sean negativos 
        if precio <= 0:
            assert precio <= 0 ,("El precio no puede ser negativo")
        self.__precio_compra = precio    
    
    def get_PrecioFinal(self): # el getter es util en este caso para no mosrtar el calcul entero de el precio final 
        return (f"El precio final de su compra con descuento es: $CLP {self.Precio_Final}") 
    

        

    


#instanciamos 

cliente=Cliente("elizabeth","estudiante",3500)

print( cliente.get_PrecioFinal)
print()

