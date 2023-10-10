a=[10,20,30,40,50,60,70,80,90]
print(len(a))
print(a)
print(a[4])
print(a[0:4])
print(a[4:6])
print(a[7:])
print(a[-3:-7])
print(a[:3])
print(a[-2:-8:-2])
print(a[::-1])
try:
    print(a[::0]) #ERROR
except Exception as e:
    print(e)

