import smtplib
import requests
from datetime import datetime

LAT = 37.090240
LONG = -95.712891

# Get the current ISS location
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
iss_latitude = float(data['iss_position']['latitude'])
iss_longitude = float(data['iss_position']['longitude'])

# Check if ISS is within a 5-degree range of the specified location
def latlng_check():
    return (LAT - 5) <= iss_latitude <= (LAT + 5) and (LONG - 5) <= iss_longitude <= (LONG + 5)

# Get sunrise and sunset times for the given location
parameters = {
    "lat": LAT,
    "lng": LONG,
    "formatted": 0 
}

sun_response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
sun_response.raise_for_status()
data = sun_response.json()

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

print(f"Sunrise: {sunrise}, Sunset: {sunset}")

# Get the current time
time_now = datetime.now()
current_hour = time_now.hour

# Email credentials (use environment variables in production)
my_email = "sender@gmail.com"
password = "password"

# If the ISS is nearby and it's daytime, send an email
if latlng_check():
    if current_hour < sunrise or current_hour > sunset:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="receiver@gmail.com",
                msg=f"Subject: Look Up Now!!\n\nHello!\nThe ISS is visible in your area right now. Look up to spot it!"
            )
        print("Email sent!")
    else:
        print("The ISS is nearby, but it's not nighttime.")
else:
    print("The ISS is not in range.")

