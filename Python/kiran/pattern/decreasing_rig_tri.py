def triangle(n):
    for i in range(n):
        for j in range(i,n):
            print("*",end=" ")
        print()
    
n=5
triangle(n)

# i=0 * * * * *
# i=1 * * * *
# i=2 * * *
# i=3 * * 
# i=4 * 