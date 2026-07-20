words = ["donkey","bad","ganda"];

with open("chapters practice sets/chapter9/file.txt", "r") as f:
    content = f.read();
for word in words:
    content = content.replace(word,"#"*len(word))


with open("chapters practice sets/chapter9/file.txt", "w") as f:
    f.write(content);
