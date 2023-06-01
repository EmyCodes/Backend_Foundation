#!/usr/bin/python3

import requests
import time

token = "6225658854:AAHbEAoqdFo-gcXrEcEU5uqTYw8MjX36dqc"
base_url = "https://api.telegram.org/bot{}/sendPhoto".format(token)

audios_urls = [
    "https://t.me/RevdAtegberoteachings/307",
    "https://t.me/RevdAtegberoteachings/308",
    "https://t.me/RevdAtegberoteachings/309"
]

for url in audios_urls:
    time.sleep(5)
    parameters = {
        "chat_id": "956127600",
        "photo": url,
        "caption": "Audio {}".format(url)
    }
    
    response = requests.get(base_url, data=parameters)
    print(response.text)