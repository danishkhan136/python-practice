import random

def game():
    print("You are playiinfg the game ...");
    score = random.randint(1, 92);
    with open ("chapters practice sets/chapter9/hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"Your score: {score}")
    if(score>hiscore):
        with open ("chapters practice sets/chapter9/hiscore.txt", "w") as f:
            f.write(str(score));

    return score

game()