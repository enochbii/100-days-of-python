#choosing random number from 1 to 100
from logging import raiseExceptions
import random 
from art import logo

print(logo)

num = random.randint(1,100)
print(f"""
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Pssst, the correct answer is {num}
""")
a=input("choose a difficuty. Type 'easy' or 'hard': ")

#create a difficulty function 
def difficulty(a):
    if a == "hard":
        return 5
    elif a =="easy":
        return 10
  

attempts= difficulty(a)
print(f"You have {attempts} remaining to guess the number. ")


# create a guess function
def guess(a):
        if a>num:
            print("Too high")
            print("Guess again")
        elif a<num:
            print("Too low")
            print("Guess again")
        else:
            print(f"you got it! The answer was {num}")

gues=int(input("make a guess: "))
b=0
while b !=attempts and b!=num:
    guess(gues)






