
"""
#time complexity O(max(a,b))
#ex: 13 and 1
#euclid approach
def Euclid_gcd(a,b):
    while(a!=b):
        if(a>b):
            a=a-b
        else:
            b=b-a
    return a

a = int(input("enter first value:"))
b = int(input("enter second value:"))
print(Euclid_gcd(a,b))
"""
"""
def find_hcf(a,b):
    if(a<b):
        lowest=a
    else:
        lowest=b
    for i in range(1,lowest+1):
        if(a%i==0) and (b%i==0):
            hcf=i
    return hcf
a = int(input("enter first value:"))
b = int(input("enter second value:"))
print(find_hcf(a,b))


"""
"""
def find_hcf(a,b):
    if(a<b):
        lowest=a
    else:
        lowest=b
    for i in range(lowest+1,0,-1):
        if(a%i==0) and (b%i==0):
            hcf=i
            return hcf
a = int(input("enter first value:"))
b = int(input("enter second value:"))
print(find_hcf(a,b))
"""
#time complexity O(log(min(a,b)))
#ex: 13 and 1  
# a=31%1=0
# b=1
#gabriel approach



def gabriel_gcd(a,b):
    while(a!=0 and b!=0):
        if( a>b):
            a=a%b
        else:
            b=b%a
    if a==0:
        return b
    return a


a = int(input("enter first value:"))
b = int(input("enter second value:"))

print(gabriel_gcd(a,b))
