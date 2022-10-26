from fileinput import filename
import os
import logging
import telegram
import requests 
from telegram.ext import Updater
from telegram.ext import CommandHandler, PicklePersistence
import websockets
import selenium
import asyncio

async def get_prices():
    coins = ["BTC", "ETH", "XRP", "LTC", "BCH", "ADA", "DOT", "LINK", "BNB", "XLM", "MATIC"]

    crypto_data = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms=USD".format(",".join(coins))).json()["RAW"]
        
        async with websockets.connect(https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms=USD) as client:
        pass 
    
     print(await client.recv())

    data = {}
    for i in crypto_data:
        data[i] = {
            "coin": i,
            "price": crypto_data[i]["USD"]["PRICE"],
            "change_day": crypto_data[i]["USD"]["CHANGEPCT24HOUR"],
            "change_hour": crypto_data[i]["USD"]["CHANGEPCTHOUR"]
        }

    return data


if __name__ == "__main__":

     loop = asyncio.get_prices()
     loop.run_until_forever(get_prices())

telegram_bot_token = "5547565271:AAHtiiRajG3dozhAm0QbKWeiM2Ii3RHfeJs"

updater = Updater(token=telegram_bot_token, use_context=True, persistence=PicklePersistence(filename='bot_data'))
dispatcher = updater.dispatcher


def start_command(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text="hi! i was built and used for sample by the owner of t.me/cryptowisechannel! This is not the best of me.")

dispatcher.add_handler(CommandHandler("start", start_command))
updater.start_polling(1.0)

def chart_command(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text = "get_prices()")

dispatcher.add_handler(CommandHandler("chart", chart_command))
updater.start_polling(1.0)

def info_command(update, context):
    chat_id = update.effective_chat.id
    message = ""

    crypto_data = get_prices()
    for i in crypto_data:
        coin = crypto_data[i]["coin"]
        price = crypto_data[i]["price"]
        change_day = crypto_data[i]["change_day"]
        change_hour = crypto_data[i]["change_hour"]
        message += f"Coin: {coin}\nPrice: ${price:,.2f}\nHour Change: {change_hour:.3f}%\nDay Change: {change_day:.3f}%\n\n"

    context.bot.send_message(chat_id=chat_id, text=message)


dispatcher.add_handler(CommandHandler("info", info_command))
updater.start_polling(1.0)

updater.idle() 


