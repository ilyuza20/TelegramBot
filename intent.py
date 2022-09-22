import json
import time

import telebot
from deeppavlov import build_model, train_model
from deeppavlov.core.common.file import read_json
import logging

logging.basicConfig(level=logging.DEBUG)
bot = telebot.TeleBot("1985173749:AAGpKK0JpKF1_71Oz8oyV_W73Xwgm9arL-0")
model_config = read_json("squad_ru_bert_infer.json")
model1 = build_model(model_config, download=True)
print("Model is installed")

context = open('context.txt', 'r')


@bot.message_handler()
def handle_start(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Hi! What do you need?")
        bot.register_next_step_handler(message, get_intent)  # следующий шаг
    else:
        bot.send_message(message.from_user.id, "Write '/start' to get started with the bot.")


def get_intent(message):

    config = read_json("intent_catcher.json")
    model = build_model(config)
    print("Model built")

    intent = model([message.text])
    print(intent)
    if intent == ['calculator']:
        bot.send_message(message.from_user.id, "You can calculate here: https://calcus.ru/calculator-imt")
        bot.register_next_step_handler(message, get_intent)
    elif intent == ['fitness_club']:
        #bot.send_message(message.from_user.id, "Ask your question, please")
        bot.register_next_step_handler(message, answer_question(message))
        bot.register_next_step_handler(message, get_intent)
    else:
        bot.send_message(message.from_user.id, "Sorry, I don't understand")


def answer_question(message):
    question: str = message.text[1:]
    logging.debug(message.from_user.id)
    answers = model1([''.join(map(str, context))], [question])
    logging.info(answers)
    print(answers)
    bot.send_message(message.from_user.id, answers)


while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        time.sleep(15)
