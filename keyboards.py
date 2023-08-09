from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

language_keyboard = InlineKeyboardMarkup(row_width=1)
b1m = InlineKeyboardButton(text='Українська', callback_data=f'/language uk')
b2m = InlineKeyboardButton(text='English', callback_data=f'/language en')
language_keyboard.add(b1m)
language_keyboard.add(b2m)
