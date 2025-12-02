""" 
Author: Kristinn Hrafn
Date: 2025-12-02

Class which let's you read, write and update players
stored in the ./DataLayer/Repository/players.json
"""

import json
from Models.Player import Player

FILE_PATH = "Repository/players.json"

class PlayerIO:
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
        with open(FILE_PATH, "w") as player_file:
            json.dump(date, player_file)
