#CONNECT TO API

import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    responce = requests.get(url)
    
    if responce.status_code == 200:
      pokemon_data = responce.json()
      return pokemon_data
    else:
        print(f"Failed to retrieve info. {responce.status_code}")

pokemon_name = "pikachu"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
   print(f"{pokemon_info["height"]}")