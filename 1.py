import time
import telebot

bot = telebot.TeleBot("1985173749:AAGpKK0JpKF1_71Oz8oyV_W73Xwgm9arL-0")



@bot.message_handler(commands=["help", "h"])
def handle_help(message):
    bot.send_message(message.from_user.id, "Help?")

@bot.message_handler(commands=["question", "q"])
def handle_help(message):
    bot.send_message(message.from_user.id, "Any questions?")

@bot.message_handler()
def handle_message(message):
    bot.send_message(message.from_user.id, "Hello")

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        time.sleep(15)


#answers = model(["Входной текст", ...], ["Вопрос", ...],[["Текст ответа", loss], ...])
