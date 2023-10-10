a=[10,20,30,40,50]
a1=a #shallow copy
print(a is a1) #True
print(a) #[10, 20, 30, 40, 50]
print(a1) #[10, 20, 30, 40, 50]
del a[2]  
print(a) #[10, 20, 40, 50]
print(a1) #[10, 20, 40, 50]

#------------------------------------
a=[10,20,30,40,50]
a1=a #shallow copy
b1=a.copy() #deep copy
del a[2]
print(a)
print(a1)
print(b1)
print(a is a1)
print(a1 is b1)
print(a is b1)