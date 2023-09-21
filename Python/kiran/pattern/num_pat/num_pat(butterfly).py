def butterfly(n):
    for i in range(n):
        p=1
        for j in range(i+1):
            print(" ", end=" ")
            p=p+1
        for j in range(i,n):
            print(" ", end=" ")
        for j in range(n,i,-1):
            print(" ", end=" ")
        p=1
        for j in range(i+1):
            print("*", end=" ")
            p=p+1
        print()
    for i in range(n):
        p=1
        for j in range(i,n+1):
            print(" ", end=" ")
            p=p+1
        for j in range(i+1):
            print("*", end=" ")
        for j in range(i+1):
            print(" ", end=" ")
        p=1
        for j in range(i,n):
            print(" ", end=" ")
            p=p+1
        print()
butterfly(5)