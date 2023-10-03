# using list
# str=input("enter your string:")
# li=str.split(" ")
# for i in li:
#     print(i[::-1],end=" ")



# str="India is my home"                                    
# def rev_str(str):
#     new_str=""
#     count=0
#     for i in range(len(str)):
#         if (str[i]==" "):
#             str1=str[count:i+1][::-1]
#             new_str+=str1
#             count=i+1
#         elif i==len(str)-1:
#             str1=str[count:i+1][::-1]
#             new_str+=str1
#     print(new_str) 
       

# rev_str(str)  

# # Input: "this is my book"
# # Output: "siht si ym koob"


# str="india is my home"                                    
# def rev_Str(str):
#     new_str=""
#     count=0
#     for i in range(len(str)):
#         if (str[i]==" "):
#             str1=str[i-1].upper()+str[count:i-1][::-1]+" "
#             new_str+=str1
#             count=i+1
#         elif i==len(str)-1:
#             str1=str[count:i+1][::-1]
#             new_str+=str1
#     print(new_str) 
       

# rev_Str(str)  

# ## Input: "this is my book"
# # # Output: "Siht Si Ym Koob"


str="India is my home"                                    
def rev_str(str):
    new_str=""
    count=0
    for i in range(len(str)):
        if (str[i]==" "):
            str1=str[count:i+1][::-1]
            new_str+=str1
            count=i+1
        elif i==len(str)-1:
            str1=str[count:i+1][::-1]
            new_str+=str1
    print(new_str) 
       

rev_str(str)  

 
