'''
## What is Recursion?
You are used to programming and solving problems using control structures such as if-else statements (selection structures) and iterative loops (repetition structures)

Another control mechanism that can be used in problem solving and programming is recursion

The basic idea behind recursion is this:

- If the problem is considered easy solvable, solve it immediately
- If the problem can’t be solved immediately, divide it into easier problems, then solve the easier problems

Generally when a problem can be defined in terms of itself then it can be solved recursively
'''

'''
## Triangle Numbers
The total number of pins in a triangular arrangement is called a triangle number.

You can expand that pattern by keep adding rows with more pins:
    Row 1 -> 1 Pin
    Row 2 -> 3 Pins
    Row 3 -> 6 Pins
    Row 4 -> 10 Pins
    Row 5 -> 15 Pins
    Row 6 -> 21 Pins
    Row 7  -> 28 Pins

There is a pattern here:
    Total # pins in row 1 = 1
    Total # pins in row 2 = 2  + Total # of pins in row 1
    Total # pins in row 3 = 3 + Total # of pins in row 2
    Total # of pins in row 4 = 4 + Total # of pins in row 3
    Total # of pins in row 5 = 5 + Total # of pins in row 4

Mathematically you can write out the # of pins in the Nth row as:

    Triangle (N) = N + Triangle (N – 1)

Examples:

Triangle(3)
    = 3 + Triangle(2)
    = 3 + (2+Triangle(1))
    = 3 + (2 + (1))
    = 6

Triangle(7)
    = 7 + Triangle(6)
    = 7 + (6 + Triangle(5))
    = 7 + (6 + (5 + Triangle(4)))
    = 7 + (6 + (5 + (4 + Triangle(3))))
    = 7 + (6 + (5 + (4 + (3 + Triangle(2)))))
    = 7 + (6 + (5 + (4 + (3 + (2 + Triangle(1))))))
    = 7 + (6 + (5 + (4 + (3 + (2 + 1)))))
    = 28

Because you have defined the Nth Triangle number in terms of itself, this is a perfect problem to solve recursively.

Notice that in both examples above the sequence of additions ended with Triangle(1) = 1. This is called *the base case* for the problem

    - A base case is a problem that can be easily solved immediately
    - It typically tells you when the recursion should stop
'''
def triangle(N):

    #Base Case
    if N == 1:
        return 1

    #Recursive Call
    else:
        return N + triangle(N-1)


'''
## Fibonacci Sequence
You have probably studied and are familiar with the Fibonacci Sequence of numbers

    1,1,2,3,5,8,13,,21,34,55,….

Each value in the sequence is found by adding the previous two values in the sequence.

Mathematically we can define this as

    Fib (N) = Fib(N-1) + Fib(N-2) for N >= 3

The base cases for this recursion are Fib(1) = 1 and Fib(2) = 1

Translating that into a python function would look as follows
'''
def fib(N):

    # Base Condition
    if N == 1 or N == 2:
        return 1

    # Recursion Call
    else:
        return fib(N-1) + fib(N-2)


'''
## Iteration vs Recursion
You might be wondering, why recursion is necessary at all, when the two programs above could have easily been written with a loop.

# Iterative Triangle Number
If you look at the pattern that occurs for the Nth triangle number, you will see that its value is just the sum of the numbers from 1 to 10

    Triangle(3) = 6 = 1 + 2 + 3
    Triangle(7) = 28 = 1 + 2 + 3 + 4 + 5 + 6 + 7

That is easily accomplished using a simple loop
'''
def triangle(N):
    sum = 0
    for i in range(1,N):
        sum = sum + i
    return sum

'''
## Iterative Fibonacci Sequence
This one might be a little more complicated to understand from a looping perspective, but just need to keep track of the previous two values in some variables.
'''
def fib(N):

    f1 = 1
    f2 = 1
    for i in range(1,N-1):
        nextValue = f1 + f2
        f1 = f2
        f2 = nextValue

    return f2

# Well, the answer to the above question of recursion vs iteration, isn’t exactly straight forward.


'''
## Generally Speaking

    - Code size is smaller and sometimes logically easier to understand using recursion
    - Iterative solutions are usually faster (It takes more time to call functions then to execute a loop)
    - Recursion can take up more memory and is subject to Stack Overflow Errors
    - Some problems are just naturally recursive in nature
        * Towers of Hanoi
        * Maze Solving
        * Sorting Methods
'''