print("welcome to Tresure Island.")
print("Your mission is to find the treasure.")
choice1 = input("You're at a crossroad, where do you want to go? type 'left' or 'right'.").lower()

if choice1 =="left":
    choice2=input("you've come to a lake. There is an island in the middle of the lake. type 'wait' to wait for a boat. Type 'swim' to swim across.").lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. there is a house with 3 doors. one red, one yellow and blue. Which color do you choose?").lower()
        if choice3=="red":
            print("it's a oom full of fire. Game over.")
        elif choice3 =="yellow":
            print("you found the tresure! You win!")
        elif choice3 == "blue":
            print("you enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("you got attacked by an angry trout. Game over.")

else:
    print(" You fell into a hole. Game over")


