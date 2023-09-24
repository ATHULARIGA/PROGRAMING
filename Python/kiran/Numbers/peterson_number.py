'''
n = (digit1!) + (digit2!) + ... + (digitk!)
here are a few examples of Peterson numbers:



1. **145**:
   - 1! + 4! + 5! = 1 + 24 + 120 = 145
   - 145 is equal to the original number, so 145 is a Peterson number.

2. **40**:
   - 4! + 0! = 24 + 1 = 25
   - 25 is not equal to the original number 40, so 40 is not a Peterson number.

3. **1**:
   - 1! = 1
   - 1 is equal to the original number, so 1 is a Peterson number (since any single-digit number is considered a Peterson number).

4. **4320**:
   - 4! + 3! + 2! + 0! = 24 + 6 + 2 + 1 = 33
   - 33 is not equal to the original number 4320, so 4320 is not a Peterson number.

These examples demonstrate the concept of Peterson numbers, where some numbers can
 be expressed as the sum of factorials of their individual digits.
'''
'''
n=int(input("enter Number"))
res=0
rem=0
num=0
while(n>0):
    rem=n%10
    fact=1
    for i in range(1,rem+1):
        fact=fact*i
    res=res+fact
    n=n//10
print(res)
'''
'''
n=int(input("enter Number"))
def peterson(n):
    temp=n
    res=0
    while(n>0):
        rem=n%10
        def factorial(rem):
            a=1
            for j in range (1,rem+1):
                a=a*j
            return a
        res=factorial(rem)+res
        n=n//10
    if res==temp:
        print("peterson number")
    else:
        print("not peterson number")
    return res
    


print(peterson(n))

'''
'''
def fact(rem):
    sum=1
    for i in range(1,rem+1):
        sum=sum*i
    return sum
num=int(input("enter number")) 
res=0
temp=num
while(num>0):
    rem=num%10
    res=fact(rem)+res
    num=num//10
if (temp==res):
    print("peterson")
else:
    print("not")   
'''
def peterson(num,res):
    if(num==0):
        return res
    a=1
    for i in range(1,(num%10)+1):
        a=a*i
    return peterson(num//10,res+a)
res=0
num=int(int(input()))
print(peterson(num,res))