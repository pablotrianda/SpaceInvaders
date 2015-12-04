# -*- coding: utf-8 -*-
import pygame
import Proyectil

class NaveSpacial(pygame.sprite.Sprite):
    """ Clase de la nave"""
    
    def __init__(self,ancho,alto):
        pygame.sprite.Sprite.__init__(self)
        self.imagen = pygame.image.load('imagenes/nave.png')
        self.imagen_explo = pygame.image.load('imagenes/explo_nave.png')
        
        self.rect = self.imagen.get_rect()
        self.rect.centerx = ancho / 2
        self.rect.centery = alto - 30
        
        self.disparos = []
        self.vida = True

        self.sonido_disparo = pygame.mixer.Sound('Sonidos/shoot.wav')
        self.sonido_explosion = pygame.mixer.Sound('Sonidos/explosion.wav')
    def movimiento(self,coordenadas):
        if self.vida:
            if coordenadas[0] < 820:
                self.rect.left = coordenadas[0]

    def disparar(self,x,y):
        if self.vida:
            proyectil = Proyectil.Proyectil(x,y,True)
            self.disparos.append(proyectil)
            self.sonido_disparo.play()

    def dibujar(self,superficie):
        superficie.blit(self.imagen,self.rect)

    def destruida(self):
        self.vida = False
        self.sonido_explosion.play()
        self.imagen = self.imagen_explo
        self.velocidad = 0
        