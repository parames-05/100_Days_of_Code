import smtplib
EMAIL = "abc@gmail.com"
PASS= "Enter_Your_App_Password"
TO_EMAIL= "abc@gmail.com"
with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(user = EMAIL,password=PASS)
            connection.sendmail(from_addr=EMAIL,
                                to_addrs= TO_EMAIL,
                                msg= f"subject: Email Automation \n\n This is an automatic mail generated and sent via python script ")


















