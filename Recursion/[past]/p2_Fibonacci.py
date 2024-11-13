'''
Problem 2: Write a program and recurrence relation to find the Factorial of n where n>2 .

Mathematical Equation:
1 if n == 0 or n == 1;
f(n) = n*f(n-1) if n> 1;

Recurrence Relation:
T(n) = 1 for n = 0
T(n) = 1 + T(n-1) for n > 0

Input: n = 5
Output:
Factorial of 5 is: 120
                   5 * 4 * 3 * 2 * 1

                   4! = 4 * 3 * 2 * 1


1! = 1
0! = 1

4! = 4 * f=3!
3! = 3 * 2!
2! = 2 * 1!
1! = 1 * (1-1)!
0! = 1 # base condition


n=0! : 1
n=1! : 1 * (1-1)!
n=2! : 2 * (2-1)!
n=3! : 3 * (3-1)!
'''
# Python code to implement Fibonacci series
# Factorial function
def factorial(n):
    #TODO: CODE IMPLEMENTATION
    if (n == 0 or n == 1):
        return 1

    return n * factorial(n-1)

# Driver code
if __name__=='__main__':
    # Initialize variable n.
    n = 5
    print("Factorial of " + n, " is: ", end=" ")

    print(factorial(n))