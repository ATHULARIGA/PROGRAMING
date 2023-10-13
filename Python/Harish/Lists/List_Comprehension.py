a=[10,20,30,40,50]
b=[]
for i  in a:
    newdata=i+1
    b.append(newdata)
print(b)
print("----------------------------------------------------")
a=[1,2,3,4,5]
b=[]
for i  in a:
    newdata=i*i
    b.append(newdata)
print(b)

print("----------------------------------------------------")
a=["krishna","arjuna","bhima"]
b=[]
for i  in a:
    newdata=i.upper()
    b.append(newdata)
print(b)

print("----------------------------------------------------")

a=list(range(10,21))

b=[]
for i  in a:
    if i%2==0:
        b.append(i)
    
    
print(b)

print("----------------------------------------------------")
a=["22222krishna33","333arjuna333","bhima","athul"]
b=[]
for i  in a:
    newdata=i.isalpha()
    if newdata==True:
        b.append(i)
print(b)
