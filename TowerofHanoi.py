def move(n, start, temp, final):
    if(n>0): 
       move(n-1, start, final, temp)
       print(n, "Moved from", start, "to", final)
       move(n-1, temp, start, final)



move(3, "A", "B", "C")
