lst=[1,2,3,4,5,6,7,8,9]
row= int(input('inputrow: '))
a=len(lst)//row 
b=len(lst)%row 


llst=[]
j=0
for i in range(1,a+1):
    llst.append(lst[j:row*i])
    j=j+row

if b==0:
    llst.append(lst[-a:])

else:
    llst.append(lst[-b:])

print(llst)