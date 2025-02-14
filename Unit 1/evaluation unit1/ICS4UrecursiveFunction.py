# explanation::find the sum of each digit

def doThis(x):
    if x == 0:
        return 0
    else:
        return x % 10 + doThis(x // 10)
    
def iterative_ver(x):
    sum=0
    while True:
        a=x%10
        sum=sum+a
        x=x//10
        if x==0:
            break
    return sum

print(doThis(1))
print(iterative_ver(1))
    