import requests
import pytest

url = 'https://api.pokemonbattle.ru/v2'
token = 'TOKEN'
headers = {
    'Content-Type' : 'application/json',
    'trainer_token' : token
}
trainer_id = '7593'
trainer_name = 'Crashoveride'

def test_status_code():
    response_get_trainers = requests.get(url=f'{url}/trainers', headers=headers)
    assert response_get_trainers.status_code == 200

def test_trainer_id():
    response_get_my_trainer = requests.get(url=f'{url}/trainers', headers=headers, params = {'trainer_id' : trainer_id})
    assert response_get_my_trainer.json()['data'][0]['trainer_name'] == trainer_name
