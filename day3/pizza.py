print("welcome to python pizza Deliveries!")
size=input("what size pizza do you want? s,m, or l ")
pepperoni= input("do you want pepperoni? Y or N ")

extra_cheese= input("do you want extra cheese? Y or N ")

bill =0 
if size =='s':
    bill=15
    if pepperoni=='Y':
        bill+=2
    if extra_cheese=='Y':
        bill+=1

  
elif size =='m':
    bill=20
    if pepperoni=='Y':
        bill+=3
    if extra_cheese=='Y':
        bill+=1
elif size=='l':
    bill=25
    if pepperoni=='Y':
        bill+=3
    if extra_cheese=='Y':
        bill+=1

print(f"your final bill is $ {bill}")






