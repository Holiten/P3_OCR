"""Script to manage the maze"""

from constants import SPRITE_SIZE
from classes.sprites_sheet import SpriteSheet

class Maze:
    """Class to generate object Maze"""
    def __init__(self, file):
        self.file = file
        self.structure = 0
        self.object_list = []

    def create(self):
        """Fonction to create the maze object"""
        with open(self.file, "r") as file:
            structure_level = []
            for line in file:
                line_level = []
                for sprite in line:
                    if sprite != "\n":
                        line_level.append(sprite)
                structure_level.append(line_level)
                self.structure = structure_level
            return structure_level

    def display(self, window):
        """Fonction to diplay the maze"""
        sprite_sheet = SpriteSheet("ressources/images/floor-tiles.png")
        wall = sprite_sheet.cut_sprite(20, 0, SPRITE_SIZE, SPRITE_SIZE)
        start = sprite_sheet.cut_sprite(160, 20, SPRITE_SIZE, SPRITE_SIZE)
        arrival = sprite_sheet.cut_sprite(220, 20, SPRITE_SIZE, SPRITE_SIZE)
        ground = sprite_sheet.cut_sprite(360, 200, SPRITE_SIZE, SPRITE_SIZE)

        num_line = 0
        for line in self.structure:
            num_square = 0
            for sprite in line:
                pos_x = num_square * SPRITE_SIZE
                pos_y = num_line * SPRITE_SIZE
                if sprite == "w":
                    window.blit(wall, (pos_x, pos_y))
                elif sprite == "s":
                    window.blit(start, (pos_x, pos_y))
                elif sprite == "a":
                    window.blit(arrival, (pos_x, pos_y))
                elif sprite == "g":
                    window.blit(ground, (pos_x, pos_y))
                num_square += 1
            num_line += 1
