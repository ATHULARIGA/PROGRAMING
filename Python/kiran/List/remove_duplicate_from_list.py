def rm_dup_list(l):
    count=0
    for i in range(len(l)-1):
        if l[i] in l[i+1:] or l[i] in l[:i] :
            l.pop(i)
            l.append("")
            print(l)
               
    print(l)
            
l=[34,21,3,12,34,56,76,5,4,21,12,12,34]

rm_dup_list(l)

print("---------------------------")
def rm_dup_list(list):
    for i in range(len(list)):
        print(list[i])
        for j in range(len(list)):
            if i==j:
                pass
            else:
                if list[i]==list[j]:
                    list.pop(j)
                    list.append(10)
    print(list)
list=[34,21,3,12,34,56,76,5,4,21,12,12,34]

rm_dup_list(list)
      