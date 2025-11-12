print("Hello User!...This is a Py program built to calculate tip")
amt=float(input("Enter the bill amount: "))
tip_percent = int(input("Are you willing to tip 5%, 8% or 12%? "))
if tip_percent==5:
    tip = round(float((5/100)*amt),2)
    print(f"The tip amount to pay is ₹ {tip} ")
elif tip_percent==8:
    tip = round(float((8 / 100) * amt),2)
    print(f"The tip amount to pay is ₹ {tip}")
else:
    tip = round(float((12/100) * amt),2)
    print(f"The tip amount to pay is ₹ {tip} ")