def serchlast(lst,target):
    a=0
    for i in range(len(lst)):
        if target== lst[i]:
            a=i
    return a

def serchloc(lst,target):
    loc=[]
    for i in range(len(lst)):
        if target== lst[i]:
            loc.append(i)
    return loc


print(serchlast([1,2,3,4,5,6,7,8,9,9,9,9,9],2) ,serchloc([1,2,3,4,5,6,7,8,9,9,9,9,9],2))