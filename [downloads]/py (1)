from snake import Snake
import random

'''
To use the Template:
1. Change this file name `MySnakeTemplate.py` to your own/nick name
2. Change this class name `MySnakeTemplate` to your own/nick name
3. Implement the TODO sections
'''
class Chaewon(Snake):
    def __init__(self):
        # TODO: Construct your snake
        # start_x, start_y should be your assigned starting position.
        # length + attack + hp should be added up to a maximum of 10; otherwise, the snake will be disqualified and removed from the game.
        x, y = (int(self.MATRIX_SIZE[0] *0.4),int(self.MATRIX_SIZE[1] *0.8))
        color = (200,200,200)
        name = __name__
        length = 1
        atk = 92
        hp = 107

        self.target_snake=None
        self.target_position=None
        self.next_move=(0,0)

        #TODO: I add the following two fields' initialization
        self.map = [[[None] for _ in range(self.MATRIX_SIZE[0])] for _ in range(self.MATRIX_SIZE[1]) ]
        self.snakes_alive = []
        self.enemy_position = None
        self.enemy_head_hp = None

        super().__init__(x, y, color, name, length, atk, hp)


    def move(self) -> None:

        headx, heady, hp = self._getPosition()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        safe_directions = []
        extraoptions=[]
        best_direction = None
        self.enemy_position = None 

        try:
            for dx, dy in directions:
                new_x, new_y = headx + dx, heady + dy

                if 0 <= new_y < len(self.map) and 0 <= new_x < len(self.map[0]):
                    other = self.map[new_y][new_x]
                else:
                    other = None

                collision = self._checkCollision(new_x, new_y)
                enemy_there = False

                if other and isinstance(other, list):
                    
                    extraoptions.append([dx, dy])  

                    if not self.target_position or len(other) == 1:
                        self.enemy_position = (new_x, new_y)
                        self.enemy_head_hp = max(other)

                if not collision and not (other and isinstance(other, list)):
                    safe_directions.append([dx, dy])

            if len(self.snakes_alive) >= 2:
                best_direction = random.choice(safe_directions) if safe_directions else random.choice(extraoptions)

            else:
               
                if self.enemy_position:
                    best_direction = self._chaseEnemy(headx, heady, self.enemy_position)
                else:
                    best_direction = random.choice(safe_directions) if safe_directions else random.choice(extraoptions)

            return super().move(best_direction)

        except Exception as e:
            print(e)

        return super().move([-1,0])


    def detect(self, map: list[list[list]]) -> None:
        self.map = map  # 무브 실행 전에 얘 먼저 저장
        self.snakes_alive = [cell for row in map for cell in row if isinstance(cell, list)]
        super().detect(map)


    def _checkCollision(self, x: int, y: int) -> bool:
        if x < 0 or x >= len(self.map[0]) or y < 0 or y >= len(self.map):
            return True  # 벽
        if (x, y) in self.body_positions:
            return True  # 자기 몸
        return False


    def _getPosition(self) -> tuple[int, int, int]:
        return self.body_positions[0]


    def _chaseEnemy(self, my_x: int, my_y: int, enemy_pos: tuple[int, int]) -> list[int]:
        try:
            target_x, target_y = enemy_pos
            dx = 1 if my_x < target_x else -1 if my_x > target_x else 0
            dy = 1 if my_y < target_y else -1 if my_y > target_y else 0

            if dx != 0 and not self._checkCollision(my_x + dx, my_y):
                return [dx, 0]
            if dy != 0 and not self._checkCollision(my_x, my_y + dy):
                return [0, dy]

            return [1, 0]  # 갈 수 없으면 기본 방향
        except Exception as e:
            print("CHASE: ", e)
        finally:
            return [1,0]


def main():

    #You can write your own testing code here

    snake = Chaewon()
    print(snake)
    print("Initialized")

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