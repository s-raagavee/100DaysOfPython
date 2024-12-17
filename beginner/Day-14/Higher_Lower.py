#TASK: Create the higher or lower game. Using the data in 'game_data.py'
# present the user with 2 celebrities and ask them to choose who has more followers
# If the user gets it correct, add a point to the score and use the second option to compare
# to another celebrity
#if they get it wrong the game ends and their final score is printed

import art, random, game_data
GAME_DATA = game_data.data

print(f"\n"*100)
print(art.logo)

#return string of data
def get_data(index):
    return f"{index['name']}, a {index['description']}, from {index['country']}"

#return number of followers
def get_followers(index):
    return index['follower_count']

#compare and return who has more followers
def compare_followers(a, b):
    if get_followers(a) > get_followers(b):
        return 0
    return 1  

#make sure B data is not the same as A data
def check_same_data(b):
    b_equals_a = True
    while b_equals_a:
        if b==a:
            b = GAME_DATA[random.randint(0, len(GAME_DATA)-1)]
        else:
            b_equals_a = False
    return b

#Starting Score = 0
score = 0

#random data
a = GAME_DATA[random.randint(0, len(GAME_DATA)-1)]
b = GAME_DATA[random.randint(0, len(GAME_DATA)-1)]

#list to store the 2 data to compare
compare_data = [a, b]

game_on = True
while game_on:
    
    b = check_same_data(b=b)

    print(f"Compare A: {get_data(a)}")
    print(art.vs)
    print(f"Against B: {get_data(b)}")

    #Winner
    winner = compare_followers(a, b)
    winner_data = compare_data[winner]

    #get users answer
    user_ans = input("Who has more followers? Type 'A' or 'B': ").lower()
    user_ans_num = 2

    #save answers as numbers to represent index in 'compare_data' list
    if user_ans == "a":
        user_ans_num = 0
    elif user_ans == "b":
        user_ans_num = 1

    #Check if user has the correct answer
    #yes, add point, no, end game and print score
    if user_ans_num == winner:
        score += 1
        print(f"\n"*100)
        print(art.logo)
        print(f"You are right! Current Score: {score}")

        #swap winner to A
        a = winner_data
        b = GAME_DATA[random.randint(0, len(GAME_DATA)-1)]
    else:
        print(f"\n"*100)
        print(art.logo)
        print(f"Sorry, That is wrong. Final Score: {score}")
        game_on = False