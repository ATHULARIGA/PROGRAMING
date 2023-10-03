def reverse(word):
    rev=""
    for i in word:
        rev=i+rev
    return rev
str1="apple is red"
newstr=str1.split(" ")
ans=""
for i in range(len(newstr)):
    word=newstr[i]
    if i==len(newstr)-1:
        word1=word.capitalize()
        res=reverse(word1)
        size=len(res)
        ans=ans+(res+str(size))
    else:
        res=reverse(word)
        size=len(res)
        ans=ans+(res+str(size))


print(ans)


