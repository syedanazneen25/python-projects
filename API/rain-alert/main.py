parameters ={
    "appid": "adc5c38a17ecd658e406095e22571862",
    "lat": 37.4316,
    "lon": -78.6569,
    "cnt": 4
}
import requests
from twilio.rest import Client
api_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
api_key_token = "dxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
account_sid = "ACxxxxxxxxxxxxxxxxxxxxxxxxxxx"
auth_token = "axxxxxxxxxxxxxxxxxxxxxxxxxxx"


response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast?", params=parameters)
response.raise_for_status()
print(response)
data = response.json()
weather_list = data['list']
weather_id = []

for i in range(4):
    id = weather_list[i]['weather'][0]['id']
    weather_id.append(id)
print(weather_id)
rain = False
for id in weather_id:
    if id < 700:
        rain = True
if rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
            body= "It's going to rain. Don't forget to bring an ☔",
            from_= '+10000000000000000', 
            to= '+14000000000000000'
        )
print(message.status)


