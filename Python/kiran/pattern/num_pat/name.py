def name(n):
    for i in range(n):
        for j in range(n+1):
            if  i==0 or j==0 or j==5 or i==2:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        for i in range(n):
            print(" ", end=" ")
        for i in range(n):
            for j in range(n+1):
                if i==0  :
                    print("+", end=" ")
                else:
                    print(" ", end=" ")
                
        # for i in range(n):
        #     for  j in range(n+1):
        #         if   j==6  or i==0:
        #             print("*", end=" ")
        #         else:
        #             print(" ", end=" ")
            
    
        
        
        print()
    # print("----------------------------------")
    # for i in range(n+1):
    #     for j in range(n):
    #         if   j==2  or i==0:
    #             print("*", end=" ")
    #         else:
    #             print(" ", end=" ")
    #     print()
    # print("------------------------------------")
    # for i in range(n+1):
    #     for j in range(n):
    #         if   j==0 or j==4  or i==3:
    #             print("*", end=" ")
    #         else:
    #             print(" ", end=" ")
    #     print()
    # print("------------------------------------")
    # for i in range(n+1):
    #     for j in range(n):
    #         if   j==0 or j==4 or i==5:
    #             print("*", end=" ")
    #         else:
    #             print(" ", end=" ")
    #     print()
    # print("------------------------------------")
    # for i in range(n+1):
    #     for j in range(n):
    #         if   j==0 or i==5:
    #             print("*", end=" ")
    #         else:
    #             print(" ", end=" ")
    #     print()
    # print("------------------------------------")
    # print()
    
name(5)
