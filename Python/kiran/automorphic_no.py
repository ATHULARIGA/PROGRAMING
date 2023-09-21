'''


number    sq        automorphic
5        5*5=25      last digit is 5
6        6*6=36      last digit is 6
25      25*25=625    last digit is 25

'''
"""
num=int(input("Enter the number: ")) #25
num1=num  #25
sq=num*num #625
equal=False
temp=10

while(num1>0): #25
    rem=sq%temp   #25
    if rem==num:  #25==25
        equal=True
        break
    num1=num1//10  #2
    temp=temp*10   #100
if(equal):
    print("Auto-morphic")
else:
    print(" not Auto-morphic")

"""
# num=int(input("Enter the number: "))
# num1=num
# sq=num*num

# def auto_no(num):
#     temp=10
#     while(num>0):
#         rem=sq%temp
#         if num1==rem:
#             print("automorphic")
#             break
#         else:
            
#             num=num//10
#             temp=temp*10
            
        
    
# auto_no(num)


def square_num(num):
    square_num=num*num
    return square_num


def automorphic(num,sq_num):
    while(num>0  and  sq_num>0 ):
        if (num%10 == sq_num%10):
            num=num//10
            sq_num=sq_num//10
        else:
            return False
    return True
num=int(input("enter:"))
sq_num=square_num(num)
print(automorphic(num,sq_num))

if(automorphic(num,sq_num)==True):
    print("automorphic")
else:
    print("not")