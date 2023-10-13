a=[10,20,30,40,50,60]
print(a)
a.remove(30)
print(a)
a.pop()
print(a)
a.pop()
print(a.index(20))

a.clear()
print(a)
try:
    del a
    print(a)
except Exception as e:
    print(e)
print("-------------------------------")
b=[10,20,30,10,20,10]
print(b)
print(b.count(10))