import pygame

class Triangulo():

    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.color=(219,148,255)
        self.velocidad=0,5
    

    def movimiento (self):
        if teclas [pygame.K_LEFT]:
            self.x -= self.velocidad 
        if teclas [pygame.K_RIGHT]:
            self.x+= self.velocidad
        if teclas [pygame.K_UP]:
            self.y -= self.velocidad
        if teclas [pygame.K_DOWN]:
            self.y += self.velocidad
        


    

    def dibujar (self):
        puntos=[(self.x,self.y),(self.x-50,self.y+100),(self.x+50,self.y+100)]
        pygame.draw.polygon(ventana,self.color,puntos)