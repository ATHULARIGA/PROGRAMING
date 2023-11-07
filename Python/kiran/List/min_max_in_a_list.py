def min_no(l):
    min=l[1]
    for i in range(len(l)):
       
        if l[i] < min:
            min=l[i]
    print(min)

l=[-1,-2,-10,-9,-20,-4]
min_no(l)