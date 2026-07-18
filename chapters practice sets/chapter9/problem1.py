f=open("chapters practice sets/chapter9/poem.txt")
content = f.read()
if("twinkle".lower() in content.lower()):
    print("Present");
else:
    print("Absent");
f.close()