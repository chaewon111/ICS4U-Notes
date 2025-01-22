import pygame, random

import sys



class Game:

    # Constants
    GRID_COLOR = (200, 200, 200)  # Light gray
    LINE_COLOR = (200, 200, 200)  # Dark gray
    SCREEN_COLOR = (255, 255, 255)  # White
    FONT_SIZE = 30

    def __init__(self, w=800, m=15, n=10, Caption='Battle Grid'):
        # Initialize pygame
        pygame.init()

        self.map = [[None for _ in range(m)] for _ in range(n)]

        # Screen dimensions
        self.m = m
        self.n = n
        self.WIDTH = w
        self.cell_size = w / m
        self.HEIGHT = n * self.cell_size

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.caption = pygame.display.set_caption(Caption)
        self.font = pygame.font.SysFont(None, Game.FONT_SIZE)

        self.clock = None
        self.running = False

    def start(self):
        """Main game loop."""
        self.clock = pygame.time.Clock()
        self.running = True

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.draw_grid()
            pygame.display.flip()
            self.clock.tick(30)  # Limit to 30 frames per second

        pygame.quit()
        sys.exit()

    # Main loop
    def draw_grid(self):
        """Draw the grid on the screen."""
        self.screen.fill(Game.SCREEN_COLOR)
        for row in range(self.n + 1):
            pygame.draw.line(self.screen, Game.LINE_COLOR, (0, row * self.cell_size), (self.WIDTH, row * self.cell_size))
        for col in range(self.m + 1):
            pygame.draw.line(self.screen, Game.LINE_COLOR, (col * self.cell_size, 0), (col * self.cell_size, self.HEIGHT))