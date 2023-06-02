#!/usr/bin/python3

"""Comment"""

import telegram.ext

Token = "6225658854:AAHbEAoqdFo-gcXrEcEU5uqTYw8MjX36dqc"

updater = telegram.ext.updater(Token, use_context=True)

dispatcher = updater.dispatcher


def start(update, context):
    update.message.reply_text("Hello. Welcome to DeepChat")


def emycodes(update, context):
    update.message.reply_text("Click here to learn more about emycodes: https://wwww.emycodes.tech")


def mamuro(update, context):
    update.message.reply_text("Click here to learn more about emycodes: https://wwww.mamuro.tech")


def niyero(update, context):
    update.message.reply_text("Click here to learn more about emycodes: https://wwww.niyero.tech")
