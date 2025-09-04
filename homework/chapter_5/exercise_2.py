# 2. Read and Display Local File Contents. Read the previously saved JSON file and print
# its name and id.
# TODO:
# 1. Use Python standard libraries to open local_file and dump the contents into a json
# 2. Read the name and id from the json

import json
local_file = "pokemon_data.json"
with open(local_file, "r") as f:
    data = json.load(f)

print(f"the name of the pokemon is {data['name']}")
print(f"the id of the pokemon is {data['id']}")