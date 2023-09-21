"""
HCF of 2 no
10->|1|,|2|,\5\,\10\
20->|1|,|2|,4,\5\,\10\,20
HCF of 10 and 20 is 10
      1      5      10     20
10-------------------|
20--------------------------|


"""
a = int(input("enter first value:"))
b = int(input("enter second value:"))
lowest=min(a,b)
"""
if(a<b):
    lowest=a
else:
    lowest=b
"""
for i in range(1,lowest+1):
    if (a%i==0) and (b%i==0):
        hcf=i
print(hcf)



