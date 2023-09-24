# str=input('enter the string : ').upper()
# new_str=""
# for i in str:
#     str=chr(ord(i)+1)
#     new_str=new_str+str #chr(str)
# print(new_str[::-1],end="")
#------------------------------
str=input('enter the string : ').upper()
ans=""
for i in str:
    ans=chr(ord(i)+1)+ans
print(ans)