class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        #x,y 
    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"
        #display

class Circle:
    def __init__(self, center, r):
        self.center = center
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

    def __str__(self):
        return "Center: " + str(self.center) + ", Radius: " + str(self.r)

class Cylinder(Circle):
    def __init__(self, center, r, h):
        super().__init__(center, r)
        self.h = h

    def area(self):
        return 2 * 3.14 * self.r * self.h + 2 * 3.14 * self.r * self.r

    def volume(self):
        return 3.14 * self.r * self.r * self.h

zzz = Point(3, 4)
ll = Circle(zzz, 5)
print(str(zzz))
print(str(ll))
print("Circle area:", ll.area())

rr = Cylinder(zzz, 5, 10)
print(str(rr))
print("Cylinder area:", rr.area())
print("Cylinder volume:", rr.volume())
