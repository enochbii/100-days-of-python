programming_dictionary = {
    "Bug":"An error in a program that prevents the program from running as expected.", 
    "function":"A piece of code that you can easily call over and over again.",
    "loop":"The action of doing something over and over again.",
}

#retrieving items from dictionary
# print(programming_dictionary["function"])

#adding new items in dictionary

programming_dictionary["loop"]="The action of doing something over and over again."

# print(programming_dictionary)

empty_dict={}


#wipe an existing dict
# programming_dictionary={}
# print(programming_dictionary)

#editing an item in dictionary
programming_dictionary["Bug"]="a month in your computer"
# print(programming_dictionary)

#loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
