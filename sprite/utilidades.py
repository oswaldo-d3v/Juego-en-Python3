import pygame

import tools.ficheros as file
import sprite2d.excepciones as e


def cargar_sprite(path, color_transparente=None):
    path = file.convertir_path(path)
    if not file.existe_fichero(path):
        raise e.ErrorPathNoExiste('La ruta %s, no es accesible.' % path)

    sprite = pygame.image.load(path).convert()
    if color_transparente is not None:
        if color_transparente is -1:
            color_transparente = sprite.get_at((0, 0))
        sprite.set_colorkey(color_transparente, pygame.RLEACCEL)

    return sprite
