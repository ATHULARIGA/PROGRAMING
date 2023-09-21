def num_patt(n):
   
    for i in range(n):
        for j in range(i+1):
            if i%2==0:
                print("1",end=" ")
            if i%2!=0:
                print("2",end=" ")
            
        
        print()
    
n=5
num_patt(n)

# 1 
# 2 2
# 1 1 1
# 2 2 2 2
# 1 1 1 1 1