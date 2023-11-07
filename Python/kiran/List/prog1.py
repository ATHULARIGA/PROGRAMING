# given an array of size n-1 it consits no fro 1 to n and 1 number is missing amongs 1 to n

def missing_no(n):
    l=[]
    for i in range(1,n):
        l.append(i)
    print(l)
    l.pop(3)
    
    count=l[0]
    for i in range(len(l)):
         if l[i]==count:
             print(l[i],count)
             count+=1
    print(count)
   
n=10
missing_no(n)