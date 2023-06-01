#!/usr/bin/python3

import requests
import time

token = "6225658854:AAHbEAoqdFo-gcXrEcEU5uqTYw8MjX36dqc"
base_url = "https://api.telegram.org/bot{}/sendPhoto".format(token)

audios_urls = [
    "https://www.boomplay.com/songs/125335440?srModel=COPYLINK&srList=WEB",
    "https://www.boomplay.com/songs/116836286?srModel=COPYLINK&srList=WEB",
    "https://www.boomplay.com/songs/123079560?srModel=COPYLINK&srList=WEB"
]

for url in audios_urls:
    time.sleep(5)
    parameters = {
        "chat_id": "956127600",
        "photo": url,
        "caption": "Audio {}".format(url)
    }
    
    response = requests.get(base_url, data=parameters)
    # print(response.text)