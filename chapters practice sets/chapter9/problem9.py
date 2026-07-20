with open("chapters practice sets/chapter9/this.txt") as f:
    content1 = f.read();
with open("chapters practice sets/chapter9/this_copy.txt") as f:
    content2= f.read();

if (content1 == content2):
    print("Yes these files are inditical");
else:
    print("Not identical")