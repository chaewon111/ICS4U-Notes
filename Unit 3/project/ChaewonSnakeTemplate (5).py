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
        atk = 190
        hp = 9

        self.target_snake=None
        self.target_position=None
        self.next_move=(0,0)

        #TODO: I add the following two fields' initialization
        self.map = [[[None] for _ in range(self.MATRIX_SIZE[0])] for _ in range(self.MATRIX_SIZE[1]) ]
        self.snakes_alive = []
        
        super().__init__(x, y, color, name, length, atk, hp)


    def move(self) -> None:
       
        headx, heady, hp = self._getPosition()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        safe_directions = []
        extraoptions=[]
        enemy_detected = False
        best_direction = None

        # TODO: try
        try:
            for dx, dy in directions:   
                new_x, new_y = headx + dx, heady + dy

        
                if 0 < new_y < len(self.map) and 0 < new_x < len(self.map[0]):
                    other = self.map[new_y][new_x]
                    # 뉴엑스뉴와이에잇는거 정보 받아옴. 논일수도, 뱀일 수도
                else:
                    other = None


                # collision(몸,벽)
                collision = self._checkCollision(new_x, new_y)
                enemy_there = False

                if isinstance(other, Snake) and other is not self:
                    enemy_there=True
                    enemy_head = other.body_positions[0][:2]
                    if (new_x, new_y) != enemy_head and not collision:
                        # 적 body
                        extraoptions.append([dx, dy])


                if not collision and not enemy_there :
                    safe_directions.append([dx, dy])

                # 적 발견 시 정보 저장
                if enemy_there:
                    enemy_detected = True
                    self.enemy_hp = other.hp
                    self.enemy_attack = other.attack
                    self.enemy_head_hp = other.body_positions[0][2]  # 적 머리 HP
                    self.enemy_position = (new_x, new_y)

            # 회피 모드 (적 2명 이상 남아 있음)
            if len(self.snakes_alive) >= 2:
                best_direction = random.choice(safe_directions) if safe_directions else random.choice(extraoptions)



            else:  # 공격 모드 (1v1 상황)

                if enemy_detected:
                    
                    if self.attack >= self.enemy_head_hp or self.body_positions[0][2] > self.enemy_attack:
                        best_direction = self._chaseEnemy(headx, heady, self.enemy_position[0])

                    else:
                        best_direction = random.choice(safe_directions) if safe_directions else random.choice(extraoptions)
                else:
                    best_direction = random.choice(safe_directions) if safe_directions else random.choice(extraoptions)

            return super().move(best_direction)
        except Exception as e:
            print(e) # print out the error
        
        # TODO: If any Error, just move left
        return super().move([-1,0])
    



    def detect(self, map: list[list[list]]) -> None:
        
        self.map = map  # 무브 실행 전에 얘 먼저 저장
        self.snakes_alive = [
            cell
            for row in map
            for cell in row
            if isinstance(cell, Snake) and cell is not self]
        
        super().detect(map)


    def _checkCollision(self, x: int, y: int) -> bool:
     
        if x < 0 or x >= len(self.map[0]) or y < 0 or y >= len(self.map):
            return True  # 벽
        if (x, y) in self.body_positions:
            return True  # 자기 몸 
        return False
    


    def _getPosition(self) -> tuple[int, int]:
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
    
    # Initialize the snake
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