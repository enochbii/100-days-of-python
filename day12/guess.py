from random import randint
from art import logo 

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0
#Function to check the user's guess against actual answer.
def check_answer(guess, answer,turns):
    """check  answer against guess, return the number of guess"""
    if guess >answer:
        print("Too high.")
        return turns-1
    elif guess <answer:
        print("Too low.")
        return turns-1
    else:
        print(f"You got it! The answer was {answer}")

#make a function to set difficulty.
def set_difficulty():
    level=input("choose a difficulty. Type 'easy' or 'hard': ")
    if level =="easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS



#choosing a random number between 1 and 100.
def game():
    print(logo)
    print("welcome to the guesing game")
    print("I'm thinking of a  number between 1 and 100. ")
    answer= randint(1,100)
    print(f"Pssst, the correct answer is {answer}")
    turns = set_difficulty()


    #reapeat this guessing functionality if they get it wrong.
    guess=0

    while guess !=answer:
        print(f"You have {turns} attempts remaining to guess the number .")
        #let the user guess the number
        guess = int(input("make a guess: "))
        
        #Track the number of turns and reduce by 1 of the get wrong.
        turns= check_answer(guess,answer,turns)
        if turns == 0:
            print("You've run out guesses, you lose.")
            return
        elif guess != answer:
            print("guess again.")

game()


