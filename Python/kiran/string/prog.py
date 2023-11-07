def reach_shore(s):
    l=0
    down=0
    count=0
    for i in range(len(s)):
        
        if s[i]=="u":
            l+=1
        if s[i]=="d":
            l-=1
        
        # if l>0 and s[i]=="d" :
        #    pass
        if l ==0 and s[i]=="u":
            count+=1

            
               
        

        
    print(count)

        



s=input("enter str:").lower()
reach_shore(s)