


import math

class Quadratic:
    def __init__(self, A, B, C):
        if A!=0: # if A=0, it's linear
            self.A = A
        else:
            self.A=1
        self.B = B
        self.C = C

    def direction_opening(self):
        return 'Up' if self.A > 0 else 'Down'

    def vertex_coordinates(self):
        h = round(-self.B / (2 * self.A),3)
        k = self.A * h**2 + self.B * h + self.C
        return [h, k]

    def y_intercept(self):
        return self.C 

    def x_intercepts(self):
        discriminant = self.B**2 - 4*self.A*self.C
        if discriminant < 0:
            return []
        sqrt_d = math.sqrt(discriminant)
        v1 = round((-self.B + sqrt_d) / (2 * self.A),3)
        v2 = round((-self.B - sqrt_d) / (2 * self.A),3)
        return [v1, v2] if v1 != v2 else [v1]

    def add(self, other):
        newA = self.A + other.A 
        newB = self.B + other.B
        newC = self.C + other.C
        return Quadratic(newA, newB, newC)

    def display_standard(self):
        return f"y = {self.A}x^2 + {self.B}x + {self.C}"

    def display_vertex(self):
        h, k = self.vertex_coordinates()
        return f"y = {self.A}(x - {h})^2 + {k}"

    def __str__(self):
        return f"standard form: {self.display_standard()}\n vertex form: {self.display_vertex()}"
    

q=Quadratic(1,2,3)
print(q)

q=Quadratic(-4,2,6)
print(q)
