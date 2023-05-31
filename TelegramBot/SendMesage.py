#/usr/bin/python3

import requests
import sys
import time

token = "6225658854:AAHbEAoqdFo-gcXrEcEU5uqTYw8MjX36dqc"
base_url = "https://api.telegram.org/bot{}/sendMessage".format(token)

greetings = ["Hello there!", "Hi everyone", "What do you have for today?", "Cheers guys"]

for greeting in greetings:
    time.sleep(5)
    parameters = {
        "chat_id": "-1001579133774",
        "text": "Zipporah {}".format(greeting)
    }
    
    response = requests.get(base_url, data=parameters)
    print(response.text)