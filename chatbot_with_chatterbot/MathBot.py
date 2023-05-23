#!/usr/bin/python3
from chatterbot import ChatBot

math_bot = ChatBot('DeepChat', logic_adapters=[
    'chatterbot.logic.MathematicalEvaluation'
])

# quit commands
quit_commands = [
    'quit',
    'exit',
    'stop',
    'sleep',
    'bye'
]

print("\n\t--------------------------------DeepChat--------------------------------")

# Gives thread conversations
running = True
while running:
    print("\nDeepChat: What is your mathematical problem?")
    user = input("Me: ")
    try:
        if user == "":
            print("DeepChat: No input... \n")
            pass
        elif user in quit_commands:
            print("DeepChat: Bye... See y'all later!")
            break
        else:
            bot_response= math_bot.get_response(user)
            print("DeepChat: {} \n".format(bot_response))
    except Exception:
            print("DeepChat: Type valid numbers either in words or figures... ")
print("\n\t--------------------------------Byeeeeee--------------------------------\n")

        