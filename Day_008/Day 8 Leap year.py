year= int(input("Enter a year: \n"))
if (year%4==0 and year %100!=0) or year%400==0:
    print(f"The given year {year} is a leap year")
else:
    print(f"The given year {year} is not a leap year")