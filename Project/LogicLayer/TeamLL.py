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
    def add_player(self, team_uuid: str, player_uuid: str) -> Team:
        
        model_teams: list = DataLayerAPI.update_team()
        for team in model_teams:
            if team.uuid == team_uuid:
                (team.player).append(player_uuid)
        
        

    #TODO implement letting the captain to remove a player from his team
    def remove_player(self, team_uuid: str, player_uuid: str):

        model_teams: list = DataLayerAPI.update_team()
        for team in model_teams:
            if team.uuid == team_uuid:
                (team.player).remove(player_uuid)
        


    def get_team_members(self, team_uuid):
        pass


    # Every tournament a team has played and the result (WON/LOST)
    def get_team_history():
        pass

