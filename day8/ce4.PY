alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def ceaser(start_text, shift_amount, cipher_direction):
    end_text=""
    if cipher_direction =="decode":
        shift_amount *=-1
    for char in start_text:

    #to do-3: what happens if the user enters a number/symbol/space?
    #can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text =  "meet me at 3"
    #end_text = "..... ... ..3"
  
    
#to do-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. otherwise type 'no'.
#If they type ' ye' then asl the, for the direction/text/shift again and call the ceasar() function again?
#Hint: Try creating a new function that calls itself if they type 'yes'.
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("type your message:\n").lower()

#to do-2: what if the user enters a shift that us greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Hint: think about how you can use the modulus (%).

# ceasar(start_text=text, shift_amount=shift, cipher_direction=direction)
