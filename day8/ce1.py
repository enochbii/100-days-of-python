from pydoc import plain


alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("type the shift number:\n"))

#don't change the code above

#to do-1: Create a function called 'encrypt'  that takes the 'text' and 'shifts' as inputs.
def encrypt(plain_text,shift_amount):
    cipher_text=""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text +=new_letter
    print(f"the encoded text is {cipher_text}")

    
def decrypt(cipher_text,shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position=position - shift_amount
        plain_text +=alphabet[new_position]
    print(f"The decoded text is {plain_text}")

    #to do-2: inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text
    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output : "the encode text is mjqqt"shift

#to do-3: call the encrypt function and pass in the user inputs. You should be able to testthe code nd encrypt a message.

if direction=="encode":
    encrypt(plain_text=text,shift_amount=shift )

elif direction=="decode":
    decrypt(plain_text=text, shift_amount=shift)
