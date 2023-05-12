#!/usr/bin/python3
from chatterbot import ChatBot

UnitBot = ChatBot('DeepChat', logical_adapters=[
    "chatterbot.logical.UnitConversion"
])




running = True
while running:
    print("DeepChat: What do you want to Covert? ")
    user = input("Me: ")
    try:
        bot = UnitBot.get_response(user)
        print("DeepChat: {}".format(str(bot)))
    except Exception:
        print("DeepChat: Sorry, I don't understand what you mean.")