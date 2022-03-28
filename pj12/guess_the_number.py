#Number Guessing Game Objectives:

from art import logo
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
turns = 0

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    level.lower()
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def play_game():  
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    answer = random.randint(1,100)
    turns = set_difficulty()
    print(f"testnumber : {answer}")
    print(f"You have {turns} attempts remaining to guess the number.")

    guess = 0
    while answer != guess:
        guess = int(input("Make a guess: "))
        turns = check_answer(answer,guess,turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return 


def check_answer(answer,guess_number,turns):
    if answer < guess_number:
        print("Too high.")
        return turns- 1
    elif answer > guess_number:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {guess_number}.")
        

    

play_game()