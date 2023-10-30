def comp_list(l1,l2):
    c1=0
    c2=0
    for i in range(len(l1)):
        if l1[i] > l2[i]:
            c1+=1
        elif l1[i] < l2[i]:
            c2+=1
    print([c1,c2])


        
l1=[17,28,30]
l2=[99,16,8]
comp_list(l1,l2)
    