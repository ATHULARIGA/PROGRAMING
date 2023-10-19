name=["kohli","rohit","naveen","babar","rahul"]
runs=[13000,10000,100,6000,8000]
country=["ind","ind","afg","pak","ind"]
ipl_m=["rcb","mi","lsg"]

# for i in range(len(country)):
#     print((name[i] , runs[i], country[i],ipl_m[i]))
info=list(zip(name,runs,country,ipl_m))
print(info)


print("----------------------------------------------")
#zip_longest

from itertools import zip_longest
name=["kohli","rohit","naveen","babar","rahul"]
runs=[13000,10000,100,6000,8000]
country=["ind","ind","afg","pak","ind"]
ipl_m=["rcb","mi","lsg"]

info=list(zip_longest(name,runs,country,ipl_m,fillvalue="#"))
print(info)

   
    


   
    

