def replace(a,pos,int1):
    for i in range(len(a)):
        if i==pos:
            a[i]=int1
    print(a)
    
a=[1,2,5,6,7]
pos=int(input("enter position to replace in list:"))
int1=int(input("value to replace in above position:"))
replace(a,pos,int1)
print("--------------------------")
