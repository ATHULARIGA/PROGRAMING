str1=input("enter a string:")
sc=0
vovels=0
cons=0
for i in range(len(str1)):
    if str1[i] in "@#$%^&*()_+=-~`" :
        sc+=1
    elif str1[i] in "aeiouAEIOU":
        vovels+=1
    elif str1[i]==" ":
        pass
    else:
        cons+=1

print(sc)
print(vovels)
print(cons)
    
    