import random

# random_integer = random.randint(1,10)
# print(random_integer)

# random_float = random.random()
# print(random_float)

# love_score = random.randint(1,100)
# print(f"Your love score is {love_score}")
names_string = input ("Give me everybody's names, seperated by a comma. ")
names = names_string.split(",")
#get the total number of the list.
num_items = len(names)
 
random_choice = random.randint(0,num_items-1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + "is going to buy the meal today.")