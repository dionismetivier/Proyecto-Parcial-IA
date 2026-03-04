import pygame
import sys
from constante import *
from Entidades import Jugador

class Kanzo_Adventures:
    def __init__(self):

        #Arranque de Pygame y Ventana de visualizacion
        pygame.init()
        self.PANTALLA = pygame.display.set_mode((ANCHO_PANTALLA, LARGO_PANTALLA))

        #Carga de Escenario
        self.Fondo = pygame.image.load("assets/Imagenes/Mapa.png").convert()
        self.Fondo = pygame.transform.scale(self.Fondo, (ANCHO_PANTALLA, LARGO_PANTALLA))
        pygame.display.set_caption("The Kanzo Adventures")

        #Ajustes de Objetos
        self.clock = pygame.time.Clock()
        self.Jugador = Jugador()
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.Jugador)

    def run(self):
        #Ciclo Principal del juego
       while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #Actualizacion
        self.sprites.update()

        #Dibujo
        self.PANTALLA.blit(self.Fondo, (0, 0))
        self.sprites.draw(self.PANTALLA)

        #Actualizar, visualizar y controlar FPS
        pygame.display.flip()
        self.clock.tick(FPS)

#Base de entrada del Juego
if __name__ == "__main__":
    juego = Kanzo_Adventures()
    juego.run()