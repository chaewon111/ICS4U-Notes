from snake import Snake
import random

'''
To use the Template:
1. Change this file name `MySnakeTemplate.py` to your own/nick name
2. Change this class name `MySnakeTemplate` to your own/nick name
3. Implement the TODO sections
'''
class MySnakeTemplate(Snake):
    def __init__(self):
        # TODO: Construct your snake
        # start_x, start_y should be your assigned starting position.
        # length + attack + hp should be added up to a maximum of 10; otherwise, the snake will be disqualified and removed from the game.
        super().__init__(5, 5, 1, (100,100,100), 'MySnakeTemplate', 1, 1)

    def move(self):
        # TODO: Write your own find next moving direction logic
        direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        direction = random.choice(direction)

        super().move(direction)

    def detect(self):
        # TODO: [OPTIONAL] You can utilize the detect feature called every round
        #                  to store any value that's helpfull for your move() direction logic
        # NOTE: detect() function will onlly allow to have a MAXIMUM runtine of 2 second!
        super().detect() # Do nothing

    def _checkCollision(self):
        # TODO: [OPTIONAL] Write a helper method to check if the snake would collide with the wall
        return None

    def _getPosition(self):
        # TODO: Write a helper method to get the current head position of the snake
        return None


def main():
    '''
    You can write your own testing code here
    '''
    # Initialize the snake
    snake = MySnakeTemplate()
    print(snake)

    # Grow the snake
    snake.grow()
    snake.grow()
    snake.grow()
    snake.grow()
    print(snake)

    snake.move()
    print(snake)

    snake.move()
    print(snake)

    snake.move()
    print(snake)

    snake.move()
    print(snake)

    snake.move()
    print(snake)

    snake.move()
    print(snake)
