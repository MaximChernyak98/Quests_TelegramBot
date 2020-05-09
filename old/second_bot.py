import telebot
import gspread
from google.oauth2.service_account import Credentials

# Даем доступ к таблице
CREDENTIALS_FILE = 'c:\\Work\\Python\\telegram_bot\\credentials.json'
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=scope)
gc = gspread.authorize(credentials)

# Открываем таблицу
worksheet = gc.open_by_key('1UCAw3PTluEKc3noSBrMcLlfCU1WHhpraLd8Zwh9z9Lg').sheet1

def colnum_string (n):
    string = ""
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        string = chr(65 + remainder) + string
    return string

def set_cell_0_or_1 (row, column, state):
    cell = f'{colnum_string(column)}'+ f'{row}'
    if state == 0:
        worksheet.update_cell(row, column, 0)
        #красный
        worksheet.format(cell,
                         {'backgroundColor': {
                          "red": 22,
                          "green": 103,
                          "blue": 103
                         }})
    else:
        worksheet.update_cell(row, column, 1)
        # зеленый
        worksheet.format(cell,
                         {'backgroundColor': {
                             "red": 74,
                             "green": 41,
                             "blue": 88
                         }})

set_cell_0_or_1 (18, 8, 0)



#
# def write_in_cell(cell, value):
#     body_to_write = {"valueInputOption": "USER_ENTERED",
#                      "data": [{"range": 'Лист1' + "!" + cell,
#                                "majorDimension": "ROWS",
#                                "values": [[value]]}]
#                     }
#     service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheetId, body=body_to_write).execute()
#
#
# bot = telebot.TeleBot("1134602259:AAFnxbhTUG3WQlVBjzdH_11zRywl9lYK1_4")
#
#
#
# @bot.message_handler(content_types=['text'])
# def send_welcome(message):
#     markup = telebot.types.InlineKeyboardMarkup()
#     button1 = telebot.types.InlineKeyboardButton(text='CLick me', callback_data='add')
#     button2 = telebot.types.InlineKeyboardButton(text='CLick me 2', callback_data='add1')
#     markup.add(button1, button2)
#     bot.send_message(chat_id=message.chat.id, text='Some text', reply_markup=markup)
#
# @bot.callback_query_handler(func=lambda call: True)
# # def write_in_cell (cell):
# #     body_to_write = {"valueInputOption": "USER_ENTERED", "data": [{"range": 'Лист1' + "!" + cell,
# #                      "majorDimension": "ROWS", "values": [[1]]}]
# #                     }
# #     service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheetId, body=body_to_write).execute()
#
# def query_handler(call):
#     if call.data == 'add':
#         bot.answer_callback_query(callback_query_id=call.id, text='Hello world')
#         write_in_cell('A1', 333)
#     elif call.data == 'add1':
#         bot.answer_callback_query(callback_query_id=call.id, text='Hello world u2')
#         write_in_cell('A1', 444)
#
# bot.polling(none_stop=True)
#
#
#
# #
#
# # range_name = 'Лист1!A:G'
# # table = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=range_name).execute()
# # spread_sheet_values = table['values']
# #
# #
#
