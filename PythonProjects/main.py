import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '861ca777961a5cf288e37ba95ef76828'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}


body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

pokemon_id = response_create.json()['id'] 


body_change = {
    "pokemon_id": "184865",
    "name": "Ежик",
    "photo_id": 18 
}
response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)

message = response_change.json()['message']
print(message)


body_pokeboll = {
    "pokemon_id": "184957"
}

respons_pokeboll = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeboll)
print(respons_pokeboll.text)

message = respons_pokeboll.json()['message']
print(message)

