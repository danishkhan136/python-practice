# def factorial(n):
#     if(n==1 or n==0):
#         return 1
#     return n*factorial(n-1)

# n= int(input("enter your number :"))
# print(f"the factorial of this number is {factorial(n)}")


def sum(n):
    if(n==1):
        return 1
    return sum(n-1)+n

print(sum(5));

