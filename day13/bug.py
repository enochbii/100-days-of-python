################ Debugging ###############

##Describe Problem
# def my_function():
#     for i in range(1,21):
#         if i==20:
#             print("you got it")
# my_function()

## Reproduce the bug
# from random import randint

# dice_imgs =["1","2","3","4","5","6"]
# dice_num = randint(0,5)
# print(dice_imgs[dice_num])

# Play Computer
# year = int(input("what's your year of birth?"))
# if year > 1980 and year < 1994:
#      print("youare millenial.")
# elif year > 1994:
#      print("You are a gen z.")

# fix the error
# age = int(input("How old are you?"))
# if age>18:
#     print("You can drive at age {age}.")

## Print is your friend
# pages =0
# word_per_page = 0
# pages = int(input("number of pages: "))
# word_per_page = int(input("number of words per page: "))

# total_words = pages * word_per_page
# print(pages)
# print(word_per_page)
# print(total_words)

# use a Debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item =item * 2
        b_list.append(new_item)
    print(b_list)

mutate([1,2,3,5,8,13])


