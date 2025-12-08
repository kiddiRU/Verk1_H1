""" 
Author: Kristinn Hrafn <kristinnd25@ru.is>
Date: 2025-12-02

Functions which let you read, write and update players
stored in the ./DataLayer/Repository/players.json
"""

import json
from Models import Player

FILE_PATH = "./DataLayer/Repository/players.json"


def store_player(player: Player) -> None:
    # Changes object player into a dictionary mapping attributes to keys.
    data = player.__dict__
    
    # Reads json file containing players and stores the contents as a
    # dictionary.
    with open(FILE_PATH, "r", encoding='utf-8') as player_file:
        file_content = dict(json.load(player_file))
    
    # Adds the new player into the dictionary mapping it's uuid to the
    # object for easy lookup.  
    file_content[player.uuid] = data
    
    # Writes the updated file content back into the json file.
    with open(FILE_PATH, "w", encoding='utf-8') as player_file:
        json.dump(file_content, player_file, indent=4)


def load_players() -> list[Player]:
    # Reads the json file containing players and stores it as a dictionary.
    with open(FILE_PATH, "r", encoding='utf-8') as player_file:
        file_content = dict(json.load(player_file))
    
    # Creates a list of all players in the server file.
    # Each player is stored as a Player model object.
    player_list: list[Player] = []
    for value in file_content.values():
        # Uses **value to unpack the dictionary into a Player model object.
        player_list.append(Player(**value))
        
    return player_list


def update_player(uuid: str, updated_player: Player) -> None:
    # Reads the json file containing players and stores it as a dictionary.
    with open(FILE_PATH, "r", encoding='utf-8') as player_file:
        file_content = dict(json.load(player_file))
   
    # Overwrites the object tied to the given uuid to the object
    # given after checking if it exists to prevent key error.
    if uuid in file_content:
        file_content[uuid] = updated_player.__dict__

    # Writes the updated dictionary back into the player file.
    with open(FILE_PATH, "w", encoding='utf-8') as player_file:
        json.dump(file_content, player_file, indent=4)
