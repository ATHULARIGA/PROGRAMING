def num_patt(n):
    k=4
    for i in range(n-1):

        p=k
        
        for j in range(n):
            print(" ",end=" ")
        for j in range(n-1,i,-1):
            print(p,end=" ")
        for j in range(i):
            print(p+1,end=" ")
            p+=1
        k-=1
        
        print()
    # k=5
    # for i in range(n):
    #     p=k
    #     for j in range(n):
    #         print(" ",end=" ")
    #     for j in range(n,i,-1):
    #         print(p-1,end=" ")
    #     for j in range(i):
    #         print(p,end=" ")
    #         p+=1
    #     k-=1
        
    #     print()
        
    
n=5
num_patt(n)
