from dataclasses import replace
from time import sleep
import telebot
from telegram import Sticker
from parcing import take_value
from message import *



token = "5291763635:AAHGUWi5sLAVq5JrjS2AhtBxsyj66kpGMM0"
bot = telebot.TeleBot(token)
sticker_id = 'CAACAgIAAxkBAAEFLf9iwN5_f74oBFAlsetkeDhi_XLHLwACUAEAAhYtzTxzKyS_bZOe7CkE'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id, text="Привет! Напиши сообщение в следующем формате:\n /pc <цена> \n и я подберу 5 лучших компьютеров!")
@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, text="Формат ввода: /pc <цена>")
@bot.message_handler(commands=['info'])
def start(message):
    bot.send_message(message.chat.id, text="Привет! Я создан чтобы помочь тебе найти лучший компьютер с популярного онлайн-магазина ONLINER.BY."
                    +" Тебе нужно всего лишь ввести подходящий тебе бюджет!")
    bot.send_sticker(message.chat.id, f'{sticker_id}')


@bot.message_handler(commands=["pc"])
def price_pc(message):
    mess = message.text
    price = mess.replace("/pc ", "")
    print(price)
    price_clear = price.isdigit()
    count = 1
    if price_clear:
        values = take_value(price)
        if len(values) != 0:
            for i in take_value(price):
                bot.send_photo(
                    message.chat.id, photo=i['image'], caption=f"{count}. \n {i['text']}")
                count += 1
                sleep(0.5)
        else:
            bot.send_message(message.chat.id, text=not_result())
    else:
        bot.send_message(message.chat.id, text="Введите целое и положительное число и попробуйте снова.")
    








bot.infinity_polling()
