#25. Accept a file name from user and print extension of that.
a=str(input("Enter the file name  with extension :\n"))
b=a.split(".")
print(repr(b[-1]))