import pickle
import time

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

import ai_models
from constant import *
from keyboards import language_keyboard
from main import bot


try:

    with open(TEMP_HISTORY_FILE, 'rb') as file:
        temp_history = pickle.load(file)

except (IOError, EOFError):
    temp_history = {}


async def commands_start(msg: types.Message):
    await msg.answer(CHOSE_LANGUAGE_MSG, reply_markup=language_keyboard)


async def change_language(callback: types.CallbackQuery):
    language = callback.data.split(' ')[-1] if callback.data.split(' ')[-1] in LANGUAGES.keys() else 'en'
    user_id = callback.from_user.id
    temp_history[user_id] = {LANGUAGE: language, HISTORY: None}
    await bot.send_message(user_id, AI_INTRODUCTION[language])


async def conversations(msg: types.Message):
    user_info = temp_history.get(msg.from_user.id, None)
    
    if not user_info:
        temp_history[msg.from_user.id] = {LANGUAGE: 'en', HISTORY: None}
        user_info = temp_history[msg.from_user.id]

    start_time = time.time()
    reply, audio, messages = await ai_models.voice_chat(msg.text, msg.from_user.id, user_info)
    time_spent = time.time() - start_time

    temp_history[msg.from_user.id][HISTORY] = messages

    if SYSTEM_MESSAGE_CONLUSION in reply:

        conclusion = reply.split(SYSTEM_MESSAGE_CONLUSION)[-1].strip()
        await msg.answer(LAST_MESSAGE[temp_history[msg.from_user.id][LANGUAGE]])
        await msg.answer('Its chatgpt conclusion:\n' + conclusion)

        temp_history[msg.from_user.id][HISTORY] = \
            [
                {"role": "system", "content":
                    START_CONTENT % LANGUAGES[temp_history[msg.from_user.id][LANGUAGE]]},
                {"role": "system", "content": f"Your previous conclusion about client:\n{reply}"}
            ]

    else:
        await msg.answer(reply + f'\nTime for an answer: {time_spent}')
        await bot.send_voice(msg.from_user.id, voice=open(audio, 'rb'))


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_callback_query_handler(change_language, Text(startswith="/language"))
    dp.register_message_handler(conversations)
