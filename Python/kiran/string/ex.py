def ex(str2):
    a=""
    b=""
    c=""

    # str3=" "
    # for i in range(len(str2)):
        
        
    #     if str2[i]==" ":
    #         # print(str2[i:])
    #         # print(str2[:i])
    #         # print(str2[i+1:len(str2[:i]+" "+str2[:i])])
    #         # break
            
            
    #         if str2[:i]==str2[i+1:len(str2[:i]+" "+str2[:i])]:
    #             print(str2[i:])
    for i in str2:
        if i == " ":
            if a!=b:
                c+=a+" "
                b=a
                a=""
            else:
                a=""
        else:
            a+=i
    print(c)

                




str2="python python is python "
ex(str2)