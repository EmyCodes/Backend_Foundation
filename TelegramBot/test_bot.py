#!/usr/bin/python3
"""Quering https://api.telegram.org/ to fetch data"""


import json
import requests
import sys


token = sys.argv[1]
url = "https://api.telegram.org/bot{}/getUpdates".format(token)
response = requests.get(url)
# Parse to json
response_json = response.json()
# response = response.text

# with open("telegram_api.json", 'w', encoding='utf-8') as file_:
#    json.dump(response, file_, ensure_ascii=False)

with open("telegram_api.text", "w", encoding='utf-8') as file_:
    file_.write(str(response_json))

# url = str(url) + "?offset=770271262"
# response = requests.get(url)
# for k, v in response:
#    print("{}\t{}".format)
# Access the 'from' field
from_field = response_json['result'][0]['message']['from']['first_name']
print('Hey {}!'.format(from_field.split()[0]))