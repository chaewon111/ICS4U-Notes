'''
## Comparing Execution Times - Triangle Numbers
Run the Following Code to compare the execution times for the iterative vs the recursive Triangle Number Algorithms

    Try a small number < 10
    Try a number between 10 and 100
    Try a number over 1000000
'''
import timeit

def triangleRecursive(N):

    if N == 1:
        return 1
    else:
        return N + triangleRecursive(N-1)

def triangleIterative(N):
    sum = 0
    for i in range(1,N+1):
        sum = sum + i
    return sum

def main():
    num = int(input("Calculate Triangle Number for N = "))

    print("\nRecursive:")
    start = timeit.default_timer()
    tNumber = triangleRecursive(num)
    end = timeit.default_timer()
    elapsedNS = round((end - start)*10**9)
    print("Triangle(",num,") = ", tNumber)
    print("Solution took",elapsedNS,"nanoseconds\n")

    print("Iterative:")
    start = timeit.default_timer()
    tNumber = triangleIterative(num)
    end = timeit.default_timer()
    elapsedNS = round((end - start) * 10 ** 9)
    print("Triangle(", num, ") = ", tNumber)
    print("Solution took",elapsedNS,"nanoseconds")

main()