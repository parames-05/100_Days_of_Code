height = float(input("Enter Your height (in meters): "))
Weight = float(input("Enter your Weight (in kg): "))
bmi_calc = float((Weight/(height**2)))
bmi=round(bmi_calc,2)
if bmi < 18.5:
    print(f"Your BMI rating is {bmi}. You are underweight")
elif bmi>=18.5 and bmi<25:
    print(f"Your BMI rating is {bmi}. You are normal")
elif bmi >= 25 and bmi <30.0:
    print(f"Your BMI rating is {bmi}. You are Overweight")
else:
    print(f"Your BMI rating is {bmi}. You are Obese")
