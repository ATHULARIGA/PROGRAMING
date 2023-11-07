from threading import Thread
import time
class task1(Thread):
    def run(self):
        l=["rama", "sita", "ravana"]
        for names in l:
            print(names)
            time.sleep(3)
class task2(Thread):
    def run(self):
        for i in range(10):
            print(i)
            time.sleep(2)
class task3(Thread):
    def run(self):
         a=10
         b=20
         c=a+b
         print("sum is ",c)
t1=task1()
t2=task2()
t3=task3()
t1.start()
t2.start()
t3.start()
