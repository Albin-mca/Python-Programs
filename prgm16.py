#WAPT create a simple calculator performing only four basic operations
# program a simple calculator
a = int(input("Enter first Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Choose an operation:\n 1.Addition\n 2.Subtract\n 3.Multiply\n 4.Division\n Choose your option: "))
if(c==1):
    t = a+b
    print(" Sum= ",+t)
elif(c==2):
    t = a-b
    print(" Difference=", +t)
elif(c==3):
    t = a*b
    print(" Product= ", +t)
elif(c==4):
    t=a/b
    print(" division=", +t)
else:
    print("\n!!WARNING!! - Invalid option")

