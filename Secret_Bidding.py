
bid = {}

cond = True
while(cond):
    name = input("Enter your name: ")
    amount = int(input("Enter your bidding amount: "))
    bid[name] = amount
    choice = input("Are there more bidder? (y / n): ")
    if(choice.lower() == "y"):
        cond = True
    elif(choice.lower() == "n"):
        cond = False
    else:
        cond = False


for key in bid:
    winner_amount = 0
    if(bid[key] > winner_amount ):
        winner_amount = bid[key]
        winner_name = key

print(f"{winner_name} won the bidding with bidding amount of {winner_amount}")