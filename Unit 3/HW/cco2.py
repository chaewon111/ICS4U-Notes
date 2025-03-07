import    math

class circle:
    def __init__(self,radius):
        self.radius=radius
        

        

    def getarea(self):
        return self.radius * (3.14**2)

    def getcercum(self):
        return self.radius *3.14*2
    
    def __str__(self):
        return f'circle radius= {str(self.radius)}, area={str(self.getarea())}, circleference= {str(self.getcercum())}'
    


def main():
    
    centerx=int(input('enter center x '))
    centery=int(input('enter center y '))
    otherx=int(input('enter other x '))
    othery=int(input('enter other y '))

    radius=round(math.sqrt((centerx-otherx)**2+(centery-othery)**2),2)

    return circle(radius)

print(main())
main()
