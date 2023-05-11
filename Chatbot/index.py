#!/usr/bin/python3
from chatterbot import ChatBot

bot = ChatBot('DeepChat', read_only=True, logic_adapters=['chatterbot.logic.BestMatch'])