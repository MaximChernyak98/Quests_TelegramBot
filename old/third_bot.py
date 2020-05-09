import telebot
import gspread
from google.oauth2.service_account import Credentials
from datetime import date, timedelta

# Даем доступ к таблице
CREDENTIALS_FILE = 'c:\\Work\\Python\\telegram_bot\\credentials.json'
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=scope)
gc = gspread.authorize(credentials)

# Открываем таблицу
worksheet = gc.open_by_key('1UCAw3PTluEKc3noSBrMcLlfCU1WHhpraLd8Zwh9z9Lg').sheet1

# Открываем бота
bot = telebot.TeleBot("1134602259:AAFnxbhTUG3WQlVBjzdH_11zRywl9lYK1_4")

@bot.message_handler(content_types=['text'])
def print_quests(message):
    yesterday = (date.today() - timedelta(days=1)).strftime('%d.%m.%Y')
    values_list = worksheet.row_values(1)
    print(message.chat.id)
    for i in range(1, len(values_list)):
        markup = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text='Сделал', callback_data=f'успех/{yesterday}/{i}')
        button2 = telebot.types.InlineKeyboardButton(text='Не сделал', callback_data=f'провал/{yesterday}/{i}')
        markup.add(button1, button2)
        bot.send_message(chat_id=message.chat.id, text= values_list[i], reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    # Получаем информация от нажатой кнопки
    state = call.data.split("/")[0]
    day = call.data.split("/")[1]
    number_of_quest = int(call.data.split("/")[2]) + 1
    # Ищем строку с нужной датой
    date_list = worksheet.col_values(1)
    row = int(date_list.index(day)) + 1
    if state == 'успех':
        bot.answer_callback_query(callback_query_id=call.id, text=f'Молодца {number_of_quest} {day} {row}')
        set_cell_0_or_1(row, number_of_quest, 1)
      
    else:
        bot.answer_callback_query(callback_query_id=call.id, text=f'Слабочок {number_of_quest} {day} {row}')
        set_cell_0_or_1(row, number_of_quest, 0)

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

def colnum_string (n):
    string = ""
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        string = chr(65 + remainder) + string
    return string



bot.polling(none_stop=True)

