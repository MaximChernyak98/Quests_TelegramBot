import logging

from telegram.ext import (
    MessageHandler,
    Filters,
    CallbackQueryHandler
)

import settings
import handlers

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename="bot.log"
)


def main():
    dp = settings.MYBOT.dispatcher

    while True:
        dp.add_handler(CallbackQueryHandler(handlers.get_state_of_quest()))
        settings.MYBOT.start_polling()


if __name__ == '__main__':
    main()
