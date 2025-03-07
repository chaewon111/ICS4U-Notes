#perent
class human:
    def __init__(self,name,hp:int,x:int,y: int):
        self.hp: int=hp
        self.position: list[int,int]=[x,y]
        self.name=name
    def __str__(self):
        return str(self.name)+str(self.hp)+ str(self.position)

    def move(self, direction: list[int,int])->None:
        self.position=direction

    def movexy(self,x:int, y: int):
        self.move([x,y])

    def getspecious() ->str:
        return 'human'
    
#inheritance
class student(human):
    def __init__(self,name,hp:int,x:int,y: int ,gradelevel,GPA):
        super().__init__(name,hp,x,y)
        self.gradelevel : int= gradelevel
        self.GPA: float= GPA

    def move(self, direction: list[int,int])->None:
        dir=[direction[0] *5, direction[1] *5]
        super().move(dir)


    student= student('student a',5,0,0,11,4)
    print(student)

    


    

    

    






