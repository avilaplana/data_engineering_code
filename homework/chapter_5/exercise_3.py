# 3. Parse Data and Insert into SQLite Database. Extract specific Pokemon attributes and
# store them in a SQLite database.
# Table Schema:
# CREATE TABLE pokemon (
# id INTEGER PRIMARY KEY,
# name TEXT NOT NULL,
# base_experience INTEGER
# );
# import sqlite3
# import json
# local_file = "pokemon_data.json"
# database_file = "pokemon.db"
# # TODO:
# # 1. Create a SQLite3 connection and table with columns: id, name, base_experience
# # 2. Open and read the local_file using Python standard libraries
# # 3. Parse the JSON data to extract id, name, and base_experience
# # 4. Insert the extracted data into the SQLite table
# # 5. Verify insertion by querying and printing the data

import sqlite3
import json
local_file = "pokemon_data.json"
database_file = "pokemon.db"

sql_connection = sqlite3.connect(database_file)
create_statement = """CREATE TABLE IF NOT EXISTS pokemon (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    base_experience INTEGER
    );"""

sql_connection.execute(create_statement)

with open(local_file, "r") as f:
    data = json.load(f)
    id = data['id']
    name = data['name']
    base_experience = data['base_experience']
    sql_connection.execute(
        "INSERT INTO pokemon (id, name, base_experience) VALUES (?, ?, ?);",
        (id, name, base_experience)
    )

sql_connection.commit()
cursor = sql_connection.cursor()
cursor.execute("SELECT * FROM pokemon")
rows = cursor.fetchall()

print("All Pokémon in DB:")
for row in rows:
    # row is a tuple (id, name, base_experience)
    print(row)

sql_connection.close()
