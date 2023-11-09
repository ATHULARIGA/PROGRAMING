def binary_search(l,key):
    l=0
    h=len(l)-1
    while l<=h:
        mid=(l+h)//2
        if l[mid]==Key:
            return mid
        elif key<l[mid]:
            h=mid-1
        else:
            l=mid+1
    
    return -1
l=[10,20,30,40,50,60,70,80]
key=int(input())
print(binary_search(l,key))


