def patt(num):
  k=5
  for i in range(num):
    p=k
    q=k
    for j in range(i,num+1):
      print(" ",end=" ")
    for j in range(i+1):
        print(p,end=" ")
        p+=1
    for j in range(i):
        print(p-2,end=" ")
        p-=1
      
    k-=1

    print()

patt(5)

#         5 
#       4 5 4 
#     3 4 5 4 3 
#   2 3 4 5 4 3 2 
# 1 2 3 4 5 4 3 2 1 