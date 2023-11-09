def merge(left,right):
    i,j=0,0
    result=[]
    while(i<len(left) and j<len(right)):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        elif left[i]>right[j]:
            result.append(right[j])
            j+=1
    result+=left[i:]
    result+=right[j:]
    return result
def mergesort(l):
    if len(l)<=1:
        return l
    mid=int(len(l)/2)
   
    
    left=mergesort(l[:mid])
    right=mergesort(l[mid:])
    
    return(merge(left,right))

l=[48,47,487,24,38,38,39]
print(mergesort(l))


