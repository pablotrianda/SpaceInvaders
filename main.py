import pygame, sys
from pygame.locals import *
from random import randint
import Clases.Nave
import Clases.Invasor

ancho,alto = 900,480
listaEnemigos = []

def detener_todo():
    for enemigo in listaEnemigos:
        for disparo in enemigo.disparos:
            enemigo.disparos.remove(disparo)

        enemigo.conquista = True
def cargar_Enemigos():
    posx = 100
    for i in range(0,4):
        enemigo = Clases.Invasor.Invasor(posx,100,60)
        listaEnemigos.append(enemigo)
        posx += 200
    posx = 100
    for i in range(0,4):
        enemigo = Clases.Invasor.Invasor(posx,0,40)
        listaEnemigos.append(enemigo)
        posx += 200
           
def SpaceInvader():
    """Clase principal """
    pygame.init() #para uso del paquete
    ventana = pygame.display.set_mode((ancho,alto))  #dimension de la ventana
    pygame.display.set_caption("Space Invaders") #titulo

    jugador = Clases.Nave.NaveSpacial(ancho,alto)
    cargar_Enemigos()
    enJuego = True
    reloj = pygame.time.Clock()

    fuente = pygame.font.SysFont('Arial',50)
    texto = fuente.render("GAME OVER",0,(120,100,40))
    texto2 = fuente.render("WIN!",0,(120,100,40))
    
    pygame.mixer.music.load('Sonidos/fondo.mp3')
    pygame.mixer.music.play(3)
    
    while True: #Evento infinito hasta que salga
        reloj.tick(60) #fps
        timer = pygame.time.get_ticks() /1000
        pygame.mouse.set_visible(False)
        ventana.fill((0,0,0))
        if listaEnemigos == []:
            pygame.mixer.music.fadeout(1000)
            ventana.blit(texto2,(500,200))
            
        for evento in pygame.event.get():  #Si el usuario quiere salir de la venta
            if evento.type == QUIT:
                pygame.quit()  # Detiene los modulos
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                x,y = jugador.rect.center
                jugador.disparar(x,y)
        if enJuego:
            jugador.movimiento(pygame.mouse.get_pos())

        jugador.dibujar(ventana)
        if len(jugador.disparos) > 0:
            for x in jugador.disparos:
                x.dibujar(ventana)
                x.trayectoria()
                if x.rect.top < 100:
                    jugador.disparos.remove(x)
                else:
                    for enemigo in listaEnemigos:
                        if x.rect.colliderect(enemigo.rect):
                            listaEnemigos.remove(enemigo)
                            jugador.disparos.remove(x)
                            
                            
        if len(listaEnemigos) > 0:
            for enemigo in listaEnemigos:     
                enemigo.comportamiento(timer)
                enemigo.dibujar(ventana)

                if enemigo.rect.colliderect(jugador.rect):
                    # Un ememigo coliciona con el jugador
                    jugador.destruida()
                    detener_todo()
                    enJuego = False
                
                if len(enemigo.disparos) > 0:
                    for x in enemigo.disparos:
                        x.dibujar(ventana)
                        x.trayectoria()
                        if x.rect.colliderect(jugador.rect):
                            # Un disparo choca con el jugador
                            jugador.destruida()
                            detener_todo()
                            enJuego = False
                        if x.rect.top < 100:
                            enemigo.disparos.remove(x)
                        else:
                            for disparo in jugador.disparos:
                                if x.rect.colliderect(disparo.rect):
                                    jugador.disparos.remove(disparo)
                                    enemigo.disparos.remove(x)

        if not enJuego:
            pygame.mixer.music.fadeout(1000)
            ventana.blit(texto,(300,200))
        
        enemigo.dibujar(ventana)
        pygame.display.update() #Actualiza la ventana


SpaceInvader()
