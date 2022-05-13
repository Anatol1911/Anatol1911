import  requests
from datetime import datetime
import telebot
from auth_data import token




def get_data():
    req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
    response = req.json()
    sell_цена = response["btc_usd"]["sell"]
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC цена: {sell_цена}")


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(message.chat.id, "Привет путник! Посмотри 'цена' что бы получить лучшую цену на BTC!")

    @bot.message_handler(content_types=["text"])
    def send_text(message):
        if message.text.lower() == 'цена':
            try:
                req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
                response = req.json()
                sell_цена = response["btc_usd"]["sell"]
                bot.send_message(
                    message.chat.id,
                    f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC цена: {sell_цена}"
                )
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "Чёрт... что-то пошло не так..."
                )
        else:
            bot.send_message(message.chat.id, "Штааа??? проверь команду чел!")


    bot.polling()

if __name__ == '__main__':
    # get_data()
    telegram_bot(token)