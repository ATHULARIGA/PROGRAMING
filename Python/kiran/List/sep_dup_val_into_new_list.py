def rm_dup_list(list1):
    for i in range(len(list1)):
        print(list1[i])
        for j in range(len(list1)):
            if i==j:
                pass
            else:
                if list1[i]==list1[j]:
                    l1.append(list1[j])
                    list1.pop(j)
                    list1.append(10)
    x=set(l1)
    print(list(x))
    
l1=[]

list1=[34,21,3,12,34,56,76,5,4,21,12,12,34]

rm_dup_list(list1)
print("---------------------")

def rm_dup_list(list1):
    for i in range(len(list1)):
        
        for j in range(len(list1)):
            if i==j:
                pass
            else:
                if list1[i]==list1[j]:
                    l1.append(list1[j])
                    list1.pop(j)
                    list1.append(10)
    print(l1)
    
    for i in range(len(l1)):
        l1.sort()
        if l1[i]==l1[i+1]:
            
    print(l1)


    
l1=[]

list1=[34,21,3,12,34,56,76,5,4,21,12,12,34]

rm_dup_list(list1)