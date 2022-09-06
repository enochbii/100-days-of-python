import random 
test_seed = int(input("create a seed number: "))
random.seed(test_seed)

random_choice = random.randint(0,1)
if random_choice == 1:
    print("Heads")
else:
    print("Tails")