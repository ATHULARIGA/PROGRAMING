def hollo_sq(n):
    
    for i in range(n):
        p=0
        
        for j in range(n):
            if  j==0 or i==0 or i==4 or j==4:
                    print(p+1, end=" ")
                    p=p+1

            else:
                print(" ", end=" ")
        print()
hollo_sq(5)
