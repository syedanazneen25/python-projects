import pandas as pd  
import smtplib
import datetime as dt
import random

today = dt.datetime.now()
current_day = today.day
current_month = today.month

data = pd.read_csv("email-project/birthdays.csv")

birthdays_dict = {(row['month'], row['day']): row for (index, row) in data.iterrows()}

# Email credentials
my_email = "sender@gmail.com"
password = "password"

# Check if today's date is in the birthdays_dict
if (current_month, current_day) in birthdays_dict:
    bday_person = birthdays_dict[(current_month, current_day)]
    
    # Read all the letter templates
    with open("email-project/letter_templates/letter_1.txt") as letter1:
        letter1_content = letter1.read()
    with open("email-project/letter_templates/letter_2.txt") as letter2:
        letter2_content = letter2.read()
    with open("email-project/letter_templates/letter_3.txt") as letter3:
        letter3_content = letter3.read()
    
    random_letter = random.choice([letter1_content, letter2_content, letter3_content])
    
    bday_letter = random_letter.replace("[NAME]", bday_person['name'])
    
    print(bday_letter)
    
    # Send the email
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=bday_person['email'],  
            msg=f"Subject: Happy Birthday :)\n\n{bday_letter}\n"
        )
else:
    print("No birthdays today.")
