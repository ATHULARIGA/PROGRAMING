def num_patt(n):
    
    for i in range(n):
        p=1   #columns are getting incremented
              #p gets reset to 1
        for j in range(i+1):
            print(p,end=" ")
        
            p+=1  #inside the inner loop
        print()
    
n=5
num_patt(n)

# 1 
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
