#22. Get a string from an input string where all occurrences of first character replaced with ‘$’,
#except first character.
a=str.lower(input("Enter the string :"))
b=a[0]
a=a.replace(b,"$")
a=b+a[1:]
print(a)
