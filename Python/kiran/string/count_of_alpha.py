str=input('enter the string : ').lower()
for i in range(97,123):
    j=chr(i)
    count=0
    for l in str:
        if j==l:
            count+=1
    if count>0:
        print(j,":",count)
