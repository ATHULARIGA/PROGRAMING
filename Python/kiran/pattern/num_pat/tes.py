def num_patt(n):
    k=4
    for i in range(n-1):
        p=k
        for j in range(i+1):
            print(p,end=" ")
            p-=1
        for j in range(n-1,i+1,-1):
            print(p+1,end=" ")


    
        print()

n=5
num_patt(n)