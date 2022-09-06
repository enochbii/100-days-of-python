import random

letters = ['A', 'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

print("welcome to the Pypassword Generator!")
nr_letters =int(input("How many letters would you like in your password?\n"))
nr_symbols= int(input("how many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#eazy level
password = ""
#nr_letters
for char in range(1,nr_letters+1):
    #1-4
    password+=random.choice(letters)

for char in range(1,nr_symbols+1):
    password+=random.choice(symbols)

for char in range(1,nr_numbers+1):
    password+=random.choice(numbers)

print(password)

#hard level
# password_list=[]
# #nr_letters
# for char in range(1,nr_letters+1):
#     #1-4
#     password_list+=random.choice(letters)

# for char in range(1,nr_symbols+1):
#     password_list+=random.choice(symbols)

# for char in range(1,nr_numbers+1):
#     password_list+=random.choice(numbers)

# print(password_list)

# password = " "
# for char in password_list:
#     password +=char



