#check if it is a ovel and replace that ovel character with special charater
#pentagon->p@nt@g@n
# str=input("Please enter:")
# rep=input("Please enter replace char:")

# def char_ovel(str):
#     ans=""
#     for i in str:
#         if i in "aeiou": #first iteration p==a or p==e or p==i or p==o or p==u
#             ans=ans+rep
#             #print(rep,end="")
#         else:
#             ans=ans+i
#             #print(i,end="")
#     print(ans)
# char_ovel(str)
#------------------------------------------------------------------------------------------
str=input("Please enter:")
rep=input("Please enter replace char:")

def char_ovel(str):
    ans=""
    for i in range(len(str)):
        data=str[i]
        if data in "aeiou": #first iteration p==a or p==e or p==i or p==o or p==u
            ans=ans+rep
            #print(rep,end="")
        else:
            ans=ans+data
            #print(i,end="")
    print(ans)
char_ovel(str)