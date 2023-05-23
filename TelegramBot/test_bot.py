#!/usr/bin/python3
"""Quering https://api.telegram.org/ to fetch data"""


import json
import requests
import sys


token = sys.argv[1]
url = "https://api.telegram.org/bot{}/getUpdates".format(token)
response = requests.get(url)
# Parse to json
response = response.text

# with open("telegram_api.json", 'w', encoding='utf-8') as file_:
#    json.dump(response, file_, ensure_ascii=False)

with open("telegram_api.text", "w", encoding='utf-8') as file_:
    file_.write(response)

# print(response)
