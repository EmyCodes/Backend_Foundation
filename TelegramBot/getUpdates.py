#!/usr/bin/python3
"""Quering https://api.telegram.org/ to fetch data"""


import json
import requests


token = "6225658854:AAHbEAoqdFo-gcXrEcEU5uqTYw8MjX36dqc"
url = "https://api.telegram.org/bot{}/getUpdates".format(token)
response = requests.get(url)
# print(response.text)

# Parse to json
response_json = response.json()
# response = response.text

with open("telegram_api.json", 'w', encoding='utf-8') as file_:
    json.dump(response_json, file_, ensure_ascii=False)

with open("telegram_api.text", "w", encoding='utf-8') as file_:
    file_.write(response.text)

# url = str(url) + "?offset=770271262"
# response = requests.get(url)
# for k, v in response:
#    print("{}\t{}".format)
# Access the 'from' field
from_field = response_json['result'][0]['message']['from']['first_name']
print('Hey {}!'.format(from_field.split()[0]))
base_url = "https://api.telegram.org/bot{}/getUpdates".format(token)