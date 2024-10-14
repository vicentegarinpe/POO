#ejercicio propuesto (encapsulamiento y visibilidad)

class Vehiculo:
    def __init__(self,__marca,__modelo,__año,__disponible):
        self.__marca=__marca
        self.__modelo=__modelo
        self.__año=__año
        self.__disponible=__disponible
    def marcar_vendido(self,disponibilidad):
        self.disponibilidad=disponibilidad
        
