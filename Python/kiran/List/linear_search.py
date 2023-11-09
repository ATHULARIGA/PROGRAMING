l=[10,20,30,40,50]
key=int(input("enter key to be searched:"))
def lin_search(l,k):
    for i in range(0,len(l)):
        if l[i]==key:
            print("element found at index",i)
            break
    else:
        print("element not found")
lin_search(l,key)