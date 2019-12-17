"""This script contains the elements of the class Events"""

import pygame
from classes.objects import Objects
from classes.gardian import Gardian

class Events:
    """Class Events to count and display the events of the maze"""

    def __init__(self):
        self.object_pick = 0
        self.text_font = pygame.font.SysFont("arial", 15)
        self.text = ""


    def text_item_count(self, window):
        """Fonction to count and display the events in the maze"""
        self.object_pick = Objects.object_count

        if self.object_pick == 4:
            text = "You have 4 items to pick up"
            self.text = self.text_font.render(text, True, (255, 255, 10))
            window.blit(self.text, (60, 0))

        elif self.object_pick == 3:
            text = "You have 3 items to pick up"
            self.text = self.text_font.render(text, True, (255, 255, 10))
            window.blit(self.text, (60, 0))

        elif self.object_pick == 2:
            text = "You have 2 items to pick up"
            self.text = self.text_font.render(text, True, (255, 255, 10))
            window.blit(self.text, (60, 0))

        elif self.object_pick == 1:
            text = "You have 1 items to pick up"
            self.text = self.text_font.render(text, True, (255, 255, 10))
            window.blit(self.text, (60, 0))

        elif self.object_pick == 0:
            text = "You can fight the gardian"
            self.text = self.text_font.render(text, True, (255, 255, 10))
            window.blit(self.text, (60, 0))

    def win(self, window):
        """Function to display text if you win"""
        if self.object_pick == 0:
            text = "You win"
            self.text = self.text_font.render(text, True, (255, 255, 10))
            window.blit(self.text, (60, 0))

    def loose(self, window):
        """Function to display text if you loose"""
        if self.object_pick != 0:
            text = "You loose"
            self.text = self.text_font.render(text, True, (255, 255, 10))
            window.blit(self.text, (60, 0))
