def check_Prime(num):
    for i in range(2,num):
        if(num%i==0):
            return False
    return True
num=int(input("Enter an element"))


