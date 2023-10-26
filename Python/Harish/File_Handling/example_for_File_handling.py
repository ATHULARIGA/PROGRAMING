fname=input("enter a file name:")
fptr=open(fname,'w')
print(fptr)
for i in range(3):
    name=input("enter the name")
    num=input("enter the number")
    country=input("enter the name of country")
    mob=input("enter the mob number")
    data=name+" "+num+" "+country+" "+" "+mob+"\n"
    fptr.write(data)
    
fptr.close()
fptr=open(fname,'r')
print(fptr.read())
print("info is stored")