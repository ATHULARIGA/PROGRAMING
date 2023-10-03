class Charger:
    def __init__(self,name):
        self.cname=name
        print("charger is ready")
    def getCharger(self):
        print("charger is user for charging")

class Mobile:
    def __init__(self,name):
        self.mname=name
        self.c1=" "
        print("mobile Ready")
    def hasmobile(self,c):
        self.c1=c
        print("mobile and charger")
m=Mobile("iphone")
charge=Charger("iph charger")
m.hasmobile(charge)
print(m.mname)
print(m.c1.cname)
m.c1.getCharger()
del m
print(charge.cname)
charge.getCharger()
