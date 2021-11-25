#24. Find biggest of 3 numbers entered.
a=int(input("Enter the 1st no :"))
b=int(input("Enter the 2nd no :"))
c=int(input("Enter the 3rd no :"))
if(a>b>c):
    print("a is greater ",a)
elif(b>a>c):
    print("b is greater")
else:
    print("c is greater")
