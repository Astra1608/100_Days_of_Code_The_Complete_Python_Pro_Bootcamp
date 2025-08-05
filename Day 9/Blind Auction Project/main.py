from art import logo
print(logo)
# dict[name:bid]= {"neha" : 123 , "angela": 234}
#we can also use function max(dict_name, key= dict_name.get)
def find_highest_bidder(bidding_dict):
    winner = ""
    for bidder in bidding_dict:
        highest_bid = 0
        bid_amount = bidding_dict[bidder]
        if bid_amount>highest_bid:
            highest_bid= bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
bidders = {}
is_bidder_left = True

while is_bidder_left:
    name = input("What is your name?")
    bid = int(input("What is your bid?: $"))
    bidders[name] = bid
    query = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if query=="no":
        is_bidder_left= False
        find_highest_bidder(bidders)
    elif query== "yes":
        print("\n" * 20)





