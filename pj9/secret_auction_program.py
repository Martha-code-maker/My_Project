#from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret auction program.")

auction = True
info = {}
def find_highest_bidder(bidder_record):
  highest_bid = 0
  for key in info:
    bid_amount = info[key]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = key
  print(f"The winner is {winner} with a bid of ${highest_bid}") 
  
while auction:

  bidder = input("What is your name?: ")
  cost = int(input("What's your bid? $"))
  info[bidder] = cost
 
  other_bidder = input("Are there any other bidders? Type 'yes' or 'no'.")
  other_bidder.lower()
  if other_bidder == 'yes':
    #clear()
    continue
  else:
    #clear()
    find_highest_bidder(info)
    auction = False
  
  
  