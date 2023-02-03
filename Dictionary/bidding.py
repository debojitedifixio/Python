import os
import art

# HINT: You can call clear() to clear the output in the console.
print(art.logo)
bid = {}
flag = True


def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bid:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while flag:
    name = input("What is your name?: ")
    price = int(input("What is your Bid?: $"))
    bid[name] = price
    should_continue = input("Do you want to enter a bid again? Press Yes or No").lower()
    if should_continue == "yes":
        os.system("cls")        # not clearing the screen
    elif should_continue == 'no':
        flag = False
        find_highest_bidder(bid)

