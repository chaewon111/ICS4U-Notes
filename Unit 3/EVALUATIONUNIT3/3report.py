import random

class Dice:
    def roll(self):
        return random.randint(1, 6)

    def roll_two(self):
        return self.roll(), self.roll()

class Player:
    def __init__(self, playerid,atype):
        self.id = playerid
        self.points = 0
        self.type = atype


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
    numplayers = 300
    num_rounds = 10000

    players = [Player(i+1,1) for i in range(0,100)]
    players2 = [Player(i+1,2) for i in range(100,200)]
    players3 = [Player(i+1,3) for i in range(200,300)]

    dice = Dice()

    for round in range(1, num_rounds + 1):
        for p in players:
            d1, d2 = dice.roll_two()
            dice_sum = d1 + d2
            p.play_round(dice_sum)

        for p in players2:
            d1, d2 = dice.roll_two()
            dice_sum = d1 + d2
            p.play_round(dice_sum)

        for p in players3:
            d1, d2 = dice.roll_two()
            dice_sum = d1 + d2
            p.play_round(dice_sum)          


    sumscore1= sum([p.points for p in players])
    sumscore2= sum([p.points for p in players2])
    sumscore3= sum([p.points for p in players3])



    print(f'''        
        I assigned rounds, number of players, and types
        so that the empirical and theoretical probabilities would be similar.
        Below is the sum of player scores for each type over 10000 rounds.
        
          
        TYPE1 sum of total point: {sumscore1}
        TYPE2 sum of total point: {sumscore2}
        TYPE3 sum of total point: {sumscore3}

        
        As shown in the results above,
        Type 3 has the highest probability of winning.

    ''')

main()




'''
ex:
 I assigned rounds, number of players, and types
        so that the empirical and theoretical probabilities would be similar.
        Below is the sum of player scores for each type over 10000 rounds.
        
          
        TYPE1 sum of total point: 1230747
        TYPE2 sum of total point: 778686
        TYPE3 sum of total point: 1450084

        
        As shown in the results above,
        Type 3 has the highest probability of winning.


'''
    