

for num in range(1,1000):
    for i in range(2,num):
        if(num%i==0):
            print("not prime")
            break
        
    else:

        print(num,end=" ")





