n=int(input('input radius of thecircle: '))

def find_penny(n):
    if n==1:
        return 1
    return 2*(n*2-1)+2*(n*2-3) + find_penny(n-1)

def findxy(x,y,n):
    x=int(input('enter x you wanna know '))
    y= int(input('enter y you wanna know '))
    if x**2+y**2 >n**2:
        False
    else:
        True

print(find_penny(n))                                   