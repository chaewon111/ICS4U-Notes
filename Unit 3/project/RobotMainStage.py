import sys
import pygame, random
from snake import Snake
from MySnakeTemplate import MySnakeTemplate

class Game:

    # Constants
    GRID_COLOR = (200, 200, 200)  # Light gray
    LINE_COLOR = (200, 200, 200)  # Dark gray
    SCREEN_COLOR = (255, 255, 255)  # White
    FONT_SIZE = 30

    def __init__(self, snakes : list, w : int = 800, m : int = 15, n : int = 10, Caption : str = 'Battle Grid'):
        """Initialize Game object."""
        # Initialize pygame
        pygame.init()

        self.map : list = [[None for _ in range(n)] for _ in range(m)]

        # Player Initializing
        self.snakes : list[Snake] = snakes

        # Screen dimensions
        self.m : int = m
        self.n : int = n
        self.WIDTH : int = w
        self.cell_size : int = w // m
        self.HEIGHT : int = n * self.cell_size

        self.screen : pygame.Surface = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.caption = pygame.display.set_caption(Caption)
        self.font : pygame.font.Font = pygame.font.SysFont(None, Game.FONT_SIZE)

        self.clock = None
        self.running : bool = False

    def _update_map(self):
        for snake in self.snakes:
            color = snake.color
            for body in snake.body_positions:
                x, y, hp = body
                if hp < 1:
                    break
                self.map[x][y] = snake

    def start(self):
        """Start the game."""
        self.clock = pygame.time.Clock()
        self.running = True

        self.update()

    def update(self):
        """Main game loop."""
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.draw_grid()

            # if len(self.snakes) > 0:
            #     self.draw_snake(self.snakes[0])

            # for i in range(len(self.snakes)):
            #     status = self.snakes[i].move()
            #     if not status:
            #         print(f'{self.snakes[i].name} is disqualified or dead!')
            #         self.snakes.pop(i)

            pygame.display.flip()
            self.clock.tick(30)  # Limit to 30 frames per second

        self.exit()

    def exit(self):
        """Exit game."""
        pygame.quit()
        sys.exit()

    # Main loop
    def draw_snake(self, snake : Snake):
        color = snake.color
        for body in snake.body_positions:
            x, y, hp = body
            if hp < 1:
                break
            pygame.draw.rect(self.screen, color, (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))

    def draw_grid(self):
        """Draw the grid on the screen."""
        self.screen.fill(Game.SCREEN_COLOR)
        for row in range(self.n + 1):
            pygame.draw.line(self.screen, Game.LINE_COLOR, (0, row * self.cell_size), (self.WIDTH, row * self.cell_size))
        for col in range(self.m + 1):
            pygame.draw.line(self.screen, Game.LINE_COLOR, (col * self.cell_size, 0), (col * self.cell_size, self.HEIGHT))