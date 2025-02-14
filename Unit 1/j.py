def max(lst):
    if len(lst)==1:
        return lst[0]
    first=lst[0]
    a=max(lst[1:])
    if first>=a:
        return first
    else:
        return a
print(max([1,1,2,3,4,5,5,6,-1,-100,5,6,4,754]))


