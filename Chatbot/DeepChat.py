#!/usr/bin/python3
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


# Creating instance
bot = ChatBot('DeepChat', read_only=False, logic_adapters=[
    {
        "import_path": "chatterbot.logic.BestMatch",
        "default_response": "Sorry I don't have an answer",
        "maximum_similarity_threshold": 0.9
    }
    
])

# list to Training
list_to_train = [
    "Hi",
    "Hi there!",
    "Hello",
    "Hi there!",
    "How are you doing?",
    "Sorry, I'm a Bot I don't have feelings",
    "How are you?",
    "Sorry, I'm a Bot I don't have feelings...",
    "Lolz",
    "Funny right! Smiles..",
    "How old are you?",
    "Sorry, I'm a Bot, I'm ageless\n",
    "What's your name?",
    "I am a Bot named DeepChat... You like it!!",
    "What is your name?",
    "I am a Bot named DeepChat... You like it!!",
    "Okay",
    "Yeah",
    "Thank you",
    "You're welcome! ",
    "Really",
    "Yeah",
    "Thanks",
    "You're welcome! "
]

# These commands exit the bot
quit_commands = [
    'quit',
    'exit',
    'stop',
    'sleep',
    'bye'
]

# List trainer
list_trainer = ListTrainer(bot)
list_trainer.train(list_to_train)

print("\n\t--------------------------------DeepChat--------------------------------\n")

running = True
while running:
    # Get user's input
    response = str(input('\nUser: '))

    # Handling Errors from users
    if response=='':
        print("DeepChat: You asked nothing...")
        pass
    elif response in quit_commands:
        print("\nDeepChat: Alright, Bye. See you soon! \n")
        break
    else:
        # print("\nDeepChat: Sorry, I don't have an answer to '{}'?\n".format(response))
        response = bot.get_response(response)
        print('\nDeepChat: {}\n'.format(response))

print("\n\t--------------------------------Byeeeee--------------------------------\n")