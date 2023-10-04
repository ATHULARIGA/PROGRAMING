str1=input("enter a string:")
i=0
new_string=""
while i < len(str1):
    data=str1[i]
    asciiv=ord(data)
    if asciiv >65 and asciiv <90 :
        x=asciiv+32
        x1=chr(x)
        new_string=new_string+x1
    else:
        new_string+=data
    i+=1
print(new_string)
