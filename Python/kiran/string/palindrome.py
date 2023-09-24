
# str=input("enter a str: ")
# rev=""
# for i in str:
#     rev=i+rev
# if str==rev:
#     print("palindrome")
# else:
#     print("not palindrome")
#not working
#---------------------------------------
# str=input("enter a str: ")
# str_len=len(str)
# str1=str_len//2
# str3=str[0:str1]

# str2=str[str1+1:len(str)+1]
# str2=str2[::-1]
# print(str2)
# if str3==str2:
#     print("palindrome")
# else:
#     print("not palindrome")
#----------------------------------------------------------------
def palindrome(str,i,j):
    while i<j:
        if str[i]!=str[j]:
            return False
        i+=1
        j-=1
    return True
str=input("Please enter:")
palindrome(str,i=0,j=len(str)-1)
if palindrome(str,i=0,j=len(str)-1)==True:
    print("palindrome")
else:
    print("not palindrome")
