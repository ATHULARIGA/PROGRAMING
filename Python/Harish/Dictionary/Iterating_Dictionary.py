#dict_name = {key1: value1, key2: value2,....value n}

empinfo = {'name':'Rama', 'age': 24, 'height':6.2,'mobile':987654321}
print(empinfo)
print(type(empinfo))
print(empinfo['name'])
empinfo['address'] ="Bengaluru"
print(empinfo)
for i in empinfo.values():
    print(i)
for i in empinfo.items():
    print(i)
for i in empinfo.keys():
    print(i)
print(help(type(empinfo)))