# a=int(input("Enter a value 1: "))
# b=int(input("Enter a value 2: "))
# try:
#     res=a/b
#     print(res)
# except:
#     print("Exvept caught in program")
# print("pgm end")

def fun1():
    print("entering fun1")
    try:
        fun2()
    except Exception as e:
        print("Exvept caught in fun1")
    print("leaving fun1")
def fun2():
    print("entering fun2")
    res=10/0
    print("leaving fun2")
print("pgm started")
fun1()
print("pgm end ")