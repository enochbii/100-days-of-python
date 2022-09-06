weight = float(input("what is your weight in kg?"))
height = float(input("what is your height in cm?"))
bmi=weight/height**2
new_bmi=round(bmi)

if new_bmi<18.5:
    print(f"your BMI is {new_bmi}, you are slightly underweight.")
elif new_bmi<25:
    print(f"Your BMI is {new_bmi}, you have normal weight.")
elif new_bmi<30:
    print(f"your BMI is {new_bmi}, you are slightly overweight.")
elif new_bmi<35:
    print(f"your BMI is {new_bmi}, you are obese.")
else:
    print(f"your BMI is {new_bmi}, you are clinically obese.")