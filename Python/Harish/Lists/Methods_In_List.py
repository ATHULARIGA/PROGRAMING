a=[10,20,30,40,50]
print(a)
a.insert(2,25)
print(a)
a.append(60)
print(a)
a.append(70)
a.append(80)
try:
    a.append(90,100,110)
except Exception as e:
    print(e)
b=[90,100,110]
a.extend(b)
a.extend([120,130,140])
print(a)




    