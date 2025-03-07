# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art
print(art.logo)

print("Welcome to the secret Auction.")

entry_book = {}

def highest_bidder(bidding_dict):
    highest_bid = 0
    winner = " "
    for bidder in bidding_dict:
        bid_amt = bidding_dict[bidder]
        if bid_amt> highest_bid:
            highest_bid = bid_amt
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while True:
    name = input("Please! Enter your Name:")
    price = int(input("Please! Enter your Bid: $"))
    entry_book[name]=price
    question = input("are there any bidders? Type 'yes' or 'no' ")
    if question=='yes':
        print("\n" *50)
    elif question== 'no':
        highest_bidder(entry_book)
        break
