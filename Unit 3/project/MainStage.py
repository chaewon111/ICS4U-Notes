import pygame
import random
import sys
from SnakeBattleGame import Game
from snake import Snake

from ChaewonSnakeTemplate import Chaewon


# Screen dimensions
WIDTH, HEIGHT = 800, 600


# Main game loop
def main():
    m,n = Snake.matrix_size()
    snakes = [ ]
    snakes.append(Chaewon)

    game = Game(snakes, 800, m, n)
    game.start()

if __name__ == "__main__":
    main()