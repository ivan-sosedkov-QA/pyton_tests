import requests

URL='https://api.pokemonbattle.ru/v2'
TOKEN='b6d2abb9ebdc67dc10212d1c22f8ae0e'
HEADER={'Content-type':'application/json', 'trainer_token' : TOKEN}

body_registracion ={
     "trainer_token": TOKEN,
    "email": "tranzit_net1@mail.ru",
    "password": "AdmSii!190369"
}

body_confirm = {
    "trainer_token": TOKEN
}


body_create = {
"name": "generate",
"photo_id": -1
}

body_rename = {
     "pokemon_id": "68618",
    "name": "newwan",
    "photo_id": 2
}


body_pokeball = {
     "pokemon_id": "68618"
}

'''response_registracion= requests.post(url= f'{URL}/trainers/reg', headers=HEADER, json=body_registracion)
print(response_registracion.text)
'''

'''response_confirm= requests.post(url= f'{URL}/trainers/confirm_email', headers=HEADER, json=body_confirm)
print(response_confirm.text)'''

response_create= requests.post(url= f'{URL}/pokemons', headers=HEADER, json=body_create)

print(response_create.text)

pokemons_id=response_create.json()['id']

response_rename= requests.put(url= f'{URL}/pokemons', headers=HEADER, json=body_rename)

print(response_rename.text)

response_pokeball= requests.post(url= f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_pokeball)

print(response_pokeball.text)