def num_to_str(n):
    newstr=" "
    # for i in n:
        
    #     for j in dict1.keys():
    #         i=int(i)
    #         if i==j:
                
    #             newstr+=dict1[j]
    # print(newstr)
    for i in n:
        newstr+=dict1[int(i)]
    return newstr
            
    
dict1={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",0:"zero"}

num=input("enter the no:")
print(num_to_str(num))

