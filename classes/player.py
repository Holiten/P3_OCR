"""Script to manage the player"""

import pygame
from constants import SPRITE_SIZE, SPRITE_NUMBER

class Player:
    """Class to generate object Player"""

    def __init__(self, sprite, labyrinth):
        self.sprite = pygame.image.load(sprite).convert()
        self.sprite.set_colorkey((255, 255, 255))
        self.case_x = 1
        self.case_y = 0
        self.pos_x = 20
        self.pos_y = 0
        self.labyrinth = labyrinth
        self.state = 1

    def move(self, direction):
        """Function to move the player up, down, left, right"""

        if direction == "right":
            if self.case_x < (SPRITE_NUMBER - 1):
                if self.labyrinth.structure[self.case_y][self.case_x + 1] != "w":
                    self.case_x += 1
                    self.pos_x = self.case_x * SPRITE_SIZE

        elif direction == "left":
            if self.case_x > 0:
                if self.labyrinth.structure[self.case_y][self.case_x - 1] != "w":
                    self.case_x -= 1
                    self.pos_x = self.case_x * SPRITE_SIZE

        elif direction == "up":
            if self.case_y > 0:
                if self.labyrinth.structure[self.case_y - 1][self.case_x] != "w":
                    self.case_y -= 1
                    self.pos_y = self.case_y * SPRITE_SIZE

        elif direction == "down":
            if self.case_y < (SPRITE_NUMBER - 1):
                if self.labyrinth.structure[self.case_y + 1][self.case_x] != "w":
                    self.case_y += 1
                    self.pos_y = self.case_y * SPRITE_SIZE
