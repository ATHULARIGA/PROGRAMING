# The `seek()` function is used to change the current position of the file pointer in a file. It takes
# an optional argument that specifies the position to seek to, relative to the beginning of the file.

# The `tell()` function is used to determine the current position of the file pointer in a file. It
# returns the current position as an integer value.

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