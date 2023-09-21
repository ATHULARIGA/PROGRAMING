class Book:
    def __init__(self,value):
        self.__pages=value
    def setdata(self,value):
        if( value >=1):
            self.__pages= value
    def getdata(self):
        return self.__pages
    
b1=Book(100)
b1.setdata(114)
num=b1.getdata()
print(num)
b1.pages=-99
b1.setdata(-99)
num=b1.getdata()

print(num)