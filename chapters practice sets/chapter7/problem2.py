# n = int(input("Enter the number : "));
# i=1
# sum=0
# while(i<=n):
#     sum += i;
#     i +=1;
# print(sum);

# n = int(input("Enter the number : "));
# product =1
# for i in range(1,n+1):
#     product = product*i
# print(product);

n = int(input("Enter the number : "));
# for i in range(1,n+1):
#     print(" "*(n-i), end="");
#     print("*"*(2*i-1),end="")
#     print("")

# for i in range(1,n+1):
#     print(" "*(n-i), end="");
#     print("*"*i,end="")
#     print("")

for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"* n,end="");
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
    print(" ")


n=int(input("enter a number :"))

for i in range(1,11):
    print(f"{n} X {11-i} = {n*(11-i)}");
    
    