counter = 10                             #Counter for counting numbers from 10 to 90
spc_c = 8                                #Space counter for counting the necessary spaces for alignment
flag = 1                                 #Controlling variable
n = 50                                   #Value of n, just to indicate the position of the pyramid


for i in range (1, n+1, 2):              #Evenly increased pyramid condition
    
    for j in range ((n-i)):              #Printing the spaces for creating a pyramid
        print (' ', end= '')
        
    for k in range (1,i+1):              #Printing numbers condition
        if(flag == 1):                   #Flag, in order to control the printed alignment spaces inside the loop
         print (spc_c*' ', end= '')      #Printing alignment spaces
        print (counter,'', end = '')     #Printing numbers and spaces as intended
        counter = counter + 1            #Increasing the numbers between 10-90
        flag = 0                         #Flag=0 for not printing alignment spaces again for one row
    if(counter == 91):                   #Condition for breaking the loop for not exceeding the number 90
      break
    
    
    spc_c = spc_c - 1                    #Space counter decreases since we need less spaces in order to align rows
    flag = 1                             #Flag=1 for making the if statement true in the next loop
    print ('\n')                         #Escape
