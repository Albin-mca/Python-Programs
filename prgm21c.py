#21.List comprehensions
#(c) Form a list of vowels selected from a given word
a = input("Enter the word : ")
vowels =['a','e','i','o','u']
list1=[]
for x in a:
    if (x in vowels and x not in list1):
        list1.append(x)
print("Vowels present in the word :",list1)