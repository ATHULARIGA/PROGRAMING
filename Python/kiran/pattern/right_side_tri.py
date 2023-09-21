def triangle(n):
    for i in range(n):
        for j in range(i,n):
            print(" ",end=" ")
        for k in range(i+1):
            print("*",end=" ")
        print()
    
n=5
triangle(n)

# i=0               * 
# i=1             * *
# i=2           * * *
# i           * * * *
# i=4       * * * * *
