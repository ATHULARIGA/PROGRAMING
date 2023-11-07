import time
class Demo :
    def printname(self):
        l=["rama", "sita", "ravana"]
        for names in l:
            print(names)
            time.sleep(3)
    def printnum(self):
        for i in range(10):
            print(i)
            time.sleep(2)
    def add(self):
        a=10
        b=20
        c=a+b
        print("sum is ",c)
d=Demo()
d.printname()
d.printnum()
d.add()
