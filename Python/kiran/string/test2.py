# str="a2y3d4"
# str1=""
# int_str=0
# for i in range(len(str)):
#     if (i%2==0):
#         i=i+1
#         data=int(str[i])
#         for j in range(data):
#             str1=str[i-1]+str1
#             str2=sorted(str1)
#             ans=""
#             for ele in str2:
#                 ans=ans+ele
# print(ans)


# str="a2y3d4"
# ans=""
# for ch in str:
#     if ch.isalpha():
#         ex=ch
#     else:
#         ch=int(ch)
#         ans+=(ch*ex)
# print(ans)
# res="".join(sorted(ans))   #sorted datatype List is coverted to str
# print(res)

#--------------------------------------------------------------------------------------------    

str1="aayyydddd"
res=""
for i in range(97,123):
    j=chr(i)
    count=0
    for l in str1:
        if j==l:
            count+=1
    if count>0:
        x=str(count)
        res+=(j+x)
print(res)

# strg="aayyyyddd"
# strg=strg+" "
# res=""
# prev=strg[0]
# count=0
# for ch in strg:
#     if prev == ch:
#         count+=1
#     else:
#         count1=str(count)
#         res=res+prev+count1
#         prev=ch
#         count=1
#         prev=ch
# print(res)
        
    
        

