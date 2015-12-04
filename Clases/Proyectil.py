# -*- coding: utf-8 -*-
import pygame

class Proyectil(pygame.sprite.Sprite):
    """Clase de los proyectiles"""
    def __init__(self,posx,posy,personaje):
        pygame.sprite.Sprite.__init__(self)
        self.imagen = pygame.image.load('imagenes/proyectil.png')
        self.rect = self.imagen.get_rect()
        self.velocidad = 20

        self.rect.top = posy
        self.rect.left = posx

        self.disparoPersonaje = personaje #V -> nave; F -> invasor

    def trayectoria(self):
        if self.disparoPersonaje:
            self.rect.top -= self.velocidad
        else:
            self.rect.top += self.velocidad

    def dibujar(self,superficie):
        superficie.blit(self.imagen,self.rect)