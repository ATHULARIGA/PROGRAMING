import math
def factor(num):
    for i in range(1,int(math.sqrt(num))+1):
        if num%i==0:
            print(i,end=" ")
    for i in range(int(math.sqrt(num)),0,-1):
        #if(i!=num//i):
                print(num//i,end=" ")
factor(40)