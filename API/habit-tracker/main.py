import requests
from datetime import datetime, timedelta
USERNAME = "snazneen"
TOKEN = "abc8934jgjhnbo"
GRAPHID = "ht1"
pixela_endpoint = "https://pixe.la/v1/users"
current_date = (datetime.now()).strftime('%Y%m%d')
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPHID,
    "name": "Walking Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)

#print(response.text)

post_pixel_endpoint = f"{graph_endpoint}/{GRAPHID}"

post_params = {
    "date": current_date,
    "quantity": "3.5"
}
#response = requests.post(url=post_pixel_endpoint, json=post_params, headers=headers)
#print(response.text)

update_pixel_endpoint = f"{post_pixel_endpoint}/{current_date}"
update_params = {
    "quantity": "2.5"
}
response = requests.put(url=update_pixel_endpoint, params=update_params, headers=headers)
print(response.text)