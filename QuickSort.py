def Partition(l, low, high):
    i = low
    pivot = l[high]
    
    for j in range (low, high):
        if (l[j]<=pivot):
            l[i], l[j] = l[j],l[i]
            i+=1
           
    l[high],l[i] = l[i], l[high]
    
    return (i)
    


def Quicksort (l,p,r):
    if (p<r):
        q = Partition(l,p, r)
        Quicksort (l, p, q-1)
        q= p+1
        Quicksort (l, q+1, r)


l = [1,2,5,7,10,400,201,1203123,9,3,3252,12,4]
Quicksort(l,0,len(l)-1)
print(l)
