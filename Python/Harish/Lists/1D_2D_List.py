L=['a','b',['hi',[10,20,30,],"bye"],'c','d','e',[10.1,20.1,["python"],30.1],'f','g']
print(L) #['a', 'b', ['hi', [10, 20, 30], 'bye'], 'c', 'd', 'e', [10.1, 20.1, ['python'], 30.1], 'f', 'g']
print(L[0]) #a
print(L[2][0]) #hi
print(L[2][1][2]) #30
print(L[5]) #e
print(L[6][1]) #20.1
print(L[6][2][0]) #python