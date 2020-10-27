import settings
import utils


def get_state_of_quest(update, context):
    pushed_button = update.callback_query.data
    state = pushed_button.split("/")[0]
    day = pushed_button.split("/")[1]
    number_of_quest = int(pushed_button.split("/")[2]) + 1

    date_list = [str(i) for i in settings.GOOGLE_WORKSHEET.col_values(1)]
    row = int(date_list.index(day)) + 1
    if state == 'успех':
        state_message = 'Молодца'
    else:
        state_message = 'Слабочок'
    update.callback_query.answer(f'{state_message} {number_of_quest} {day} {row}')
    utils.set_cell_0_or_1(row, number_of_quest, state_message)
