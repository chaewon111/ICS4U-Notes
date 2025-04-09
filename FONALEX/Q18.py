#str.count('d')

alpha='abcdefghijklmnopqrstuvwxyz'

lst=[]

def main(userstr):
    for i in alpha:
        strcount=userstr.count(i)
        if strcount!=0:
            lst.append([i,strcount])

    return lst

userstr='pineapple'
print(main(userstr))