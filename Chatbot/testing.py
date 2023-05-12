#!/usr/bin/python3
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


chatbot = ChatBot('DeepChat')

conversation = [
    "Hello",
    "Hi there, how may I help you today!",
    "What's your name",
    "I am a Bot named DeepChat. You like it!!",
    "How are you doing",
    "Sorry, I'm a Bot I don't have feelings",
    "How old are you",
    "Sorry, I'm a Bot I'm ageless",
    "Thank you",
    "You're welcome."
]

trainer = ListTrainer(chatbot)

trainer.train(conversation)

response = chatbot.get_response(str(input("\nUser: ")))
print("\nBot: {}\n".format(response))