
a = int(input("enter first value:"))
b = int(input("enter second value:"))
#max1 = max(a, b)
if(b>a):
  highest=b
else:
  highest=a

for i in range(highest,(a*b)+1):
  if (i % a == 0) and (i % b == 0) :
    print(i)
    break
  

