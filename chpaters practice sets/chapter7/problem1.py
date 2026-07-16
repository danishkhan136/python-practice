n=int(input("enter a number :"))

# for i in range(1,11):
#     print(f"{n} X {i} = {n*i}");

i=0
while(i<11):
    print(f"{n} X {i} = {n*i}");
    i+=1


for i in range(2,n):
    if(n%i == 0):
        print("number is not prime");
else:
    print("number is prime ");