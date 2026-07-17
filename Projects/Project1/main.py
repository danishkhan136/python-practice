import random
'''
1 snake
2 water
0 gun

'''

computer = random.choice([0,1,2])
youstr = input("enrer your choice : ");
youDict = { "s" : 1,"w": 2,"g": 0}
reversedDict = {1 : "Snake" , 2 : "Water" , 0 : "Gun"}

you= youDict[youstr];

print(f"Computer Chose {reversedDict[computer]} \n You Chose {reversedDict[you]}")

if(computer == you):
    print("ITS A DRAW")
else:
    if(computer == 0 and you == 2):
        print("You Lose!")
    elif(computer == 0 and you == 1):
        print("You Win!")
    elif(computer == 1 and you == 2):
        print("You Lose!")
    elif(computer == 1 and you == 0):
        print("You Win!")
    elif(computer == 2 and you == 1):
        print("You Win!")
    elif(computer == 2 and you == 0):
        print("You Lose!")
    else:
        print("something went wrong")