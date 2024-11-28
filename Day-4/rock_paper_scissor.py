#Task: Create a rock paper scissors games between the user and computer

import random

#Images to print for rock, paper, scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Store images and play in lists
images = [rock, paper, scissors]
hand = ["Rock", "Paper", "Scissors"]

#Welcome Message
print("Welcome to game of Rock, Paper, or Scissors!\n\n")

#get user input as int
user = int(input("What would you like to play?\nType '0' for Rock,'1' for Papper, or '2' for Scissors!\n"))

#check if user inputted correct options
if user <= 2:
    #get computer input
    comp = random.randint(0,2)

    #print images
    print(f"\nYou Picked {hand[user]}:\n{images[user]}\n\n")
    print(f"The computer picked {hand[comp]}:\n{images[comp]}\n")

    #compare user and comp to find winner
    #draw
    if user == comp:
        print("YOU DRAW!\n")
    #user wins
    elif (user == 1 and comp == 0) or (user == 2 and comp == 1) or (user == 0 and comp == 2):
        print("YOU WIN!\n")
    #user loses
    elif (comp == 0 and user == 2) or (comp == 1 and user == 0) or (comp == 2 and user == 1):
        print("YOU LOSE!\n")
else:
    print("INCORRECT INPUT!")