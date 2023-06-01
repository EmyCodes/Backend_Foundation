#!/usr/bin/python3

import requests


token = "6225658854:AAHbEAoqdFo-gcXrEcEU5uqTYw8MjX36dqc"
base_url = "https://api.telegram.org/bot{}".format(token)

def read_msg():
    """Message Reading Function"""

    parameters = {
        "offset": "770271270"
    }

    response = requests.get(base_url + "/getUpdates", data = parameters)

    data = response.json()

    for result in data["result"]:
        print(result["message"]["text"])