f=open(r"C:\Users\Danish Khan\Desktop\python practice\chapters\chapter9\myfile.txt")

#for multiple lines
# lines = f.readlines();
# print(lines , type(lines));

#for single line
# line1 = f.readline();
# print(line1 , type(line1));

line = f.readline()
while(line != ""):
    print(line);
    line = f.readline()


f.close()