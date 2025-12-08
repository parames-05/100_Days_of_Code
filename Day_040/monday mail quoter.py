import datetime as dt
import smtplib
import random as rrr

EMAIL = "abc@gmail.com"
PASS= "Enter_Your_App_Password_Here"
TO_EMAIL= "abc@gmail.com"
now= dt.datetime.now()
week_day = now.weekday()
with open("quotes.txt","r",encoding='utf-8') as file:
    data = list(file.readlines())
    choiceee = str(rrr.choice(data).strip())
    if week_day == 0:
        with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(user = EMAIL,password=PASS)
            connection.sendmail(from_addr=EMAIL,
                                to_addrs= TO_EMAIL,
                                msg= f"subject:Monday Wisher \n\n {choiceee} ")


















