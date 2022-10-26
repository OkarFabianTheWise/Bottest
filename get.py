import requests 
import json
import pathlib
from setuptools import setup
from pythonpancakes import PancakeSwapAPI
ps = PancakeSwapAPI()
import telebot
from telebot import TeleBot
import heroku3
import matplotlib
import flask

BOT_TOKEN = '5577718850:AAERXpn4HKx4bFVOXa5gO2cnlhYTq5M-KBo'
bot = TeleBot(token=BOT_TOKEN)


@bot.message_handler(content_types=['text'])
def crypto_price_message_handler(message):
    contract = message.text
    token = ps.tokens(0xB17eA69c335589C9886763d298fCaDD9856485D9)
    bot.send_message(chat_id = message.chat.id, text=f"Your token search, {contract} is : {token}")
   
    print(token)