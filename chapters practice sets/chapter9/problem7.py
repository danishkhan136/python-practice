# method1
line=1

with open("chapters practice sets/chapter9/log.txt") as f:
    line=f.readline()
    line=f.readline()

if ("python" in line):
    print(f"Yes python present. line no: {line}");
else:
    print("Noo");

# method2
with open("chapters practice sets/chapter9/log.txt") as f:
    lines=f.readlines()

lineno=1
for line in lines:
    if ("python" in line):
        print(f"Yes python present. line no: {lineno}");
        break;
    lineno +=1

else:
    print("Noo");