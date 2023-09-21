def num_patt(n):
    for i in range(n):
        for j in range(i,n):
            print(" ",end=" ")
        for j in range(i+1):
            if i%2==0:
                print("#",end=" ")
            if i%2!=0:
                print("$",end=" ")
        for j in range(i):
            if i%2==0:
                print("#",end=" ")
            if i%2!=0:
                print("$",end=" ")
        print()
num_patt(5)

#           # 
#         $ $ $
#       # # # # #
#     $ $ $ $ $ $ $
#   # # # # # # # # #