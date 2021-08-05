import random

number = random.randint(1,9)
chance = 0

while chance < 5:
    guess = int(input("What is your guess?:-"))

    if guess == number:
        print("YOU WIN!")

    else:
        chance = chance + 1

    if not chance < 5:
        print("YOU LOSE!" + "The number is", number)