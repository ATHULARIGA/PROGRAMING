def sec_lar(l):
    
    for i in range(len(l)):
        max=l[0]
        if l[i] >max:
            l.append(l[i])
            print(l)
    print(l[-2])

l=[10,20,30,40,50]
sec_lar(l)

print("---------------")
def sec_lar(l):
    first=l[0]
    second=l[1]
    for i in l:
        if (i>first):
            second=first
            first=i
    print(second)
l=[10,20,30,40,50]
sec_lar(l)

print("---------------")
def sec_lar(l):
    if (l[0]>l[1]):
        max1,max2=l[0],l[1]
    else:
        max1,max2=l[1],l[0]
    for i in range(2,len(l)):
        if (l[i]>max1):
            max2=max1
            max1=l[i]
        elif(l[i]>max2):
            max2=l[i]
    return max2

l=[10,20,30,40,50]
sec_lar(l)
print(sec_lar(l))

print("---------------------------")
def sec_min(l):
    if (l[0]<l[1]):
        max1,max2=l[0],l[1]
    else:
        max1,max2=l[1],l[0]
    for i in range(2,len(l)):
        if (l[i]<max1):
            max2=max1
            max1=l[i]
        elif(l[i]<max2):
            max2=l[i]
    return max2

l=[10,20,30,40,50]
sec_lar(l)
print(sec_lar(l))
