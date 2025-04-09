import random

class Dice:
    def roll(self):
        return random.randint(1, 6)

    def roll_two(self):
        return self.roll(), self.roll()

class Player:
    def __init__(self, playerid):
        self.id = playerid
        self.points = 0
        self.type = self.assign_type()

    def assign_type(self):
        chance = random.randint(1, 100)
        if chance <= 30:
            return 1
        elif chance <= 90:
            return 2
        else:
            return 3

    def check_win(self, dice_sum):
        if self.type == 1:
            return dice_sum in [6, 7, 8, 9]
        elif self.type == 2:
            return dice_sum in [2, 3, 4, 5, 9, 10, 11, 12]
        elif self.type == 3:
            return dice_sum in [2, 3, 4, 5, 6, 7, 8]

    def play_round(self, dice_sum):
        if self.check_win(dice_sum):
            self.points += dice_sum
            return "WIN"
        else:
            self.points -= dice_sum
            return "LOSS"

def main():
    numplayers = int(input("How many players? "))
    num_rounds = int(input("How many rounds? "))

    players = [Player(i+1) for i in range(numplayers)]
    dice = Dice()

    for round in range(1, num_rounds + 1):
        print(f" round {round} ")
        for p in players:
            d1, d2 = dice.roll_two()
            dice_sum = d1 + d2
            result = p.play_round(dice_sum)
            print(f"player {p.id} (Type {p.type}) rolled {d1} + {d2} = {dice_sum}-> {result}, Total Points: {p.points}")

    maxscore = max([p.points for p in players])
    winners = []
    for p in players:
        if p.points == maxscore:
            winners.append(p.id)


    print(" GAME OVER ")
    print(f"highest Score: {maxscore}")
    print("winner id:",winners)


main()
    



