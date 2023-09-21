def num_patt(n):
    p=1
    for i in range(n):
        for j in range(i+1):
            print(" ",end=" ")
        for j in range(i,n):
            print(p,end=" ")
        p+=1
        print()
    
n=5
num_patt(n)

# 1 1 1 1 1 
#   2 2 2 2 
#     3 3 3 
#       4 4 
#         5 
