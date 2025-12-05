"""
Author: Elmar Sigmarsson <elmars25@ru.is>
Date: 2025-12-05

Takes in handles and names of teams, and gets the uuid of them
"""

from DataLayer import DataLayerAPI
from Models.Exception import ValidationError


def get_player_uuid(player_handle) -> str:
    """
    Takes in player handle
    looks through all players until it finds the right player
    and returns the player uuid
    If no player is found an error is raised
    """
    model_players: list = DataLayerAPI.load_players()
    for player in model_players:
        if player_handle == player.handle:
            return player.uuid
        
    raise ValidationError("Player not found")
