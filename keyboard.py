from aiogram import types

kb = [
    [
        types.KeyboardButton(text='Kyiv'),
        types.KeyboardButton(text='Odessa'),
        types.KeyboardButton(text='Lviv'),
    ],
    [
        types.KeyboardButton(text='Kharkiv'),
        types.KeyboardButton(text='Vinnytsya'),
        types.KeyboardButton(text='Ivano-Frankivsk'),
    ],
    [
        types.KeyboardButton(text='Chernihiv'),
        types.KeyboardButton(text='Dnipro'),
        types.KeyboardButton(text='Rivne'),
    ]
]

keyboard = types.ReplyKeyboardMarkup(
    keyboard=kb,
    resize_keyboard=True,
    input_field_placeholder="Enter your city...",
)
