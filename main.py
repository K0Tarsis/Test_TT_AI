import os
import pickle

from dotenv import load_dotenv
from aiogram import Bot, executor, Dispatcher

import handlers

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot=bot)


def on_shut_down():

    with open('dict_history.pkl', 'wb') as file:
        pickle.dump(handlers.temp_history, file)

    for file_name in os.listdir('temp_voice'):
        os.remove(f'temp_voice/{file_name}')


if __name__ == '__main__':
    handlers.register_handlers(dp)
    executor.start_polling(dp, skip_updates=True)
    on_shut_down()
    print('By')
