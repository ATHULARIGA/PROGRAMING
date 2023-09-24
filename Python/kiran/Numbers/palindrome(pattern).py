#num=int(input("enter the number: "))
"""
def palindrome(num):
    res=0
    temp=num
    while(num>0):
        rem=num%10
        res=(res*10)+rem
        num=num//10
    if temp==res:
        return True
    return False


row=int(input("enter the number: "))
k=1
for i in range(1,row+1):
    for j in range(i):
        while(True):
            if palindrome(k)==True:
                print(k,end=" ")
                k+=1
                break
            else:
                k+=1
    print()
"""
"""
def reverse(num):
    res=0
    while(num>0):
        rem=num%10
        res=(res*10)+rem
        num=num//10
    return sum
def check_pal(k):
    while(True):
        sum=reverse(k)
        if sum==k:
            return k
        else:
            k=k+1
k=1
for i in range(6):
    for j in range(i+1):
        print(check_pal(k),end=" ")
        k+=1
    print()
"""

'''
def palindrome(num):
    if num ==1:
         return 0
    if num==2:
         return 1
    return palindrome(num-1)+palindrome(num-2)
#palindrome(10)

        


row=int(input("enter the number: "))
k=1
for i in range(1,row+1):
    for j in range(i):
            print(palindrome(k),end=" ")
            k+=1
    print()
'''



# def palindrome(num):
#     a, b = 0, 1
#     for i in range(num):
#         a, b = b, a + b
#         return a
# #palindrome(10)

        


# row=int(input("enter the number: "))
# k=1
# for i in range(1,row+1):
#     for j in range(i):
#             print(palindrome(k),end=" ")
#             k+=1
#     print()
