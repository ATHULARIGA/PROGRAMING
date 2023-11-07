def sep_num_chr():
    chr=[]
    num=[]
    l=[1,'f',2,'b',3,4,'h','j',6,9,0,'k']
    for i in l:
        
        if str(i).isalpha()==True:
            chr.append(i)
        if str(i).isnumeric()==True:
            num.append(i)
    print("num list:",num)
    print("chr list:",chr)
    

sep_num_chr()