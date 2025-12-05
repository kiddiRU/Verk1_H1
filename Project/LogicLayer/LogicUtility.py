"""
Author: Elmar Sigmarsson <elmars25@ru.is>
Date: 2025-12-05

Takes in handles and names of teams, and gets the uuid of them
"""

from DataLayer import DataLayerAPI


def get_player_uuid(self, player_handle):
    """
    Takes in player handle
    looks through all players until it finds the right player
    and returns the player uuid
    """
    model_players: list = DataLayerAPI.load_players()

    for player in model_players:
        if player_handle == player.handle:
            return player.uuid
