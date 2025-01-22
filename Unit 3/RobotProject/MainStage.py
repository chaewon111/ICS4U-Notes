import pygame
import random
import sys
from RobotMainStage import Game

# Screen dimensions
WIDTH, HEIGHT = 800, 600


# Main game loop
def main():
    game = Game(1000, 100, 60)
    game.start()

if __name__ == "__main__":
    main()