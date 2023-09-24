'''
Here are a few more examples of Armstrong numbers:

371: 3^3 + 7^3 + 1^3 = 27 + 343 + 1 = 371
9474: 9^4 + 4^4 + 7^4 + 4^4 = 6561 + 256 + 2401 + 256 = 9474
'''

num=int(input())
dig=len(str(num))

temp=num
def armstrong(num):
    res=0
    while(num>0):
        rem=num%10
        res=(rem**dig)+res
        num=num//10
    #return res
    if res==temp:
        print("Armstrong")
    else:
        print("Not Armstrong")

armstrong(num)




# def armstrong(num,res):
#     if(num==0):
#         return res
#     else:
#         res=(num%10)**digit+res
#         return armstrong(num//10,res)
# num=int(input(("enter")))
# digit=len(str(num))
# print(armstrong(num,0))