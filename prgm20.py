a= int(input("Enter the current year:"))
b= int(input("Enter the  final year:"))
print("The leap year from year",a,"to",b,"are :" )
for numbers in range(a,b):
   if(numbers % 4 == 0) and (numbers %100!= 0) or (numbers % 400 ==0):
      print(numbers)