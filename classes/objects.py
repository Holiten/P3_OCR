"""Scrip to manage the objects"""

import random
import pygame
from constants import SPRITE_SIZE, SPRITE_NUMBER

class Objects:
    """Class to generate object Object"""

    object_count = 0
    object_list = []

    def __init__(self, sprite, labyrinth):
        self.labyrinth = labyrinth
        self.sprite = pygame.image.load(sprite).convert()
        self.case_x_rand = 0
        self.case_y_rand = 0
        self.pos_x_rand = 0
        self.pos_y_rand = 0
        self.loop = True
        self.object_state = 1

        Objects.object_count += 1
        Objects.object_list.append(Objects.object_count)

    def ramdom_loop(self):
        """Function to randomize the position of objects"""

        while self.loop:

            self.case_x_rand = random.randrange(SPRITE_NUMBER)
            self.case_y_rand = random.randrange(SPRITE_NUMBER)
            self.pos_x_rand = self.case_x_rand * SPRITE_SIZE
            self.pos_y_rand = self.case_y_rand * SPRITE_SIZE

            if self.labyrinth.structure[self.case_y_rand][self.case_x_rand] == "g":
                self.loop = False
                self.object_count += 1

            else:
                self.loop = True

    def display(self, window):
        """Function to display the objects"""

        self.window = window

        if self.object_state == 1:
            self.window.blit(self.sprite, (self.pos_x_rand, self.pos_y_rand))
