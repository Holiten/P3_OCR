"""This script launches the main program"""

import sys
import pygame
from pygame.locals import *

from constants import WINDOW
from classes.maze import Maze
from classes.player import Player
from classes.objects import Objects
from classes.gardian import Gardian
from classes.events import Events

# Pygame init.
pygame.init()

# Set the window
WINDOW = pygame.display.set_mode((WINDOW, WINDOW))

# main loop init.
run = True

# Create object maze
MAZE = Maze("ressources/labyrinth.md")

# Create object player
MACGYVER = Player("ressources/images/MacGyver.png", MAZE)

# Create object gardian
GARDIAN = Gardian("ressources/images/Gardien.png", MAZE)

# Create object items
ETHER = Objects("ressources/images/ether.jpg", MAZE)
SERINGUE = Objects("ressources/images/seringue.png", MAZE)
AIGUILLE = Objects("ressources/images/aiguille.png", MAZE)
TUBE = Objects("ressources/images/tube_plastique.png", MAZE)

# Create object events
GAME_EVENTS = Events()

# main loop
while run:

    # Tracking time
    pygame.time.Clock()

    # create and display maze
    MAZE.create()
    MAZE.display(WINDOW)

# create and display random objects

    # Object N°1
    ETHER.ramdom_loop()
    ETHER.display(WINDOW)

    # Object N°2
    SERINGUE.ramdom_loop()
    SERINGUE.display(WINDOW)

    # Object N°3
    AIGUILLE.ramdom_loop()
    AIGUILLE.display(WINDOW)

    # Object N°4
    TUBE.ramdom_loop()
    TUBE.display(WINDOW)

    # display player
    WINDOW.blit(MACGYVER.sprite, (MACGYVER.pos_x, MACGYVER.pos_y))

    # display guardian
    GARDIAN.display(WINDOW)

    # items count
    GAME_EVENTS.text_item_count(WINDOW)

    # refresh window
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

        elif event.type == KEYDOWN:

            if event.key == K_RIGHT:
                MACGYVER.move("right")
            elif event.key == K_DOWN:
                MACGYVER.move("down")
            elif event.key == K_LEFT:
                MACGYVER.move("left")
            elif event.key == K_UP:
                MACGYVER.move("up")

            player_new_position = MACGYVER.pos_x, MACGYVER.pos_y

            if player_new_position == (ETHER.pos_x_rand, ETHER.pos_y_rand):
                if ETHER.object_state == 1:
                    ETHER.object_state = 0
                    Objects.object_count -= 1

            elif player_new_position == (SERINGUE.pos_x_rand, SERINGUE.pos_y_rand):
                if SERINGUE.object_state == 1:
                    SERINGUE.object_state = 0
                    Objects.object_count -= 1

            elif player_new_position == (AIGUILLE.pos_x_rand, AIGUILLE.pos_y_rand):
                if AIGUILLE.object_state == 1:
                    AIGUILLE.object_state = 0
                    Objects.object_count -= 1

            elif player_new_position == (TUBE.pos_x_rand, TUBE.pos_y_rand):
                if TUBE.object_state == 1:
                    TUBE.object_state = 0
                    Objects.object_count -= 1

            elif player_new_position == (GARDIAN.pos_x, GARDIAN.pos_y):
                if Objects.object_count == 0:
                    GAME_EVENTS.win(WINDOW)
                    print("You win")
                    GARDIAN.state = 0
                    MACGYVER.state = 1
                else:
                    GAME_EVENTS.loose(WINDOW)
                    print("you loose")
                    GARDIAN.state = 1
                    MACGYVER.state = 0
