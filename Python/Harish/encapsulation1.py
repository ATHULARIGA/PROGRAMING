class Person:
    def __init__(self):
        self.__name=" "
    def getter(self):
        return self.__name
    def setter(self,value):
        self.__name=value
    
p1=Person()
p1.setter("Bhima")
res=p1.getter()
print(res) #Bhima