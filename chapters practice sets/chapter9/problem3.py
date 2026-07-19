def generateTable(n):
    table = ""
    for i in range(1,11):
        table += f"{n} X {i} = {n*i}\n"
    
    with open(f"chapters practice sets/chapter9/tables/table_{n}.txt","w") as f:
        f.write(table)


for i in range (2,21):
    generateTable(i)