STOCK = "NVDA"
COMPANY_NAME = "Nvidia Corp"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
parameters = {"function": "TIME_SERIES_DAILY",
              "symbol": STOCK,
              "apikey": "H5L9NSPIMPTVOLE8"
              }

news_params = {
    "apiKey": "210e4a497f6e4024affb5f5215dd4279",
    "q": COMPANY_NAME,
    "searchIn": "title",
    "searchIn": "description", 
    "language": "en",
    "totalResults": 4,
    "sortBy": "popularity"
}

import requests
from datetime import datetime, timedelta
from twilio.rest import Client
#### Getting stock values and comparing ####
response = requests.get(url=STOCK_ENDPOINT, params=parameters)
stock_data = response.json()

news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
news_data = news_response.json()
news_title = []
news_description = []
for i in range(4):
    title = news_data["articles"][i]['title']
    news_title.append(title)
for i in range(4):
    description = news_data["articles"][i]['description']
    description = description[15:len(description)]
    news_description.append(description)
account_sid = "Axxxxxxxxxxxxxxxxxxxxxxxxxxxx"
auth_token  = "axxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

client = Client(account_sid, auth_token)
yesterday = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')
day_before_yesterday = (datetime.now() - timedelta(2)).strftime('%Y-%m-%d')

yesterday_stock = float(stock_data["Time Series (Daily)"][yesterday]['4. close'])
day_before_yesterday_stock = float(stock_data["Time Series (Daily)"][day_before_yesterday]['4. close'])
print(f"Stock prices for {COMPANY_NAME} {yesterday} = {yesterday_stock}, {day_before_yesterday} = {day_before_yesterday_stock}.")
def cal_percent():
    message_data = ""
    if yesterday_stock == day_before_yesterday_stock:
         message += "No change in the stock market.\n"
    if yesterday_stock > day_before_yesterday_stock:
        diff = round((yesterday_stock - day_before_yesterday_stock)/ day_before_yesterday_stock * 100, 2)
        if diff >= 0.2:
            message_data += f"{STOCK}: 🔺 {diff}%\n"
            for title, description in zip(news_title, news_description):
                message_data += f"Headline: {title}.\nBrief: {description}.\n"
    if yesterday_stock < day_before_yesterday_stock:
        diff = round((day_before_yesterday_stock - yesterday_stock)/ yesterday_stock * 100, 2)
        if diff >= 0.2:
            message_data += f"{STOCK}: 🔻 {diff}%\n"
            for title, description in zip(news_title, news_description):
                message_data += f"Headline: {title}.\nBrief: {description}.\n"
    return message_data 
new_message = cal_percent()
print(new_message)
'''message = client.messages.create(
    to="+140000000000",
    from_="+18000000000",
    body= new_message)

print(message.sid)'''









