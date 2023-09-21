
"""
def sum_digit(num):
    res=0
    while(num>0):
        rem = num % 10
        res += rem
        num = num// 10
    print(res)
num=int(input("enter:"))
sum_digit(num)

"""
def sum_of_digits(num):
    if(num==0):
        return 0
    return(no_of_digits(num//10)+num%10)
num=int(input())
print(sum_of_digits(num))
