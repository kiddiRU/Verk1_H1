""" 
Author: Kristinn Hrafn
Date: 2025-12-02

Functions which let you read, write and update players
stored in the ./DataLayer/Repository/players.json
"""

import json
from Models.Player import Player

FILE_PATH = "./DataLayer/Repository/players.json"

"""
Takes in model class Player.
Inserts information about the Player class into a json file for storage.
"""
def store_player(player: Player) -> None:
    data = {
        "name": player.name, 
        "date_of_birth": player.date_of_birth,
        "home_address": player.home_address,
        "email": player.email,
        "phone_number": player.phone_number,
        "handle": player.handle,
        "url": player.url
    }
        
    with open(FILE_PATH, "r") as player_file:
        file_content = dict(json.load(player_file))

    file_content[player.uuid] = data
        
    with open(FILE_PATH, "w") as player_file:
        json.dump(file_content, player_file)


"""
No parameters
Reads json file containing players and creates a list of Player model objects of each entry in the json file.
Returns the created player list.
"""
def load_players() -> list[Player]:
    with open(FILE_PATH, "r") as player_file:
        file_content = dict(json.load(player_file))
        
    player_list = []
    for uuid, value in file_content.items():
        player.append(Player(uuid,
                             value["name"],
                             value["date_of_birth"],
                             value["home_address"],
                             value["email"],
                             value["phone_number"],
                             value["handle"],
                             value["url"],))
        
    return player_list
       
"""
Takes in uuid, key and value as parameters.
uuid and key have to exist in the json file.
Will update the value tied to the key given of the player with the given uuid.
"""
def update_player(uuid: str, key: str, value: str) -> None:
    with open(FILE_PATH, "r") as player_file:
        file_content = dict(json.load(player_file))

    if uuid in file_content:
        file_content[uuid][key] = value

    with open(FILE_PATH, "w") as player_file:
        json.dump(file_content, player_file)

