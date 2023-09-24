
class Tiger:
    def eat(self):
        print("tiger is eating")
    def sleep(self):
        print("tiger is sleepin")
    def breath(self):
        print("tiger is breathing")
class Deer:
    def eat(self):
        print("Deer is eating")
    def sleep(self):
        print("Deer is sleeping")
    def breath(self):
        print("Deer is breathing")
class Monkey:
    def eat(self):
        print("Monkey is eating")
    def sleep(self):
        print("Monkey is sleeping")
    def breath(self):
        print("Monkey is breathing")
def animal(ref):
    ref.eat()
    ref.sleep()
    ref.breath()



c=Tiger()
p=Deer()
f=Monkey()

animal(c)
animal(p)
animal(f)