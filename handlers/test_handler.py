from aiogram import types, F, Router
from utils import get_weather
from aiogram.methods import SendPhoto
from aiogram.utils.markdown import hbold

test_router = Router()

CITY = [
    'Kyiv',
    'Odessa',
    'Lviv',
    'Kharkiv',
    'Vinnytsya',
    'Ivano-Frankivsk',
    'Chernihiv',
    'Dnipro',
    'Rivne'
]


@test_router.message(F.text.in_(CITY))
async def weather(message: types.Message):
    city = message.text
    resp = get_weather(city.lower().replace('-', ''))
    photo_path = f'set03/big/{resp["icon_num"]}.png'
    photo = types.FSInputFile(photo_path)
    card = \
        f'City: {hbold(city)}\n' \
        f'Weather: {resp["summary"]}\n' \
        f'Speed of wind: {resp["wind"]["speed"]}\n' \
        f'Temperature: {resp["temperature"]}\n' \

    await message.answer_photo(photo, caption=card)
