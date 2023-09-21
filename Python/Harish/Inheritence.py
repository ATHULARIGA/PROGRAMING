class Parent:
    def __init__(self) -> None:
        self.a=10
class Child(Parent):
    def __init__(self) -> None:
        Parent.__init__(self)
        self.b=20
c1=Child()
print(c1.b)
print(c1.a)
'''
class a:
    def __init__(self) :
        self.a=10
class b(a):
    def __init__(self) :
        a.__init__(self)
        self.b=20
class c(b):
    def __init__(self):
        b.__init__(self)
        self.c=30
c1=c()
print(c1.c)
print(c1.b)
print(c1.a)
'''