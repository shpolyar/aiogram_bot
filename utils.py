import requests

URL = 'https://www.meteosource.com/api/v1/free/point'
API_KEY = 'p205hs6dwmegmom9son902hec7dfa54s1dwjzdxn'


def get_weather(city):
    response = requests.get(URL, params={'key': API_KEY, 'place_id': city}).json()
    return response['current']
