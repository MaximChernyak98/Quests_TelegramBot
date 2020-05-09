import telebot

bot = telebot.TeleBot("1134602259:AAFnxbhTUG3WQlVBjzdH_11zRywl9lYK1_4")

@bot.message_handler(content_types=['text'])
def send_welcome(message):
	bot.reply_to(message, (message.text + ", мля"))

bot.polling(none_stop=True)


# -*- coding: utf-8 -*-


# import telebot
#
# TOKEN = "1134602259:AAFnxbhTUG3WQlVBjzdH_11zRywl9lYK1_4"
# bot = telebot.TeleBot(TOKEN)
#
#
# # Приветственная надпись
# @bot.message_handler(commands=['start'])
# def start(message):
#     sent = bot.send_message(message.chat.id, 'Как тебя зовут?')
#     bot.register_next_step_handler(sent, hello)
#
#
# def hello(message):
#     bot.send_message(message.chat.id, 'Привет, {name}. Рад тебя видеть.'.format(name=message.text))
#
#
# bot.polling()