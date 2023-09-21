'''
time comp O(n)


num=int(input("enter no:"))  #num:40
for i in range(1,num+1):
    if (num%i==0):
        print(i,end=" ")   #factors->1,2,3,4,5,8,10,20,40

'''
'''
#time comp O(n)

num=int(input("enter no:")) #num=40
for i in range(1,num//2+1):
    if (num%i==0):
        print(i,end=" ")  #1,2,3,4,5,8,10,20
                          #|
                          #|
print(num)                 #40
'''

import math
x=[]
num=int(input("enter no:")) #num=40
for i in range(1,int(math.sqrt(num))+1):
    if (num%i==0):
        x.append(i)
        print(i,end=" ")  #1,2,4,5
for i in x[::-1]:
        if(i!=num//i):
            print(num//i,end=" ") #40,20,10,8


"""
# The code is finding all the factors of a given number `num`. It uses the square root of `num` as the
# upper limit for the loop, as factors always come in pairs. The code first prints all the factors
# from 1 to the square root of `num`, and then prints the remaining factors from the square root of
# `num` to 1. The time complexity of this code is O(sqrt(n)), where n is the given number.


#time complexity  is O(sqrt(n))
import math
num=int(input("enter no:")) #num=40
for i in range(1,int(math.sqrt(num))+1):
    if (num%i==0):        
        print(i,end=" ")  #1,2,4,5
for i in range(int(math.sqrt(num)),0,-1):
    #if(i!=num//i) This is only to remove duplicates(EX:n=25)
    # will get 5 twice)
            if(i!=num//i):
                print(num//i,end=" ") #10 13 20 40

#running loop for 2 times so time complexity is 
#O(sqrt(n))  + O(sqrt(n))
#O(2(sqrt(n)))
"""