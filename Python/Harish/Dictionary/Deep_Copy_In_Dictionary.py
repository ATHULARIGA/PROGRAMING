d={1:44, 2:55 , 3:66, 4:77} 
print(d)
d[2]=22
print(d)
d1=d#shaloww copy
del d[2]
print(d)  #{1: 44, 3: 66, 4: 77}
print(d1) #{1: 44, 3: 66, 4: 77}
d2=d.copy()  #deep copy
del d[4]
print(d)    #{1: 44, 3: 66}
print(d1)   #{1: 44, 3: 66}
print(d2)   #{1: 44, 3: 66, 4: 77}