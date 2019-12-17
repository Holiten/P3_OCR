import pygame
from constants import SPRITE_SIZE

class SpriteSheet:

    def __init__(self, fichier):
        self.file = pygame.image.load(fichier)

    def cut_sprite(self, pos_x, pos_y, sprite_height, sprite_width):
        self.sprite_width = SPRITE_SIZE
        self.sprite_height = SPRITE_SIZE

        sprite_sheet = pygame.Surface([sprite_height, sprite_width]).convert()
        sprite_sheet.blit(self.file, (0, 0), (pos_x, pos_y, sprite_height, sprite_width))
        return sprite_sheet