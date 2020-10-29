import logging
import time
import datetime

from telegram.ext import (
    MessageHandler,
    Filters,
    CallbackQueryHandler
)

import settings
import handlers
import utils

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename="bot.log"
)


def main():
    dp = settings.MYBOT.dispatcher
    jq = settings.MYBOT.job_queue
    time_to_start = datetime.time(hour=9, minute=20)
    jq.run_daily(utils.print_quests, time=time_to_start)
    settings.MYBOT.start_polling()
    while True:
        dp.add_handler(CallbackQueryHandler(handlers.get_state_of_quest))
        time.sleep(5)


if __name__ == '__main__':
    main()
