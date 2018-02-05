#a simple two dice rolling game, based on random module.
import random

def roll(sides=36):
    number_rolled = random.randint(1,sides)
    return number_rolled

def main():
    sides=36
    rolling = True
    while rolling:
        roll_again = input("Yes=Press Any Keys than Q. No=Enter the word Q.")
        if roll_again.lower() !="q":
            number_rolled = roll(sides)
            print("You rolled a total of",number_rolled)
        else:
            rolling = False
    print("Thanks for playing")

main()