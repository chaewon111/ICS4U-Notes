from typing import final

class Snake:

    ATTRIBUTE_RESTRICTION = 5
    MATRIX_SIZE = (10, 10)

    @staticmethod
    def matrix_size():
        """
        Return the map size as a tuple (m, n).
        """
        return Snake.MATRIX_SIZE

    def __init__(self, start_x, start_y, length, color, name, attack, hp):
        """
        Initialize the Snake object.

        :param start_x: Starting x-coordinate in grid units.
        :param start_y: Starting y-coordinate in grid units.
        :param length: Initial Length of the snake.
        :param color: The color of the snake (can be used for visualization later).
        :param name: The name of the snake (can be used for visualization later).
        """
        if length + attack + hp > Snake.ATTRIBUTE_RESTRICTION:
            self.body_positions = [(None, None, None)]
        else:
            self.body_positions = [(start_x, start_y, hp)]
        self.length = length
        self.color = color
        self.name = name
        self.attack = attack
        self.hp = hp

    @property
    def qualification(self):
        """
        Check if the snake is qualified to play the game.

        :return: True if the snake is qualified, False otherwise.
        """
        return self.body_positions[0] != (None, None, None)

    @final # We'll fire you if you override this method.
    def move(self, direction):
        """
        Move the snake in a specified direction. return False if the snake is disqualified or dead.

        :param direction: Tuple (dx, dy) indicating the direction (e.g., (1, 0) for right).
        """
        if not self.qualification or self.checkDead():
            return False

        head_x, head_y, hp = self.body_positions[0]
        new_head = (head_x + direction[0], head_y + direction[1], hp)

        # Insert the new head and remove the last segment if the length remains the same
        self.body_positions = [new_head] + self.body_positions[:self.length - 1]

        if self.check_collision():
            self.length -= 1
            del self.body_positions[0]

        return True



    @final # We'll fire you if you override this method.
    def grow(self):
        """
        Increase the length of the snake by 1.
        """
        self.length += 1
        # No need to modify body_positions as the tail will naturally grow with subsequent moves

    @final # We'll fire you if you override this method.
    def checkDead(self):
        """
        Check if the snake is dead.
        """
        return self.length < 1

    @final # We'll fire you if you override this method.
    def check_collision(self):
        """
        Check for collisions with the boundaries or itself.

        :return: True if a collision is detected, False otherwise.
        """
        head = self.body_positions[0]
        # Check for boundary collision
        if not (0 <= head[0] < Snake.MATRIX_SIZE[1] and 0 <= head[1] < Snake.MATRIX_SIZE[0]):
            return True
        # Check for self-collision
        if head in self.body_positions[1:]:
            return True
        return False

    @final # We'll fire you if you override this method.
    def __str__(self):
        """
        ToString() of the snake.
        """
        return self.__repr__()

    @final # We'll fire you if you override this method.
    def __repr__(self):
        """
        String representation of the snake for debugging.
        """
        return f"Snake(length={self.length}, body_positions={self.body_positions})"


class MySnake(Snake):
    def __init__(self):
        # TODO: Construct your snake
        # start_x, start_y should be your assigned starting position.
        # length + attack + hp should be added up to a maximum of 10; otherwise, the snake will be disqualified and removed from the game.
        super().__init__(10, 10, 1, 'red', 'Hi', 1, 1)

    def move(self,direction):
        # TODO: Write your own find next moving direction logic
        # direction = [1, 0]
        super().move(direction)

    @property
    def _getPosition(self):
        # TODO: Write a helper method to get the current head position of the snake
        return None

# Initialize the snake
snake = MySnake()

# Grow the snake
snake.grow()
snake.grow()
snake.grow()
snake.grow()
print(snake)

snake.move([1, 0])
print(snake)

snake.move([0, 1])
print(snake)

snake.move([-1, 0])
print(snake)

snake.move([0, -1])
print(snake)

snake.move([0, -1])
print(snake)
