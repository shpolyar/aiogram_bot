import requests

API = 'https://www.fruityvice.com/api/fruit/all'


def get_fruits():
    response = requests.get(API).json()
    return response