num=int(input("enter number: "))
res=0
count=0
while(num>0):
    num=num//10
    count+=1
print(count)
# def count_no(num):
#     count=0
#     while num>0:
#         rem=num%10
#         num=num//10
#         count+=1
#     return count
# num=int(input("Number is:"))
# print(count_no(num))
# count_no(num)
