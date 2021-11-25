#21.List comprehensions
#(d) List ordinal value of each element of a word (Hint:use ord() to get ordinal values)
list1=["a,b,c,d","ghij","1234"]
print(list1)
for i in list1:
    for j in i:
        value=ord(j)
        print(value)