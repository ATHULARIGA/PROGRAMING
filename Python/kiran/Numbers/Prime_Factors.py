'''
num=int(input("enter no:"))  
def prime_factor(num):
    i=2
    while(num>1):
        while(num%i==0):
            print(i)
            num=num//i
        i+=1

    
prime_factor(num)


'''
'''
import math
num=int(input("enter no:"))  
def prime_factor(num):
    for i in range(2, int(math.sqrt(num))+1):
        while(num%i==0):
            print(i)
            num=num//i
            
prime_factor(num)
'''
#this code wont work when the no is prime so if no is greater than 1 even after all the iterations then print num
import math
num=int(input("enter no:"))  
def prime_factor(num):
    for i in range(2, int(math.sqrt(num))+1):
        while(num%i==0):
            print(i)
            num=num//i
        if num > 1:
            print(num)
       
prime_factor(num)