#/usr/bin/python3

import requests
import sys
import time

token = "6225658854:AAHbEAoqdFo-gcXrEcEU5uqTYw8MjX36dqc"
base_url = "https://api.telegram.org/bot{}/sendPhoto".format(token)

photos_urls = [
    "https://imgtr.ee/images/2023/05/31/1jolY.jpg",
    "https://imgtr.ee/images/2023/05/31/1jolY.jpg",
    "https://imgtr.ee/i/1jJbX",
    "https://imgtr.ee/i/1j8R1",
    "https://imgtr.ee/i/1jahV"
]

for url in photos_urls:
    time.sleep(5)
    parameters = {
        "chat_id": "956127600",
        "photo": url,
        "caption": "Photo {}".format(url)
    }
    
    response = requests.get(base_url, data=parameters)
    print(response.text)