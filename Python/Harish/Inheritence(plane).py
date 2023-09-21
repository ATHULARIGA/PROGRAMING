'''
class Cargoplane:
    def takeoff(self):
        print("Plane is taking-off")
    def fly(self):
        print("Plane is flying")
    def land(self):
        print("Plane is landing")
    def carryC(self):
        print("Plane is carrying cargo")
class Passangerplane:
    def takeoff(self):
        print("Plane is taking-off")
    def fly(self):
        print("Plane is flying")
    def land(self):
        print("Plane is landing")
    def carryp(self):
        print("Plane is carrying passangers")
class Fighterplane:
    def takeoff(self):
        print("Plane is taking-off")
    def fly(self):
        print("Plane is flying")
    def land(self):
        print("Plane is landing")
    def carryW(self):
        print("Plane is carrying wepons")

c=Cargoplane()
p=Passangerplane()
f=Fighterplane()
print("--------------------------------------")
c.takeoff()
c.fly()
c.land()
c.carryC()
print("--------------------------------------")
p.takeoff()
p.fly()
p.land()
p.carryp()
print("--------------------------------------")
f.takeoff()
f.fly()
f.land()
f.carryW()
'''
class Plane:
    def takeoff(self):
        print("Plane is taking-off")
    def fly(self):
        print("Plane is flying")
    def land(self):
        print("Plane is landing")
class Cargoplane(Plane):
    def carryC(self):
        print("Plane is carrying cargo")
class Passangerplane(Plane):
    def carryp(self):
        print("Plane is carrying passangers")

class Fighterplane(Plane):
    def carryW(self):
        print("Plane is carrying wepons")
c=Cargoplane()
p=Passangerplane()
f=Fighterplane()
print("--------------------------------------")
c.takeoff()
c.fly()
c.land()
c.carryC()
print("--------------------------------------")
p.takeoff()
p.fly()
p.land()
p.carryp()
print("--------------------------------------")
f.takeoff()
f.fly()
f.land()
f.carryW()