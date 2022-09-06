3+5
7-4

3*2
# print(type(6/3))
# print(2**3)

# print(3*(3+3)/3-3)
height = input("enter your height in m:")
weight = input("enter your weight in kg: ")

new_weight=float(weight)
new_height = float(height)
bmi= new_weight/new_height**2
new_bmi=round(bmi)
print(new_bmi)