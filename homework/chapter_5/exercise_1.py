# 1. Fetch Data from API and Save Locally. Pull Pokemon data from the PokeAPI and save
# it to a local file. The local JSON file should contain Pokemon data for Bulbasaur (ID:
# 1)
# import requests
# import json
# data_api = "https://pokeapi.co/api/v2/pokemon/1/"
# local_file = "pokemon_data.json"
# # TODO:
# # 1. Make a GET request to data_api
# # 2. Extract the JSON response
# # 3. Write the JSON data to local_file

import requests
import json
data_api = "https://pokeapi.co/api/v2/pokemon/1/"
local_file = "pokemon_data.json"

response = requests.get(data_api)
if response.status_code == 200:
    json_response = response.json()
    with open(local_file, "w") as f:
        json.dump(response.json(), f)
