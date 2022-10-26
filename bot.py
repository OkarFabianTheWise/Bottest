import requests


def get_prices():
    coins = ["BTC", "ETH", "XRP", "LTC", "BCH", "ADA", "DOT", "LINK", "BNB", "XLM"]

    crypto_data = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms=USD".format(",".join(coins))).json()["RAW"]

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
    print(get_prices())

    if token:
        price = contract[contract]['usd']
        bot.send_message(chat_id = message.chat.id, text=f"The price of {contract}: {price}\n Hey I was Created by @cryptowisechannel!This is not the best of me!")
    else:
         bot.send_message(chat_id = message.chat.id, text=f"Your token search, {contract} was not found")
    