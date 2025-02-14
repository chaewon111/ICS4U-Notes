cases=[100,500,1000,5000,10000,25000,50000,100000,500000,1000000]
def dealnodeal(cases):
    
    ask=input('enter cases seperated by commas: ').split(',')
    ask=list(map(int,ask))
    bank=int(input('enter bank offer: '))
    
    if len(cases)<=len(ask):
        print('unvalid value')
        return dealnodeal(cases)
    
    sum=0
    for i in range(len(cases)):
        if i +1 in ask:
            pass
        else:
            sum=sum+cases[i]

    average=sum/(len(cases) - len(ask))
    print('average' ,average)
    

    
    if bank> average:
        return 'deal'
    else:
        return 'no deal'
    

print(dealnodeal(cases))
   


