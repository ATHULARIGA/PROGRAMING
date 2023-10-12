a=[10,20,30]
b=[40,50,60]
c=a+b
print(c)  #[10, 20, 30, 40, 50, 60]
print("-------------------------------------")
a=[1,2,3]
c=a*3
print(c) #[1, 2, 3, 1, 2, 3, 1, 2, 3]
print("-------------------")

try:
    res1=a-b
    
    print(res1)
    
except Exception as e:
    print(e)
try:
    res2=a/b
    print(res2)
except Exception as e:
    print(e)

print("----------------------------------------------")
a=[33,44,55,66]
print(33 in a)
print(22 in a)
print(66 not in a)
print(66 in a)
print(22 not in a)
