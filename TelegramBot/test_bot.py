#!/usr/bin/python3
"""Quering https://api.telegram.org/ to fetch data"""


import json
import requests


url = "https://api.telegram.org/bot6225658854:AAGfSl53gx7MZ8Sm-upqF04Ie8DZruPYyWM/getUpdates"
response = requests.get(url)
# Parse to json
response = response.text

# with open("telegram_api.json", 'w', encoding='utf-8') as file_:
#    json.dump(response, file_, ensure_ascii=False)

with open("telegram_api.text", "w", encoding='utf-8') as file_:
    file_.write(response)

# print(response)