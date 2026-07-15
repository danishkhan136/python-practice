
#d={}#empty dictionary
marks={
    "harry": 65,
    "shubam" : 56,
    "ali" : 99
};

print(marks,type(marks));
print(marks["ali"]);
print(marks.items());
print(marks.keys());
print(marks.values());
marks.update({"harry":60, "renuka":79});
print(marks);
print(marks.get("harry"));
print(marks.get("sarry"));
print(marks["harry"]);
#print(marks.get("harry2"));#Prints none
#print(marks["harry2"]);#returns an error
print(len(marks));
