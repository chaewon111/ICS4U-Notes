import pygame
import random
import sys
from RobotMainStage import Game

from MySnakeTemplate import MySnakeTemplate

# Screen dimensions
WIDTH, HEIGHT = 800, 600


# Main game loop
def main():
    snakes = [ ]
    snakes.append(MySnakeTemplate())

    game = Game(snakes, 800)
    game.start()

if __name__ == "__main__":
    main()