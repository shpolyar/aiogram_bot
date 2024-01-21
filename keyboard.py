from aiogram import types

kb = [
    [
        types.KeyboardButton(text='Tell the joke'),
        types.KeyboardButton(text='Random number'),
        types.KeyboardButton(text='Categories'),
        types.KeyboardButton(text='Coffee'),

    ],
]

keyboard = types.ReplyKeyboardMarkup(
    keyboard=kb,
    resize_keyboard=True,
    input_field_placeholder='Choose menu'
)
