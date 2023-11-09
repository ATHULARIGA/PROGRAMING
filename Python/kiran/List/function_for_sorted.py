def sorted(l):
    for i in range(len(l)):
        for j in range(0,len(l)-1):
            if l[j]>l[j+1]:
                l[j]=l[j+1]
print(l)
l=[40,30,25,20,15,10,5,2]
sorted(l)