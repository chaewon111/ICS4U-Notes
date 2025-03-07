class circle:
    def __init__(self, radius):
        if radius<=0:
            self.radius=1
        else:
            self.radius= float(radius)
    
    def getarea(self):
        return self.radius * (3.14**2)

    def getcercum(self):
        return self.radius *3.14*2
    
    def __str__(self):
        return f'circle radius= {str(self.radius)}, area={str(self.getarea)}, circleference= {str(self.getcercum)}'
    

print(circle(2))
print(circle(4.3))
