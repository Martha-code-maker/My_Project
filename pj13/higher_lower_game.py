from art import logo,vs
from game_data import data
#from replit import clear
import random 

def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"
    
def compare(guess,A_followers, B_followers):
    if A_followers > B_followers:
        return guess == 'a'
    elif A_followers < B_followers:
        return guess == 'b'
        
  
print(logo)
score = 0
game_continue = True
B = random.choice(data)

while game_continue: 
    A = B
    B = random.choice(data)
    if A == B:
        B = random.choice(data)
    
    
    
    print(f"Compare A: {format_data(A)}")
    print(vs)
    print(f"Against B: {format_data(B)}")
    
    guess = input("Who has more followers? Type 'A' or 'B': ")
    guess.lower()

    A_follower = A["follower_count"]
    B_follower = B["follower_count"]

    is_correct = compare(guess, A_follower, B_follower)
    
    #clear()
    print(logo)
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
        
    else:
        game_continue = False
        print(f"Sorry, that's wrong.Final score: {score}")
        
        
