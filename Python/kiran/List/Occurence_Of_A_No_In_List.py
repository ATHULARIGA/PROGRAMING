def occ_of_no(x):
    l=[34,21,3,12,34,56,76,5,4,21,12,12,34]
    count=0
    for i in l:
        if x == i:
            count+=1
    return count
        
            
find=12
print(occ_of_no(find))