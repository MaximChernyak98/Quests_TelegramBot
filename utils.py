from datetime import datetime, timedelta, date
import settings
import config
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def print_message_with_keyboard(message, buttons_text_list):
    keyboard = []
    for button in buttons_text_list:
        keyboard.append(InlineKeyboardButton(button[0], callback_data=button[1]))
    reply_markup = InlineKeyboardMarkup([keyboard])
    settings.MYBOT.bot.send_message(chat_id=config.CHAT_ID, text=message, reply_markup=reply_markup)


def print_quests(*args):
    yesterday = (date.today() - timedelta(days=1)).strftime('%d.%m.%Y')
    values_list = settings.GOOGLE_WORKSHEET.row_values(1)
    for index, value in enumerate(values_list[1:]):
        buttons_text_list = [('Сделал', f'успех/{yesterday}/{index + 1}'),
                             ('Не сделал', f'провал/{yesterday}/{index + 1}')]
        print_message_with_keyboard(value, buttons_text_list)


def convert_colnum_to_letters(n):
    string = ""
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        string = chr(65 + remainder) + string
    return string


def set_cell_0_or_1(row, column, state):
    cell = f'{convert_colnum_to_letters(column)}{row}'
    if state == 'Слабочок':
        settings.GOOGLE_WORKSHEET.update_cell(row, column, 0)
        red_background_color = {"red": 22, "green": 103, "blue": 103}
        settings.GOOGLE_WORKSHEET.format(cell, {'backgroundColor': red_background_color})
    else:
        settings.GOOGLE_WORKSHEET.update_cell(row, column, 1)
        green_background_color = {"red": 74, "green": 41, "blue": 88}
        settings.GOOGLE_WORKSHEET.format(cell, {'backgroundColor': green_background_color})
