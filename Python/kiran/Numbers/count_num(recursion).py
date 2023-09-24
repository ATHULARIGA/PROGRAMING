def no_of_digits(num):
    if(num==0):
        return 0
    return(no_of_digits(num//10)+1)
num=int(input())
print(no_of_digits(num))