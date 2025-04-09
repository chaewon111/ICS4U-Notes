class students:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def check(self):
        if self.age <16:
            return 'not eligible to apply for driive licence.'
        else:
            return 'eligible to apply for driive licence.'
        
    def __str__(self):
        return f'name:{self.name}, age: {self.age} is {self.check()}'
    

for i in range(10):
    name=input('enter name')
    age=int(input('enter age'))
    i=students(name,age)
    print(i)