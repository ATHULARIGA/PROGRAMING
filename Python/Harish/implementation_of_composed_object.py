class Os:
    def __init__(self):
        self.status=True
        print("os is installing")
    def getOs(self):
        print("os is still installing")

class Mobile:
    def __init__(self,name):
        self.mname=name
        self.o=Os()
        print("mobile created")
        print("with os installed")
m=Mobile("iphone")
print(m.mname)
print(m.o.status)
m.o.getOs()
del m
print(m.mname)
print(m.o.status)
m.o.getOs()
