import telebot
from datetime import datetime
import calendar
import locale
from pprint import pprint
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')

CREDENTIALS_FILE = 'credentials.json'  #  ← имя скаченного файла с закрытым ключом
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)
spreadsheetId = '1UCAw3PTluEKc3noSBrMcLlfCU1WHhpraLd8Zwh9z9Lg'

def write_in_cell(cell, value):
    body_to_write = {"valueInputOption": "USER_ENTERED",
                     "data": [{"range": 'Лист1' + "!" + cell,
                               "majorDimension": "ROWS",
                               "values": [[value]]}]
                    }
    service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheetId, body=body_to_write).execute()


bot = telebot.TeleBot("1134602259:AAFnxbhTUG3WQlVBjzdH_11zRywl9lYK1_4")



@bot.message_handler(content_types=['text'])
def send_welcome(message):
    markup = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton(text='CLick me', callback_data='add')
    button2 = telebot.types.InlineKeyboardButton(text='CLick me 2', callback_data='add1')
    markup.add(button1, button2)
    bot.send_message(chat_id=message.chat.id, text='Some text', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
# def write_in_cell (cell):
#     body_to_write = {"valueInputOption": "USER_ENTERED", "data": [{"range": 'Лист1' + "!" + cell,
#                      "majorDimension": "ROWS", "values": [[1]]}]
#                     }
#     service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheetId, body=body_to_write).execute()

def query_handler(call):
    if call.data == 'add':
        bot.answer_callback_query(callback_query_id=call.id, text='Hello world')
        write_in_cell('A1', 333)
    elif call.data == 'add1':
        bot.answer_callback_query(callback_query_id=call.id, text='Hello world u2')
        write_in_cell('A1', 444)

bot.polling(none_stop=True)



#

# range_name = 'Лист1!A:G'
# table = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=range_name).execute()
# spread_sheet_values = table['values']
#
#

