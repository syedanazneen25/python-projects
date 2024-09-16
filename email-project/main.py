import smtplib
import datetime as dt
import random

with open("email-project/quotes.txt") as data:
    quotes = data.readlines()
daily_quote = random.choice(quotes)
my_email = "sender@gmail.com"
password = "password"
day = dt.datetime.now()
if day.weekday() == 0:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
       connection.starttls()
       connection.login(user=my_email, password=password)
       connection.sendmail(
         from_addr=my_email, 
            to_addrs="receiver@gmail.com", 
            msg=f"Subject: Monday Motivation\n\n Hello!\nHere's your Monday motivation to kick-start the week.\n{daily_quote}\nBye."
        )
    
