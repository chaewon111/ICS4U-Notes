suit=input('enter suit seperated by comma: ')
value=input('enter value seperated by comma: ')

cardinput='cardinput.txt'
cardoutput='cardoutput.txt'

file = open(cardinput, "w")
file.write(suit)
file.write('\n')
file.write(value)

file.close()
###############################################


file1=open(cardinput,'r')


line = file1.readline()
suitlst=line.rstrip('\n').split(',')
line = file1.readline()
valuelst=line.rstrip('\n').split(',')
file1.close()



##################################################

final=[]
for i in suitlst:
    uuu=[]
    for j in valuelst:
        uuu.append(str(j)+str(i))
    final.append(uuu)


with open(cardoutput, 'w') as file1:
    for row in final:   
        file1.write(' '.join([str(item) for item in row]))   
        file1.write('\n')




for row in final:
    for value in row:
        print(value, end=' ')
    print('')

        

#####################################

def check():
    for i in range(len(final)):
        for j in final[i]:
            if j !='-':
                return True
    else:
        return False
    
def check2(ask):
    for i in range(len(final)):
        for j in final[i]:
            if ask in j:
                return False
    else:
        return True

    

while check():
    ask=input('enter deck to remove (value+suit): ')
    if check2(ask):
        print(f'there is no {ask}: ')
        continue
    else:
        for i in range(len(final)):
            for j in range(len(final[i])):
                if final[i][j]==ask:
                    final[i][j]='-'
    print(final)










    

