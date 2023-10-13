import copy
a=[10,20,30,[40]]
print(a)
a1=a
b=copy.deepcopy(a)
print(a)
print(a1)
print(b)
a[1]=200
print(a)
print(b)