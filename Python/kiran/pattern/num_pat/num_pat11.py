def hollo_sq(n):
    for i in range(n):
        for j in range(n):
            if  j==0 or i==0 or i==4 or j==4:
                print(j+1, end=" ")
            else:
                print(" ", end=" ")
        print()
hollo_sq(5)
