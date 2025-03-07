import random
class game:
    def __init__(self,name,point=0):
        self.name=name
        self.point=point

    def spin(self): # 60 % blue (3 ),,, 25%yello (5),,, 10% (red)8 ,,,,,5 blavk (0)
        color=[3,3,3,3,3,3,3,3,3,3,3,3,5,5,5,5,5,8,8,0]
        b=random.choice(color)
        self.point= b+ self.point
        return ''

    def roll(self):
        dice=[1,2,3,4,5,6]
        c=random.choice(dice)
        self.point= c+self.point
        return self.point

     

    def __str__(self):
        return f''' player {self.name} point ={self.spin()}{self.roll()}'''
    
print(game('yo'))


