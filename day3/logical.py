print("welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))

if height >=120:
    print("You can ride the rollercoaster!")
    age = int(input("what is yoir age? "))
    bill =0


    if age<12:
        bill=5
        print("Child tickets are $5")

    elif age <18:
        bill=7
        print("youth tickets are $7.")
    elif age>=45 and age<=55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill=12
        print("Adult tickets are  $12.")
    wants_photo=input("Do you want a phot taken? Y or N.")
    if wants_photo =="Y":
        bill += 3
    

    print(f"Your final bill is {bill}")
    

else:
    print("Sorry, you have to grow taller before you can ride.")
