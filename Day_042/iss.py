import requests
import smtplib
import time
from datetime import datetime

MY_LAT = 10.997093  # Your latitude
MY_LONG = 70.017311  # Your longitude
MY_EMAIL = "abc@gmail.com"
MY_PASSWORD = "Enter_your_app_password_here"
TO_EMAIL = "abc@gmail.com"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Check if ISS is within +5 / -5 degrees of your position
    return (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5) and \
           (MY_LONG - 5) <= iss_longitude <= (MY_LONG + 5)


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.utcnow().hour

    return time_now >= sunset or time_now <= sunrise


while True:
    time.sleep(60)
    print("Checking \n")
    if is_iss_overhead() and is_night():
        print("ABOVE!!!!!!!")
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=TO_EMAIL,
                msg="Subject:Look Up!\n\nThe ISS is above you in the sky. 🚀"
            )