#Task: Create a simplified Black Jack Game

import art, random

#Set list of card values, does not change
CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#function to add card to list
def deal_card():
    return CARDS[random.randint(0, len(CARDS)-1)]

#function to add values in list and retun total score
def get_score(all_cards):
    score = 0
    for value in all_cards:
        score += value
    return score

#function to check if the dealer has less than 17 cards and if so to add a card, 
# add new card to score and retun value
def check_dealers_hand(dealers_score):
    if dealers_score < 17:
        dealer.append(deal_card())
        dealers_score = get_score(all_cards=dealer)
    return dealers_score

#function to check if there is an ace in hand and to count it as 1 if hand is over 21
def check_ace(score, cards):
    if score > 21 and 11 in cards:
        score -= 10
    return score

#functions to check the scores and print winner
def final_scores(player_score, dealers_score):
    dealers_score= check_dealers_hand(dealers_score=dealers_score)
    dealers_score = check_ace(score=dealers_score, cards=dealer)
    player_score = check_ace(score=player_score, cards=player)

    result = ""
    
    if dealers_score == 21:
        result == "You Lose!"
    elif player_score == 21:
        result = "You Win!"
    elif dealers_score > 21:
        result = "Dealer's BUST! You Win!"
    elif player_score > 21:
        result = "BUST! You Lose!"
    elif player_score == dealers_score:
        result = "You Draw!"
    elif player_score > dealers_score :
        result = "You got more than the dealer! You Win!"
    elif dealers_score > player_score:
        result = "Dealer has more than you! You Lose!"

    print(f"\n\n\nYour final hand: {player}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer}, final score: {dealers_score}")
    print(f"{result}\n\n\n")

#fucntion to play black jack
def blackjack(dealer, player):
    print("\n"*100)
    print(art.logo)

    Game_on = True

    while Game_on:
        player_score = get_score(all_cards=player)
        dealers_score = get_score(all_cards=dealer)
        
        print(f"Your Cards: {player}, current score: {player_score}")
        print(f"Dealer's first card: {dealer[0]}")

        if player_score >= 21 or dealers_score >= 21:
            final_scores(player_score=player_score, dealers_score=dealers_score)
            return
        else:
            hit = input("\nType 'y' to get another card, type 'n' to pass: ")
            if hit == "y":
                player.append(deal_card())
            elif hit == "n":
                final_scores(player_score=player_score, dealers_score=dealers_score)
                Game_on = False
            else:
                print("\nError: Incorrect Input!\nEnd Game")
                final_scores(player_score=player_score, dealers_score=dealers_score)
                Game_on = False

#start the game, and clear lists when new games start
game = True
while game:
    play_game = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play_game == "y":

        dealer = []
        player = []

        dealer.clear
        player.clear

        dealer.append(deal_card())
        dealer.append(deal_card())

        player.append(deal_card())
        player.append(deal_card())

        blackjack(dealer=dealer, player=player)
        
        '''
        #test case 1: dealer=13, player=24
        # score: dealer = 13+card, player = 14
        dealer = [11, 3]
        player = [11, 5, 8]
        blackjack(dealer=dealer, player=player)
        '''
    elif play_game == "n":
        game = False
    else:
        print("\nERROR: Incorrect Input!\n")

        