def tri(n):
    p=1
    for i in range(n):
       
        for j in range(i+1):
            print(p, end=" ")
        p=p+1
        for j in range(i,n):
            print(" ", end=" ")
        for j in range(n,i,-1):
            print(" ", end=" ")
        
        print()
    p=4
    for i in range(n+1):
        
        for j in range(i,n-1):
            print(p, end=" ")
        p=p-1
        for j in range(i+1):
            print(" ", end=" ")
        for j in range(i+1):
            print(" ", end=" ")
    
        
        print()
tri(5)