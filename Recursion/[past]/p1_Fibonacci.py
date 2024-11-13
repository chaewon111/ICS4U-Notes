'''
Problem 1: Write a program and recurrence relation to find the Fibonacci series of n where n > 2 .

Mathematical Equation:
n if n == 0, n == 1;
fib(n) = fib(n-1) + fib(n-2) otherwise;

Recurrence Relation:
T(n) = T(n-1) + T(n-2) + O(1)

Input: n = 5
Output:
Fibonacci series of 5 numbers is : 0 1 1 2 3 5 8 13
                               n : 0 1 2 3 4 5 6 7
'''
# Python code to implement Fibonacci series
# Function for fibonacci
def fib(n):
    #TODO: CODE IMPLEMENTATION
    if (n == 0):
        return 0

    if (n == 1):
        return 1

    return fib(n-1) + fib(n-2)

def fib_series(n):
    res = []
    for i in range(0, n):
        res.append(fib(i))

# Driver code
if __name__=='__main__':
    # Initialize variable n.
    n = 5
    print("Fibonacci series of " + n + " numbers is :", end=" ")

    # For Loop to print the fibonacci series.
    for i in range(0, n):
        print(fib(i), end=" ")
