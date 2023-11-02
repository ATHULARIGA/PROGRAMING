def freq(str1,key):
    count=0
    
    for i in range(len(str1)):
        if key==str1[i:i+len(key)]:
            count+=1
    print(count)


str1="abcbdidbbcb"
key="bcb"
freq(str1,key)
