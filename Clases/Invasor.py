# -*- coding: utf-8 -*-
import pygame
from random import randint
import Proyectil

class Invasor(pygame.sprite.Sprite):
    """Clase de los invasores"""
    def __init__(self,posx,posy,distancia):
        pygame.sprite.Sprite.__init__(self)
        self.imagenA = pygame.image.load('imagenes/invader1.png')
        self.imagenB = pygame.image.load('imagenes/invader2.png')
        
        self.imagenes = [self.imagenA,self.imagenB]
        
        self.imagen_invasor = self.imagenes[0]
        self.rect = self.imagen_invasor.get_rect()
        
        self.rangoDisparos = 3
        self.disparos = []
        self.velocidad = 3
        
        self.rect.top = posy
        self.rect.left = posx

        self.conquista = False

        self.derecha = True
        self.contador = 0
        self.max_desenso = self.rect.top + 40

        self.limite_derecha = posx + distancia
        self.limite_izquierda = posx - distancia

    def comportamiento(self,tic):
        if not self.conquista:
            self.__movimientos()
            self.__dispara()
            if tic % 2 == 0:
                self.imagen_invasor = self.imagenes[0]
            else:
                self.imagen_invasor = self.imagenes[1]
    def dibujar(self,superficie):
        superficie.blit(self.imagen_invasor,self.rect)

    def __movimientos(self):
        if self.contador < 3:
            self.movimiento_lateral()
        else:
            self.moviento_vertical()
            
    def movimiento_lateral(self):
        if self.derecha:
            self.rect.left += self.velocidad
            if self.rect.left > self.limite_derecha:
                self.derecha = False
                self.contador += 1
        else:
            self.rect.left -= self.velocidad
            if self.rect.left < self.limite_izquierda:
                self.derecha = True

    def moviento_vertical(self):
        if self.max_desenso == self.rect.top:
            self.contador = 0
            self.max_desenso = self.rect.top + 40
        else:
            self.rect.top += 1
            
    def __dispara(self):
        if (randint(0,200)) < self.rangoDisparos:
            x,y = self.rect.center
            proyectil = Proyectil.Proyectil(x,y,False)
            self.disparos.append(proyectil)

   