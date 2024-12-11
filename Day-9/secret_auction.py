#TASK: create a secret auction. Get all user's name and bid without the 
# other bidder seeing the previosu bidders bid.

import art

#function to compare bids, and print the winner
def compare_bids(bids):
    highest_bid = 0
    winner = ""

    for bidder in bids:
        bid_amount = bids[bidder]

        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
            
    print(f"\nThe winner is {winner} with a bid of ${highest_bid}")
    
print(art.logo)

all_bids = {}

#while loop for bidders to keep bidding until no more bids are needed
continue_auction = True
while continue_auction:
    name = input("\nWhat is your name?: ")
    bid = int(input("What is your bid?: $"))
    all_bids[name] = bid

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if more_bidders == "no":
        continue_auction = False
        compare_bids(bids=all_bids) #call compare bids method to print winner

    elif more_bidders == "yes":
        print("\n"*100)
