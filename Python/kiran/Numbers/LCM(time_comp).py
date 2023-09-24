#Time comp is same as gabriel GCD that is O(log(min(a,b)))
#Time comp for a*b is O(1)
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
lcm=(a*b)/gabriel_gcd(a,b)
print(lcm)