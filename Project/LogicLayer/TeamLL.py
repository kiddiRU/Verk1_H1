"""
Author: Elmar Sigmarsson <elmars25@ru.is>
Date: 2025-12-03

Created the TeamLL class and added the functions
"""

from uuid import uuid4
from DataLayer import DataLayerAPI
from Models.Team import Team

class TeamLL():

    def __init__(self, data_api: DataLayerAPI) -> None:
        self._data_api: DataLayerAPI = data_api


    #TODO implement letting the captain to add player to his team
    def add_player(self, player_uuid) -> Team:
        pass

    #TODO implement letting the captain to remove a player from his team
    def remove_player(self):
        pass


    def get_team_members(self, team_uuid):
        pass


    # Every tournament a team has played and the result (WON/LOST)
    def get_team_history():
        pass

