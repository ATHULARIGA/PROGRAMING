def num_patt(n):
    p=1
    for i in range(n):
        for j in range(i+1):
            print(p,end=" ")
        p+=1
        print()
    
n=5
num_patt(n)

# i=0 1 
# i=1 2 2 
# i=3 3 3 3 
# i=4 4 4 4 4 
# i=4 5 5 5 5 5 