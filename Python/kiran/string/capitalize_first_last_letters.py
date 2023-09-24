def capitalize_first_last_letters(str):
    str1=""
    for i in range(len(str)):
        if i==0:
            str1=str[0].upper()
        if i==len(str)-1:
            str1=str1+str[i].upper()
        if i in range(1, len(str)-1):
            str1=str1+str[i]
    return str1
            
        
        
str="hello"
print(capitalize_first_last_letters(str))