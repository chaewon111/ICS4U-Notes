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
        x, y = (120,0)
        color = (200,200,200)
        name = __name__
        length = 7
        atk = 40
        hp = 153

        self.target_snake=None
        self.target_position=None
        self.next_move=(0,0)
        
        super().__init__(x, y, color, name, length, atk, hp)

    import random


    def move(self) -> None:
       
        head_x, head_y = self._getPosition()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        safe_directions = []
        extraoptions=[]
        enemy_detected = False
        best_direction = None


        # 현재 맵 상태 확인 (적 탐색)
        for dx, dy in directions:
            new_x, new_y = head_x + dx, head_y + dy

            # 맵 경계 안이면 셀 정보 확인
            if 0 < new_y < len(self.map) and 0 < new_x < len(self.map[0]):
                other = self.map[new_y][new_x]
                # 뉴엑스뉴와이에잇는거 정보 받아옴. 논일수도, 뱀일 수도
            else:
                other = None


            # collision(몸,벽)
            collision = self._checkCollision(new_x, new_y)
            

            if isinstance(other, Snake) and other is not self:
                enemy_there=True
                enemy_head = other.body_positions[0][:2]
                if (new_x, new_y) != enemy_head:
                    # 적 몸통이면 그냥 부딪혀도 됨
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

          ''' # 내 머리 HP와, 몸통 중 최대 HP 비교
            head_hp = self.body_positions[0][2]
            body_hps = [segment[2] for segment in self.body_positions[1:]]  # 머리 제외
            max_body_hp = max(body_hps) if body_hps else 0

            # 갈아끼우기 전략 조건
            if head_hp < max_body_hp and self.length >= 2:
                # 일부러 벽으로 향하는 방향 설정
                best_direction = self.crash(head_x, head_y)'
                
            print(f" my HP: {self.hp}, my atk: {self.attack}, 내 머리 HP: {self.body_positions[0][2]}")'
            '''
          
            if enemy_detected:
                print(f" enemy HP: {self.enemy_hp}, atk: {self.enemy_attack}, 상대 머리 HP: {self.enemy_head_hp}")
                if self.attack >= self.enemy_head_hp and self.body_positions[0][2] > self.enemy_attack:
                    # s내가 뒤지는게먼전지, 쟤가 뒤지는 게 먼전지 확인 ㅂㅌ
                    best_direction = self._chaseEnemy(head_x, head_y, self.enemy_position[0])
                else:
                    best_direction = random.choice(safe_directions) if safe_directions else [1, 0]
            else:
                best_direction = random.choice(safe_directions) if safe_directions else [1, 0]

        return super().move(best_direction)
    



    def detect(self, map: list[list[list]]) -> None:
        
        self.map = map  # 무브 실행 전에 얘 먼저 저장된대
        self.snakes_alive = [
            cell
            for row in map
            for cell in row
            if isinstance(cell, Snake) and cell is not self]
        
        super().detect(map)


    def _checkCollision(self, x: int, y: int) -> bool:
     
        if x < 0 or x >= len(self.map[0]) or y < 0 or y >= len(self.map):
            return True  # 벽 충돌
        if (x, y) in self.body_positions:
            return True  # 자기 몸 충돌
        return False
    


    def _getPosition(self) -> tuple[int, int]:
        return self.body_positions[0]
    


    def _chaseEnemy(self, my_x: int, my_y: int, enemy_pos: tuple[int, int]) -> list[int]:
       
        target_x, target_y = enemy_pos
        dx = 1 if my_x < target_x else -1 if my_x > target_x else 0
        dy = 1 if my_y < target_y else -1 if my_y > target_y else 0

        if dx != 0 and not self._checkCollision(my_x + dx, my_y):
            return [dx, 0]
        if dy != 0 and not self._checkCollision(my_x, my_y + dy):
            return [0, dy]

        return [1, 0]  # 갈 수 없으면 기본 방향




def main():
    
    #You can write your own testing code here
    
    # Initialize the snake
    snake = Chaewon()
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
