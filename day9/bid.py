

#HINT: You can call clear() to clear the output in the console.


from art import logo
print(logo)

bids={}
no_user=False


def highest_bidder(bidder):
  highest_bid=0
  winner=0
  #bidder={"james":123, "enock":321}
  for bid in bidder:
    amount_bid=bidder[bid]
    if amount_bid>highest_bid:
      highest_bid=amount_bid
      winner=bid

  print(f"the highest bid is ${amount_bid}, and the winner is {winner}")
  




while not no_user:
  name=input("what is your name?: ")
  price= int(input("what is your bidding price? $"))
  bids[name]=price
  should_bid=input("Is there other person who wants to bid? Type 'yes' or 'no'.\n")
  if should_bid=="no":
    no_user=True
    highest_bidder(bids)
  elif should_bid=="yes":
    pass

