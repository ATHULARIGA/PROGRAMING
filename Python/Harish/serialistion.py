import pickle
class Employee:
    def __init__(self, name,id,sal,mob):
        self.ename = name
        self.eid = id
        self.esal=sal
        self.emobl=mob
    def disp(self):
        print(self.ename,self.eid,self.esal,self.emobl)
e=Employee("rama",101,50000,1111)
f=open("name.txt","wb")
pickle.dump(e,f)
print("obj stored in file")
f.close
