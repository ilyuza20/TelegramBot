import time

import telebot
from deeppavlov import build_model
from deeppavlov.core.common.file import read_json
import logging

logging.basicConfig(level=logging.DEBUG)
bot = telebot.TeleBot("1985173749:AAGpKK0JpKF1_71Oz8oyV_W73Xwgm9arL-0")
model_config = read_json("squad_ru_bert_infer.json")
model = build_model(model_config, download=True)
print("Model is installed")

#context = open('context.txt', 'r')
with open("/Users/днс/PycharmProjects/pythonProject2/context.txt") as f:
    context = [word for line in f for word in line.split(".")]


@bot.message_handler(commands=["help", "h"])
def handle_help(message):
    bot.send_message(message.from_user.id, "Help? \n"
                                           "/q or /question - ask a question\n")


# @bot.message_handler(commands=["context", "c"])
# def parse_context(message):
#    context[message.from_user.id] = message.text[3:]
#    bot.send_message(message.from_user.id, "The context is set")


@bot.message_handler(commands=["question", "q"])
def answer_question(message):
    question: str = message.text[1:]
    logging.debug(message.from_user.id)
    answers = model([''.join(map(str, context))], [question])
    logging.info(answers)
    print(answers)
    bot.send_message(message.from_user.id, answers)


@bot.message_handler()
def handle_message(message):
    bot.send_message(message.from_user.id, "Please send '/help' to know how to use this bot")


while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        time.sleep(15)
