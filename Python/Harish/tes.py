

class Brain:
    def __init__(self,name):
        self.bname = name
        print("brain is created")
    def getBrain(self):
        print("brain is working ")

class Car:
    def __init__(self,name):
        self.cname = name
        print("car is ready")
    def getCar(self):
        print("car is working ")
    

class Person:
    def __init__(self, name):
        self.pname = name
        self.b=Brain("brain1")
        self.c1=" "
        print("Person is ready")
    def hasCar(self,c):
        self.c1=c
p=Person("rahul")
c=Car("Audi")
p.hasCar(c)
print(p.pname)
print(p.b.bname)
print(p.c1.cname)
p.b.getBrain()
p.c1.getCar()
del p
c.getCar()
print(c.cname)
print(p.bname)

