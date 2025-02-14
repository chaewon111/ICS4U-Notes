def is_inside(x, y, R):
    return x**2 + y**2 <= R**2
        

def count_penny(x, y, R):
    if R == 0:  
        return 1
    if x > R:  
        return 0
    else:
        if y > R:  
            return count_penny(x + 1, -R, R)
        else:
            if is_inside(x, y, R):  
                return 1 + count_penny(x, y + 1, R)
            else:  
                return 0 + count_penny(x, y + 1, R)



R = int(input("Enter the R of the circle: "))
print(count_penny(-R,-R,R))


    

            
def is_inside(x,y,n):
    return x**2+y**2 <=n**2 



                           