import requests

url = 'https://api.pokemonbattle.ru/v2'
token = 'TOKEN'
headers = {
    'Content-Type' : 'application/json',
    'trainer_token' : token
}

# Создание покемона
body_create_pokemon = {
    "name": "generate",
    "photo_id": -1
}
response_create_pokemon = requests.post(url=f'{url}/pokemons', headers=headers, json=body_create_pokemon)
print(response_create_pokemon.text)

# Получение ID созданного покемона
pokemon_id = response_create_pokemon.json().get('id')

# Изменение имени покемона
change_name_pokemon = {
    "pokemon_id": pokemon_id,
    "name": "generate",
    "photo_id": -1
}
response_change_name = requests.put(url=f'{url}/pokemons', headers=headers, json=change_name_pokemon)
print(response_change_name.text)

# Поймать покемона в покебол
catch_in_pokeball = {
    "pokemon_id": pokemon_id
}
response_catch = requests.post(url=f'{url}/trainers/add_pokeball', headers=headers, json=catch_in_pokeball)
print(response_catch.text)
