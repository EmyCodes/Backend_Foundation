#!/usr/bin/python3

import telegram
from telegram.ext import Updater, CommandHandler

Token = "6225658854:AAHbEAoqdFo-gcXrEcEU5uqTYw8MjX36dqc"
updater = Updater(Token, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello. Welcome to DeepChat")

def emycodes(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Click here to learn more about emycodes: https://www.emycodes.tech")

# Add more handlers as needed

start_handler = CommandHandler('start', start)
emycodes_handler = CommandHandler('emycodes', emycodes)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(emycodes_handler)

updater.start_polling()
updater.idle()
