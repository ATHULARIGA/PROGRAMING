fname=input("enter a file name:")
fptr=open(fname,'w')
print(fptr)
for i in range(2):
    name=input("enter the name")
    age=input("enter the age")
    jersy_no=input("enter the jersy no")
    matchs_play=input("enter the no of matches played")
    no_of_fifties=input("enter the no of hundreds")
    no_of_hundreds=input("enter the no of hundrteds")
    strikerate=input("enter the strikerate")
    data=name+" "+age+" "+jersy_no+" "+" "+matchs_play+" "+no_of_fifties+" "+no_of_hundreds+" "+strikerate+"\n"
    fptr.write(data)
    
fptr.close()
fptr=open(fname,'r')
#read() read()                # operation on file
#print(fptr.read())
print("info is stored")
# print(fptr.read(5))      # read(byte) operation on file

# print(fptr.readline())      # readline() operation on file

print(fptr.readlines())     # readlines() operation on file it prints entire data in list format



