import os
import pickle

from dotenv import load_dotenv
from aiogram import Bot, executor, Dispatcher
from aiogram.utils.exceptions import TelegramAPIError
from constant import *

import handlers


load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot=bot)


def on_shut_down():
    with open(TEMP_HISTORY_FILE, 'wb') as file:
        pickle.dump(handlers.temp_history, file)

    for file_name in os.listdir(TEMP_VOICE_DIRECTORY):
        os.remove(f'{TEMP_VOICE_DIRECTORY}/{file_name}')

def main_start():
    try:
        handlers.register_handlers(dp)
        executor.start_polling(dp, skip_updates=True)

    except TelegramAPIError:
        print(TELEGRAM_SERVERS_ERROR_MSG)
        main_start()

    else:
        print(OTHER_CRITICAL_ERROR_MSG)

if __name__ == '__main__':
    main_start()
    on_shut_down()
    print('By')
