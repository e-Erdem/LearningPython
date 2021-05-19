## BUBBLE SORT ##
l = [11, -1, 33, 45, 99, -23, 10101,1000,-2]
swapped = True
size= len(l)

while(swapped == True):
  swapped = False
  index = 0
  #while (index < size-1):
  for index in range(0,len(l)-1,1):
    if(l[index] > l[index+1]):
        swapped = True
        l[index],l[index+1] = l[index+1],l[index]
        #tmp = l[index]
        #l[index] = l[index+1]
        #l[index+1] = tmp
    #index +=  1
    
    
print(l)
