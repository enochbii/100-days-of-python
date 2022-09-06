#step 1

import random


word_list = ["ardvark", "baboon","camel"]

#TO DO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)
print(f'Psst, the solution is {chosen_word}.')

#TO DO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#step 2
# To Do-2: - loop through each position in the chosen_word:
#if the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g If the user guessed "p" and the chosen word was "apple", then display should be ["_","p","_","_"].
display=[]
word_length= len(chosen_word)
for _ in range(word_length):
    display+="_"
print(display)

end_of_game= False

while not end_of_game:
    guess = input("guess  a letter ").lower()

    #TO DO 3 - check if the letter the user guessed (guess) is one of the letters in the chosen_word

    #step 3
    #To Do 3: - print "display" and you should see the guessed letter in the correct position and every other letter replace with "_".
    #Hint - Don't worry about gettin the user to guess the next letter. We'll tackle that in step3.
    for position in range(word_length):
        char=chosen_word[position]
        print(f"Current position: {position}\n Current letter: {char}\n Guessed letter: {guess}")
        if char==guess:
            display[position]=char

   

    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game= True
        print("you win")
    