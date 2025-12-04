""" 
Author: Kristinn Hrafn <kristinnd25@ru.is>
Date: 2025-12-02

Functions which let you read, write and update players
stored in the ./DataLayer/Repository/players.json
"""

import json
from Models import Player

FILE_PATH = "./DataLayer/Repository/players.json"

"""
Takes in model class Player.

Inserts information about the Player class into a json file
for storage.
"""
def store_player(player: Player) -> None:
    # Changes object player into a dictionary mapping keys to attributes.
    data = player.__dict__
    
    # Reads json file containing players and stores it as a dictionary.
    with open(FILE_PATH, "r") as player_file:
        file_content = dict(json.load(player_file))
    
    # Updates the dictionary adding the new player model into the file content.
    file_content[player.uuid] = data
    
    # Writes the updated file content into the file containing players.
    with open(FILE_PATH, "w") as player_file:
        json.dump(file_content, player_file)


"""
No parameters

Reads json file containing players and creates a list of
Player model objects of each entry in the json file.

Returns the created player list.
"""
def load_players() -> list[Player]:
    # Reads the json file containing players and stores it as a dictionary.
    with open(FILE_PATH, "r") as player_file:
        file_content = dict(json.load(player_file))
    
    # Creates a list of all players in the player_file as a Player model object.
    player_list: list[Player] = []
    for value in file_content.values():
        # Uses **value to unpack the dictionary into a Player model object.
        player_list.append(Player(**value))
        
    return player_list
       
"""
Takes in uuid, key and value as parameters.

uuid and key have to exist in the json file.

Will attempt to find player with given uuid and update the
value tied to given key of that player
"""
def update_player(uuid: str, key: str, value: str) -> None:
    # Reads the json file containing players and stores it as a dictionary.
    with open(FILE_PATH, "r") as player_file:
        file_content = dict(json.load(player_file))
    
    # Updates the file content, checking if the uuid and key exist in
    # the dictionary.
    if uuid in file_content:
        if key in file_content[uuid]:
            file_content[uuid][key] = value

    # Wriets the updated dictionary into the player file.
    with open(FILE_PATH, "w") as player_file:
        json.dump(file_content, player_file)

