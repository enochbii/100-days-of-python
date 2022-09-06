# import random

# random_side = random.randint(0,1)

# if random_side ==1:
#     print("heads")
# else:
#     print("tals")

# import random

# name_string = input("Give me everbody's names, separated by a comma. ")
# names = name_string.split(",")

# num=len(names)

# random_choice = random.randint(0, num-1)
# person_who_will_pay = names[random_choice]
# print(person_who_will_pay+" is going to buy the meal today.")




row1 = [" "," "," "]
row2 = [" "," "," "]
row3 = [" "," "," "]
map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position =input("where do you want to put the treasure?")

horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical -1]
selected_row[horizontal-1]="X"

print(f"{row1}\n{row2}\n{row3}")



