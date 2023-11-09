# prg to check weather even list is sorted or not
def even_lis_sorted(l):
    a=1
    d=1
    for i in range(len(l)-1):
        if l[i]%2==0:
            if l[i]<l[i+1] :
                a+=1
               
            elif l[i]>l[i+1]:
                d+=1
           
            if d==len(l) or a==len(l):
                print("sorted")
                
            else: print("not sorted")
                
print("---------------------------------------------------------------------------------------------")
l=[2,4,6,8]
print(l)
even_lis_sorted(l)

def even_lis_sorted(l):
    for i in range(1,len(l)):
        if(l[i]<l[i-1]):
            return False
    return True
                

l=[2,4,6,8]
print(l)
print(even_lis_sorted(l))


