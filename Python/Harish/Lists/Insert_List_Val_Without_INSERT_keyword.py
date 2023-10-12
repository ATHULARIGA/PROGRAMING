def insert(a,pos,val):
    
    
        for i in range(len(a)):
            

            if i == pos:
                a=a[:i]+[val]+a[i:]
        return a

a=[1,3,5,6,7,10]

pos=int(input("enter position to insert in list:"))
val=int(input("value to insert in above position:"))

a=insert(a,pos,val)
print(a)
