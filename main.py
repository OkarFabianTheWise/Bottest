from audioop import add
from itertools import count
import os
import time
import asyncio
import heroku3
import random
import flask
import secrets
import requests
import webhooks
from flask import Flask, request
import logging
from xml.etree.ElementInclude import include
from telebot import TeleBot
from config import TOKEN
import telebot

bot = telebot.TeleBot("5679878646:AAG0BJwWoNIDaeq_cw0xn2JCq8IJzWAmOmY")
server = flask(__name__)

#antispam
@bot.message_handler(content_types=['text'])
def spam(message):
    p= message.text 
    print(p)
    meek= message.from_user.username
    if meek==None: 
        bot.send_message(message.chat.id, "get tf out")
        bot.kick_chat_member(message.chat.id, message.from_user.id)

#Roll number Game
@bot.message_handler(commands=['roll'])
def handle_command(message):
    roll = random.randint(1, 1000  )
    bot.get_chat_members_count(message.chat.id)
    bot.send_message(message.chat.id, count)
    
@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://trackmoth.herokuapp.com//' + TOKEN)
    return "!", 200
   

if __name__ == '__main__':
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))