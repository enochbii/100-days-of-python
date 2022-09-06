import random


user_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors.\n"))

computer_choice = random.randint(0,2)
print(f"Computer chose {computer_choice}")

if user_choice ==0 and computer_choice==2:
    print("you lose!")
elif computer_choice > user_choice:
    print("you lose!")
elif user_choice > computer_choice:
    print("you win!")
elif computer_choice == user_choice:
    print("it's a draw")
else:
    print("You typed an invalid number, you lose!")