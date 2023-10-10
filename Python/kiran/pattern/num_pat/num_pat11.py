def hollo_sq(n):
    
    for i in range(n):
        p=1
        
        for j in range(n):
            if  j==0 or i==0 or i==4 or j==4:
                if p<=4:
                    print(p, end=" ")
                else:
                    print(j-1,end=" ")
                
                
                    
            
            else:
                print(" ", end=" ")
            p+=1
        print()
hollo_sq(5)
