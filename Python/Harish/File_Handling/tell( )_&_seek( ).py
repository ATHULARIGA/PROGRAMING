fptr=open("names.txt", "r")
pos=fptr.tell()
print(pos)    #0
data=fptr.read(10)
print(data)
pos=fptr.tell()
print(pos)   #0


fptr.seek(0)
pos=fptr.tell()
print(pos)

fptr.seek(20)
pos=fptr.tell()
print(pos)      #20