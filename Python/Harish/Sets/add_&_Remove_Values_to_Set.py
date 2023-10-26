# The code is creating an empty set `a` and then using a loop to ask the user to enter 5 values. Each
# value is added to the set using the `add()` method. After the loop, the set `a` is printed.
a=set()
for i in range(5):
    print("enter a value:")
    data=int(input())
    a.add(data)
print(a)
a.update([60,70,80])
print(a)

print("----------------------")
# The code is asking the user to enter a value to discard from the set `a`. The `discard()` method is
# then used to remove the specified value from the set. Finally, the updated set `a` is printed.


num=int(input("Enter a value to  discard:"))
a.discard(num)
print(a)