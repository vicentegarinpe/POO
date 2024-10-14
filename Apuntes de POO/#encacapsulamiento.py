#encacapsulamiento
#objetos actuen como datos abtractos 
# mecanismo de agrupamiento
##visibilidad publica y privada que son los guines bajos , osea privado solo se puede editar en clase persona no desde otra
#doble guion bajo al principio solamente para que sea privado 

class Test:
    def __uno(self):
        print("este metodo es privado ya que su nombre empieza con dos guones bajo")
    def dos(self):
        print("este metodo es publico")
    def __tres__(self):
        print("este metodo tambien es publico")

test1=Test()
test1.__uno() # no funcionara
test1.dos() #se ejecutaran correctamente por que son publicos
test1.__tres__() #se ejecutaran correctamente por que son publicos



#self.__ asi se veria un atributo privado
