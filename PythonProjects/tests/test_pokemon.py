import requests
import pytest

URL='https://api.pokemonbattle.ru/v2'
TOKEN='b6d2abb9ebdc67dc10212d1c22f8ae0e'
HEADER={'Content-type':'application/json', 'trainer_token' : TOKEN}
TRAINER_ID='9943'

def test_status_code() : 
    response = requests.get(url= f'{URL}/pokemons', params={'trainer_id': TRAINER_ID})

    assert response.status_code == 200

def test_part_of_response() :
    response_get = requests.get(url= f'{URL}/trainers', params={'trainer_id': TRAINER_ID})

    assert response_get.json()["data"][0]["trainer_name"] == 'Иван'


@pytest.mark.parametrize('key, value', [('trainer_id', TRAINER_ID), ('id', '68619')])
def test_param  (key, value):
    response_param= requests.get(url= f'{URL}/pokemons', params={'trainer_id': TRAINER_ID})
    assert response_param.json()["data"][0][key] == value


