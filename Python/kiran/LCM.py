"""
10->10,20,30,40
20->20,40,60
    1      10    20   8
10          __________|
20                ____|
"""
a = int(input("enter first value:"))
b = int(input("enter second value:"))
max1 = max(a, b)

while(True):
  if (max1 % a == 0) and (max1 % b == 0) :
    break
  max1 += 1
print(f"LCM of {a} and {b} is: {max1}")

