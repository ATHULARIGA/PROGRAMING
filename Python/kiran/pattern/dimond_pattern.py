def hill_pat(n):
    for i in range(n-1):
        for j in range(i,n):
            print(" ",end=" ")
        for j in range(i):
            print("*",end=" ")
        for j in range(i+1):
            print("*",end=" ")
        print()
    for i in range(n):
        for j in range(i+1):
            print(" ",end=" ")
        for j in range(i,n-1):
            print("*",end=" ")
        for j in range(i,n):
            print("*",end=" ")
            
        print()
    
            
        
    
n=5
hill_pat(n)

# i=0               * 
# i=1             * * *
# i=2           * * * * *
# i=3          * * * * * * *
# i=4         * * * * * * * *
