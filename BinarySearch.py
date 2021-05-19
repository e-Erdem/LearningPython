def bin_search(l, L, R, x):
    if (R>=0):
        mid = int((L+R)/2)
        if (l[mid]==x):
            return mid
        elif (x< l[mid]):
            return bin_search(l,L,mid-1,x)
        else:
            return bin_search (l, mid+1, R,x)
    else:
        return -1
            
l = [0,10, 11, 12, 13, 27, 37]

print (bin_search(l, 0, len(l)-1,37))
