nmk=input('enter row col track seperated by space ').split()
k=[]
for i in range(int(nmk[2])):
    track=input('row, colstart, colend spd by space ').split()
    k.append(track)

'''for i in range(len(k)):
    for j in range(len(k)-i):
        if i[0]==j[0]:
        '''
llst=[]
for i in range(int(nmk[0])):
    lst=[]
    for j in range(1,int(nmk[1])+1):
        lst.append(j)
    llst.append(lst)

#########################################
b=0
for i in range(len(k)):
    a=int(k[i][0])-1
    s=len(llst[a][int(k[i][1])-1:int(k[i][2])])
    print(s)
    b=s+b


print(len(llst)*len(llst[0])-b)
        
    









