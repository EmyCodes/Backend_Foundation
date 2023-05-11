#!/usr/bin/python3
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


# Creating instance
bot = ChatBot('DeepChat', read_only=False, logic_adapters=['chatterbot.logic.BestMatch'])

# list to Training
list_to_train = [
    "Hi",
    "Hi there!",
    "Hello",
    "Hi there!",
    "What's your name?",
    "I am a Bot named DeepChat... You like it!!",
    "What is your name?",
    "I am a Bot named DeepChat... You like it!!",
    "How are you doing?",
    "Sorry, I'm a Bot I don't have feelings",
    "How are you?",
    "Sorry, I'm a Bot I don't have feelings",
    "How old are you?",
    "Sorry, I'm a Bot, I'm ageless\n"
]

# These commands exit the bot
quit_commands = [
    'quit',
    'quit()',
    'exit',
    'exit()',
    'stop',
    'sleep'
]

# List trainer
list_trainer = ListTrainer(bot)
list_trainer.train(list_to_train)

running = True
while running:
    # Get user's input
    response = str(input('\nUser: '))

    # checks whether the input is valid with the bot training
    if response.capitalize() in list_to_train:
        response = response.capitalize()
        response = bot.get_response(response)
        print('\nDeepChat: {}\n'.format(response))
    elif response.lower() in quit_commands:
        print("\nDeepChat: Alright, Bye. See you soon! \n")
        break
    else:
        print("\nDeepChat: Sorry, What do you mean by '{}'?\n".format(response))

