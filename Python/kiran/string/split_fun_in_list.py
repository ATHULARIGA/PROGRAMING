str="india is my home"
list=str.split(" ")
# for i in list:
#     print(i[::-1],end=" ")
# print()
# print("----------------------")
for i in range(len(list)-1,-1,-1):
    word=list[i]
    for j in range(len(word)):
        if j==0 or j==len(word)-1:
            first_char=chr((ord(word[j]))-32)
            print(first_char,end="")
        else:
            print(word[j],end="")
    print(end=" ")



            