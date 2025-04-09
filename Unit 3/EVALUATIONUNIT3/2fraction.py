

import math
import random

class Fraction:
    def __init__(self, numerator, denominator):

        self.numerator = numerator
        if denominator!=0:
            self.denominator = denominator
        else:
            denominator=10
        self.reduce()

    def reduce(self):
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator = self.numerator //gcd
        self.denominator = self.denominator//gcd

    def equals(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def add(self, other):
        new_den = math.lcm(self.denominator, other.denominator)
        a = new_den // self.denominator
        b = new_den // other.denominator
        new_num = a * self.numerator + b * other.numerator
        return Fraction(new_num, new_den)

    def subtract(self, other):
        new_den = math.lcm(self.denominator, other.denominator)
        a = new_den // self.denominator
        b = new_den // other.denominator
        new_num = a * self.numerator - b * other.numerator
        return Fraction(new_num, new_den)

    def multiply(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def divide(self, other):
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"



def quiz():
    while True:
        nu1 = random.randint(1, 14)
        de1 = random.randint(nu1 + 1, 15)
        nu2 = random.randint(1, 14)
        de2 = random.randint(nu2 + 1, 15)

        f1 = Fraction(nu1, de1)
        f2 = Fraction(nu2, de2)

        op = random.choice(["+", "-", "*", "/"])

        if op == "+":
            correct = f1.add(f2)
        elif op == "-":
            correct = f1.subtract(f2)
        elif op == "*":
            correct = f1.multiply(f2)
        else:
            correct = f1.divide(f2)
            if int(correct)==correct:
                pass
            else:
                op=='*'
                correct = f1.multiply(f2)


        print(f"What is {f1} {op} {f2}? (answer as n/d )")
        userans = input("enter answer: ")


        
        user_num, user_den = map(int, userans.split("/"))
        userfrac = Fraction(user_num, user_den)
        if userfrac.equals(correct):
            print("Correct")
        else:
            print(f"incorrect. Correct answer: {correct}")
            print('please enter lowest term as n/d')


        cont = input("if you want to stop, enter stop: ")
        if cont == "stop":
            break

quiz()

    #좆같이 처어렵네 시발 s