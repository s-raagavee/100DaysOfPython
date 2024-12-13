#TASK: Create 2 levels: Easy (10 lives) or hard (5 lives).
# User has to guess randomly generated number.
# Output whether number is too high or too low

import art, random

print(art.logo)

#welcome message
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")

def play(lives):
    num = random.randint(1, 100)

    while lives != 0:
        print(f"\nYou have {lives} attempts to guess the number!")
        guess = input("Make a guess: ")

        #Check guess against computer's number
        if int(guess) == num:
            print(art.win)
            print(f"You guessed the right number, it was {num}\n")
            return
        elif int(guess) > num:
            print("Your guess is too high!")
            lives -= 1
        elif int(guess) < num:
            print("Your guess is too low!")
            lives -= 1
        else:
            print("Wrong input!")
            lives -= 1
    if lives == 0:
        print(art.lose)
        print("YOU LOSE!\nYou ran out of guesss!\n")


#User chooses difficulty
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
lives = 0
if level == "easy":
    lives = 10
    play(lives)
elif level == "hard":
    lives = 5
    play(lives)