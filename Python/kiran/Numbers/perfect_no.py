"""
number     factorial      result            conclusion
6          1+2+3            6           it is a perfect number
28         1+2+4+7+14       28          it is a perfect number
8          1+2+4            7           it is not a perfect number
"""


def perfect_no(num):
    sum=0

    for i in range(1,num):
        if num%i==0:
            sum+=i
        
    return sum
n=int(input("enter number: "))
res=perfect_no(n)
print(res)
if(res==n):
    print("perfect")
else:
    print(" not perfect")
