a = int (input("enter the number : "))
b = int (input("enter the number second : "))

if(b == 0):
    raise ZeroDivisionError("hey our program  is not meant to divide numbers with zero")
else:
    print(f"the division a/n is {a/b}")