'''
import math
def check_Prime(num):
    if num==0 or num==1:
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if(num%i==0):
            return False
    return True
num=int(input("Enter an element: "))
print(check_Prime(num))
'''
import math
def prime(num):
    if (num==0 or num==1):
        return False
    if (num==2 or num==3):
        return True
    if (num%2==0 or num%3==0):
        return False
    for i in range(5,int(math.sqrt(num))+1,6):
        if (num%i==0)or (num%(i+2)==0):
            return True
        
    return True
num=int(input("Enter an element: "))
print(prime(num))