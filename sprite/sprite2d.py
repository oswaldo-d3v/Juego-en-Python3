import pygame

from sprite.excepciones import ErrorSprite
from sprite.utilidades import cargar_sprite


class Sprite2D(pygame.sprite.Sprite):
    def cargar_sprite(self, path):
        if isinstance(path, str):
            return cargar_sprite(path)
        elif isinstance(path, pygame.Surface):
            return path
        else:
            raise ErrorSprite('Imposible crear el sprite en base al objeto')

    def __init__(self, sprite):
        self.sprite(sprite)
        self.ancho, self.alto = self.sprite.get_rect().size
