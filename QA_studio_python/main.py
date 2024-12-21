import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'd2840f3d646b50b17bc5fcf49d59a550'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}


body_create = {
    "name": "Pika",
    "photo_id": 1
}

body_change = {
    "pokemon_id": "164559",
    "name": "Pika2",
    "photo_id": 1
}


body_add_pokeboll = {
    "pokemon_id": "164559"
}

"""response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)"""

"""response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)"""

"""response_add_pokeboll = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_change)
print(response_add_pokeboll.text)"""
