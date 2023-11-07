def rev_list(l):
    for i in range(len(l)-1,-1,-1):
        num=l[i]
        l1.append(num)
    print(l1)

    
    
l=[10,20,30,40,50,60]
l1=[]
rev_list(l)

print("-------")
def rev_list(list):
    i=0
    j=len(list)-1
    while i<j:
        list[i], list[j] = list[j], list[i]
        i=i+1
        j=j-1
    print(list)
list=[10,20,30,40,50,60]

rev_list(list)

print("-----------")

def rev_list(list):
    i=0
    j=len(list)-1
    while i<j:
        temp=list[i]
        list[i]=list[j]
        list[j]=temp
        i=i+1
        j=j-1
    print(list)
list=[10,20,30,40,50,60]

rev_list(list)