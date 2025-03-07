

def selectionSort(a):
    new=[0]*len(a)
    small = 0
    smallIndex = 0

    for i in range (0,len(a)):

        #Sets the minimum to the first non sorted location
        small = a[i]

        #Search the rest of the list for the smallest value
        for j in range(i,len(a)):

            #Found a new smallest? record its location too.
            if a[j] <= small:
                small = a[j]
                smallIndex = j

        #Make the swap
        new[smallIndex] = small   
        
    return new

a=[4,3,2,1]

print(selectionSort(a))