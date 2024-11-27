#Task: 

#print welcome message
print("Hello Treasure Seeker!\nWelcome to the treasure Island!\nMake good choices to find that treasure!\nGOOD LUCK!\n\n\n")

print("You enter the forest.")

#get user input to see if they want to go left or right, and use it to check conditions
direction = input("You are at a cross road!\nDo you want to turn left or right?\nType 'L' for Left or 'R' for Right\n")
print(f"\nYou have chosen to go {direction}")
if direction == 'R':
    print("You keep walking until you reach the river.")

    #get user input to see if they want to swim or wait, and use it to check conditons
    action = input("Do you want to swim across or wait for a boat?\nType 'S'to Swim or 'W'to Wait\n")
    print(f"\nYou have chosen to {action}")
    if action == 'W':
        print("The boat arrives 10 minutes later")

        #get user input to see which door they want to enter, and use it to check conditions
        door = input("You arrive infront of 3 doors. Yellow, Blue and Red.\nWhich door do you want to go through?\nType 'Y'for Yellow, 'B' for Blue or 'R'for Red\n")
        if door == 'Y':
            print("\nYou chose the yellow door.")
            print("You were instantly electrocuted and died!\nGAME OVER")

        elif door == 'B':
            print("\nYou chose the blue door.")
            print("You found the treasure! CONGRATULATIONS!!\nYOU WON!")

        elif door == 'R':
            print("\nYou chose the red door.")
            print("You were chased by a swarm of bees over a cliff! you fell to your death!\nGAME OVER")

        else:
            print(f"\nYou chose the {door} door.")
            print("That door doesnt exist!!\nGAME OVER")

    elif action == 'S':
        print("You start swimming across the river\nGIANT leeches appear and attack you! You Drowned!\nGAME OVER!")

    else:
        print("You can't do that!\nGAME OVER!")

elif direction == 'L':
    print("You walked into a cave where a bear attacked and ate you!!\nGAME OVER!")

else:
    print("You can't go that way!\nGAME OVER!")