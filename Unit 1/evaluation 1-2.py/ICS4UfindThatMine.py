minetxt='mine.txt'
file=open('mine.txt','r')
minelist=[]
while True:
    line = file.readline()
    if line == "":
        break
    else:
        minelist.append(line.rstrip('\n').split())


# [n][n],[n][n-1],[n][n+1],, [][] [n-1][n-1],

for i in range(len(minelist)):
    for j in range(len(minelist[i])):
        if minelist[i][j]=='*':
            continue
        else:
            minelist[i][j]=0



for i in range(len(minelist)):
    for j in range(len(minelist[i])):
        if minelist[i][j]=='*':
            continue
        else:
            if i==0 and j==len(minelist[0])-1:
                if minelist[i][j-1]=='*':
                        minelist[i][j]=minelist[i][j]+1
                if minelist[i+1][j-1]=='*':
                        minelist[i][j]=minelist[i][j]+1
                if minelist[i+1][j]=='*':
                    minelist[i][j]=minelist[i][j]+1
            elif i==0 and j==0:
                if minelist[i+1][j]=='*':
                    minelist[i][j]=minelist[i][j]+1
                if minelist[i+1][j+1]=='*':
                    minelist[i][j]=minelist[i][j]+1
                if minelist[i][j+1]=='*':
                    minelist[i][j]=minelist[i][j]+1
            elif i==len(minelist)-1 and j==0:
                if minelist[i-1][j]=='*':
                        minelist[i][j]=minelist[i][j]+1
                if minelist[i-1][j+1]=='*':
                    minelist[i][j]=minelist[i][j]+1
                if minelist[i][j+1]=='*':
                    minelist[i][j]=minelist[i][j]+1
            elif i==len(minelist)-1 and j==len(minelist[0])-1:
                    if minelist[i-1][j-1]=='*':
                        minelist[i][j]=minelist[i][j]+1 
                    if minelist[i-1][j]=='*':
                        minelist[i][j]=minelist[i][j]+1
                    if minelist[i][j-1]=='*':
                        minelist[i][j]=minelist[i][j]+1


            
            elif i!=0 and i!=len(minelist)-1 and j==0:
                if minelist[i-1][j]=='*':
                    minelist[i][j]=minelist[i][j]+1
                if minelist[i-1][j+1]=='*':
                    minelist[i][j]=minelist[i][j]+1
                if minelist[i][j]=='*':
                    minelist[i][j]=minelist[i][j]+1
                if minelist[i][j+1]=='*':
                    minelist[i][j]=minelist[i][j]+1
                if minelist[i+1][j]=='*':
                    minelist[i][j]=minelist[i][j]+1
                if minelist[i+1][j+1]=='*':
                    minelist[i][j]=minelist[i][j]+1

            elif i!=0 and i!=len(minelist)-1 and j==len(minelist[0])-1:
                if minelist[i-1][j-1]=='*':
                        minelist[i][j]=minelist[i][j]+1
                if minelist[i-1][j]=='*':
                    minelist[i][j]=minelist[i][j]+1 
                if minelist[i][j-1]=='*':
                    minelist[i][j]=minelist[i][j]+1
                if minelist[i][j]=='*':
                    minelist[i][j]=minelist[i][j]+1  
                    
                if minelist[i+1][j-1]=='*':
                    minelist[i][j]=minelist[i][j]+1
                if minelist[i+1][j]=='*':
                    minelist[i][j]=minelist[i][j]+1
            elif j!=0 and j!=len(minelist)-1 and i==len(minelist)-1:
                if minelist[i][j-1]=='*':
                    minelist[i][j]=minelist[i][j]+1
                if minelist[i][j]=='*':
                    minelist[i][j]=minelist[i][j]+1
                if minelist[i][j+1]=='*':
                    minelist[i][j]=minelist[i][j]+1
                if minelist[i-1][j-1]=='*':
                        minelist[i][j]=minelist[i][j]+1
                if minelist[i-1][j]=='*':
                    minelist[i][j]=minelist[i][j]+1
                if minelist[i-1][j+1]=='*':
                    minelist[i][j]=minelist[i][j]+1

            elif j!=0 and j!=len(minelist)-1 and i==0:
                if minelist[i][j-1]=='*':
                        minelist[i][j]=minelist[i][j]+1
                if minelist[i][j]=='*':
                    minelist[i][j]=minelist[i][j]+1
                if minelist[i][j+1]=='*':
                    minelist[i][j]=minelist[i][j]+1

                if minelist[i+1][j-1]=='*':
                    minelist[i][j]=minelist[i][j]+1
                if minelist[i+1][j]=='*':
                    minelist[i][j]=minelist[i][j]+1
                if minelist[i+1][j+1]=='*':
                    minelist[i][j]=minelist[i][j]+1
            

            else:    
                if minelist[i-1][j-1]=='*':
                    minelist[i][j]=minelist[i][j]+1
                if minelist[i-1][j]=='*':
                    minelist[i][j]=minelist[i][j]+1
                if minelist[i-1][j+1]=='*':
                    minelist[i][j]=minelist[i][j]+1

                if minelist[i][j-1]=='*':
                    minelist[i][j]=minelist[i][j]+1
                if minelist[i][j]=='*':
                    minelist[i][j]=minelist[i][j]+1
                if minelist[i][j+1]=='*':
                    minelist[i][j]=minelist[i][j]+1

                if minelist[i+1][j-1]=='*':
                    minelist[i][j]=minelist[i][j]+1
                if minelist[i+1][j]=='*':
                    minelist[i][j]=minelist[i][j]+1
                if minelist[i+1][j+1]=='*':
                    minelist[i][j]=minelist[i][j]+1


file.close()


#[[2, '*', 1, 1, '*'], ['*', 3, 1, 1, 1], ['*', 2, 0, 0, 0], [2, 2, 0, 0, 0], ['*', 1, 0, 0, 0]]
'''for i in range(len(minelist)):
    for j in range(len(minelist[0])):
        file1.write(str(j))
        '''
with open('sss.txt', 'w') as file1:
    for row in minelist:
        file1.write(' '.join([str(item) for item in row]))
        file1.write('\n')


