try:
    a = int(input("enter your number"))
    print(a)

except ValueError as v :
    print("heyy")
    print(v)

except Exception as e:
    print(e)


print("thank you")