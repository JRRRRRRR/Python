# Number guessing game

import random

answer = random.randint(1,20)

chances = 3
success = False

for turn in range(chances):
    guess = int(input("Enter guess: "))
    if guess == answer:
        print("Cottect!")
        success = True
        break
    else:
        print("BZZZT! Wrong!")

if success == True:
    print("Congratulations!")
else:
    print("Sorry, the correct answer was ", answer)
