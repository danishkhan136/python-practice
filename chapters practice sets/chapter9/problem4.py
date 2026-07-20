word = "donkey";

with open("chapters practice sets/chapter9/file.txt", "r") as f:
    content = f.read();

NewContent = content.replace(word,"######")

with open("chapters practice sets/chapter9/file.txt", "w") as f:
    f.write(NewContent);
