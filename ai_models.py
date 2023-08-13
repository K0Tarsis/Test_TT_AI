import os
import openai

from dotenv import load_dotenv
from gtts import gTTS

from constant import *

load_dotenv()
OPENAI_TOKEN = os.getenv("OPENAI_TOKEN")
openai.api_key = OPENAI_TOKEN

def gen_start_message(language):
    return \
        [
            {"role": "system", "content": START_CONTENT % LANGUAGES[language]},
            {"role": "assistant", "content": AI_INTRODUCTION[language]}
        ]


async def voice_chat(user_message: str, user_id: int, user_info: dict = None):

    language = user_info[LANGUAGE] if user_info[LANGUAGE] else 'en'
    messages = user_info[HISTORY] if user_info[HISTORY] else gen_start_message(language)
    messages.append({"role": "user", "content": user_message})

    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )

    reply = chat.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})

    file_name = TEMP_VOICE_FILES % user_id
    audio = gTTS(text=reply, lang=language, slow=False)
    audio.save(file_name)

    print(LOG_MSG % (user_id, user_message, reply))

    return reply, file_name, messages

# Not necessary, takes a lot of time
# def define_language(user_message: str):
#     prompt = f"Tell me what language this is: ```{user_message}```, " \
#              f"response in format like this '''Language:=uk''' for Ukrainian," \
#              f" if you cant determinate language write: 'None'"
#
#     l_messages = [{"role": "user", "content": prompt}]
#
#     chat = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo", messages=l_messages
#     )
#
#     reply = chat.choices[0].message.content.split(':=')
#
#     return reply[1] if len(reply) > 1 else None
