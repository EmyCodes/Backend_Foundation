#!/usr/bin/python3
from chatterbot import ChatBot

UnitBot = ChatBot('DeepChat', logical_adapters=[
    "chatterbot.logical.UnitConversion"
])


quit_commands = [
    'quit',
    'exit',
    'stop',
    'sleep',
    'bye'
]


running = True
while running:
    print("DeepChat: What do you want to Convert? ")
    user = input("Me: ")
    if str(user)=='':
        print("DeepChat: You asked nothing...")
        pass
    elif user in quit_commands:
        print("\nDeepChat: Alright, Bye. See you soon! \n")
        break    
    try:
        bot = UnitBot.get_response(user)
        print("DeepChat: {}".format(str(bot)))
    except Exception:
        print("DeepChat: Sorry, I don't understand what you mean.")