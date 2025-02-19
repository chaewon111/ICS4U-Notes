import random
file=open('dice.txt','w')
def creatdice():
    myData = []
    

    numRows = 6
    numColumns = 6

    for i in range(0,numRows):
        row = []
        for j in range(0,numColumns):
            number = random.randint(1,100)
            row.append(number)
        myData.append(row)
    return myData

def findmax():
    lllst=[]
    mydata=creatdice()
    print(mydata)
    m=0
    for i in range(6):
        a=max(mydata[i])
        if a>m:
            m=a
    for i in range(6):
        for j in range(6):
            if mydata[i][j]==m:
                print(f'maximum value({m}) located at ({i},{j})')
                file.write(i,j)



file=open('dice.txt','w')
hh=findmax()

for i in range(6):


    a= random.randint(1,6)
    b= random.randint(1,6)
    print(a,b)
    if (a,b)==hh:
        print(a,b)
        break





