a=(10,20,30,40,50)
print(a)
print(id(a))
a=a[0:2]+(25,)+a[2:]
print(a)
print(id(a))
