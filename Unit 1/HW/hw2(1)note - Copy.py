rectangularList =   [
                        [2,3,4],
                        [7,8,9],
                    ]

nonRectangularList =[
                        [2,3,4,5],
                        [7,9,5,6,9,3,2],
                        [2,5],
                        [3,4,5,6,9,10]
                    ]

maxx= max([len(i) for i in nonRectangularList])
ssum= [0]*maxx

for i in nonRectangularList:
    for j in range(len(i)):
        ssum[j]=ssum[j] +i[j]
print(ssum)


