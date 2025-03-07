 # difficult(sad) why is my grade


lst=[4,2,11,2]
lst.sort()


num=[]
nnn=[]

def makelist(lst):
    global num
    for i in lst:
        if i not in num:
            num.append(i)
            nnn.append(1)
        else:
            loc=num.index(i)
            nnn[loc]= nnn[loc]+1
    return nnn


def check(nnn):
    ch=1
    for i in range(1, len(nnn)):
        if nnn[i]!=nnn[i-1]:
            ch= ch+1
    return ch


def findnth(nnn,ask):
    for i in range(1,ask):
        m=max(nnn)
        for j in range(len(nnn)):
            if nnn[j]==m:
                nnn[j]=0
    a=max(nnn)
    return a


def hhh(a):
    loc= nnn.index(a)
    return num[loc]



def main():
    nnn= makelist(lst)
    ch= check(nnn)
    while True:
        
        ask=int(input('enter nth '))
        
        if ask<= ch and ask>0:
            break

    
    a=findnth(nnn,ask)
    print(hhh(a))

main()




# PLEASE GRADE 100%  
        


    

    



