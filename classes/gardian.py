"""Script to generate the gardian"""

import pygame
from constants import SPRITE_SIZE

class Gardian:
    """Class Gardian to generate the gardian"""
    def __init__(self, sprite, labyrinth):
        self.case_x = 13
        self.case_y = 14
        self.pos_x = self.case_x * SPRITE_SIZE
        self.pos_y = self.case_y * SPRITE_SIZE
        self.sprite = pygame.image.load(sprite).convert()
        self.sprite.set_colorkey((255, 255, 255))
        self.labyrinth = labyrinth
        self.state = 1

    def display(self, window):
        """Function to display gardian"""

        self.window = window

        if self.state == 1:
            self.window.blit(self.sprite, (self.pos_x, self.pos_y))
