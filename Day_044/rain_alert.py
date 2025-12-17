import requests
from twilio.rest import Client

API_URL = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "Enter Your API Key Here"
account_sid = "ACCOUNT ID"
auth_token = "Authentication_Key"

parameters = {"lat" :10.997093,
              "lon" :77.017583,
              "cnt" :4,
              "appid" : API_KEY}
response = requests.get(API_URL,params=parameters)
response.raise_for_status()
data=response.json()
WILL_RAIN = False
for hour_data in data["list"]:
    condition_code= hour_data["weather"][0]["id"]
    descrip = hour_data["weather"][0]["description"]
    print(condition_code,descrip)
    if int(condition_code) < 700:
        WILL_RAIN = True
if WILL_RAIN:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"Rain’s about to drop harder than exam results!🌧️☔",
        from_="Enter_your_Twilio_number_here",
        to="Enter_Your_Phone_Number_with_country_code",
    )
    print(message.status)


