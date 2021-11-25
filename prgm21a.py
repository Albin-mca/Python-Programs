#21.List comprehensions
#(a) Generate positive list of numbers from a given list of integers
list1=[1,-2,3,-4,5,-6,7,-8,9,-10,11]
list2=[i for i in list1 if i>0]
print(list2)