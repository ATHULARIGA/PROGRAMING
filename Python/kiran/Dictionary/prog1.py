def fun1(list1):
    for i in list1:
        if i not in dict1:
            dict1[i]=1
        else:
            dict1[i]+=1
    print(dict1)            
str1="Hi rama hello rama and rama is sleeping"
dict1={}
list1=str.split("")
fun1(list1)