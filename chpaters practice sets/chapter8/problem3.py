# def sum(n):
#     if(n==1):
#         return 1
#     return sum(n-1)+n;

# print(sum(10));

def rem(l,word):
    n=[]
    for item in l:
        if not (item == word):
            n.append(item.strip(word))
    return n 

l = ["harry","rohan","Shubam","an"]

print(rem(l,"an"));