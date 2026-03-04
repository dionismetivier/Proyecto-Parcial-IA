import pygame
from constante import *

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        #Carga y Escalado de Imagenes
        Imagen_1 = pygame.image.load("assets/Imagenes/Wraith_01/Wraith_01_Moving Forward_000.png").convert_alpha()
        Imagen_2 =  pygame.image.load("assets/Imagenes/Wraith_01/Wraith_01_Moving Forward_001.png").convert_alpha()

        self.sprites_derecha = [
          pygame.transform.scale(Imagen_1, (120, 120)),
          pygame.transform.scale(Imagen_2, (120, 120))
        ]

        self.sprites_izquierda = [
            pygame.transform.flip(s, True, False) for s in self.sprites_derecha
        ]

        # Estado y Movimiento de Personaje
        self.direccion = "derecha"
        self.actual_sprite = 0.0
        self.image = self.sprites_derecha[0]
        self.rect = self.image.get_rect(topleft=(100, 600))
        self.velocidad_y = 0
        self.animado = False

    def update(self):
        #Captura de teclas presionadas
        Controles = pygame.key.get_pressed()
        self.animado = False

        #Movimientos Horizontales
        if Controles[pygame.K_LEFT]:
            self.rect.x -= 8
            self.animado = True
            self.direccion = "izquierda"
        if Controles[pygame.K_RIGHT]:
            self.rect.x += 8
            self.animado = True
            self.direccion = "derecha"

        #Animacion
        if self.animado:
            self.actual_sprite += 0.1 #Velocidad de Animacion
            if self.actual_sprite >= len(self.sprites_derecha):
                self.actual_sprite = 0

            #Seleccion de Sprites segun la direccion
            if self.direccion == "derecha" :
                self.image = self.sprites_derecha[int(self.actual_sprite)]
            else:
                self.image = self.sprites_izquierda[int(self.actual_sprite)]

        else:
            #Imagen estatica cuando el personaje no se esta moviendo
            if self.direccion == "derecha":
                self.image = self.sprites_derecha[0]
            else:
                self.image = self.sprites_izquierda[0]

        #Salto y gravedad
        if Controles[pygame.K_SPACE] and self.rect.bottom >= 650:
            self.velocidad_y = -20

        self.velocidad_y += 1
        self.rect.y += self.velocidad_y

        #Colision con el suelo para que el personaje no caiga infinitamente
        if self.rect.bottom > 650:
            self.rect.bottom = 650
            self.velocidad_y = 0