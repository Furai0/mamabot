#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.
import random
import telebot
from telebot import types

API_TOKEN = '7839862006:AAGdUPvjPnXmRxgjQOJQ-PkA_cTdXD_sNEk'

bot = telebot.TeleBot(API_TOKEN)



hangry = ['Нет'],['Только поел'],['Сытый']
food = ['Маленьких детей'], ['Картошку'], ['Шашлык'], ['Роллы']

@bot.message_handler(commands=['start'])
def handle_start(message):

  # Создание клавиатуры
  keyboard = types.ReplyKeyboardMarkup(row_width=1)
  button1 = types.KeyboardButton('Сына, ты голодный?', resize_markup=True)
  button2 = types.KeyboardButton('Что ел?', resize_markup=True)

  keyboard.add(button1, button2)
  bot.reply_to(message, 'Привет! Я mam бот. ', reply_markup=keyboard)


@bot.message_handler(func=lambda message: True, content_types=['text', 'photo', 'sticker'])
def chat(message):

    if message.photo:
        bot.send_message(message.chat.id, 'Вы отправили изображение. С изображениями пока работать не умеем(')

    elif message.sticker:
        bot.send_message(message.chat.id, 'Вы отправили стикер. С стикерами пока работать не умеем(')

    elif message.text == 'Сына, ты голодный?':
            bot.reply_to(message, random.choice(hangry))

    elif message.text == 'Что ел?':
        bot.reply_to(message, random.choice(food))

    else:
        bot.reply_to(message, 'Неизвестная команда. Чтобы начать, напиши /start')

# print jopa popa

bot.polling()
