import pyjokes
import random
from aiogram import types, F, Router
import requests
from utils import get_fruits

test_router = Router()


@test_router.message(F.text == 'Tell the joke')
async def joke(message: types.Message):
    # logging.info('Tell the joke')
    my_joke = pyjokes.get_joke()
    await message.answer(my_joke)


@test_router.message(F.text == 'Random number')
async def rand_int(message: types.Message):
    ran = random.randint(1, 10000)
    await message.answer(str(ran))


@test_router.message(F.text == 'Categories')
async def category(message: types.Message):
    await message.answer('Wait please...')
    for num, item in enumerate(get_fruits()):
        if num == 5:
            break
        card = \
            f'Name of fruit - {item.get("name")}\n' \
            # f'Name of fruit - {item.get("name")}\n' \
        # f'Name of fruit - {item.get("name")}\n' \
        await message.answer(card)


@test_router.message(F.text == 'Coffee')
async def coffee(message: types.Message):
    api = 'https://coffee.alexflipnote.dev/random.json'
    await message.answer('Wait please...')
    response = requests.get(api).json()
    card = f'Coffee: {response["file"]}'
    await message.answer(card)

