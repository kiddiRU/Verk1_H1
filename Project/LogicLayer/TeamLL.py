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
        
        model_teams: list = DataLayerAPI.load_teams()
        for team in model_teams:
            if team.uuid == team_uuid:
                team.list_player_uuid.append(player_uuid)
                DataLayerAPI.update_team(team_uuid, "list_player_uuid", team.list_player_uuid)
                

    #TODO implement letting the captain to remove a player from his team
    def remove_player(self, team_uuid: str, player_uuid: str) -> Team:

        model_teams: list = DataLayerAPI.load_teams()
        for team in model_teams:
            if team.uuid == team_uuid:
                team.list_player_uuid.remove(player_uuid)
                DataLayerAPI.update_team(team_uuid, "list_player_uuid", team.list_player_uuid)
        


    def get_team_members(self, team_uuid) -> list:
        
        model_teams: list = DataLayerAPI.load_teams()
        for team in model_teams:
            if team.uuid == team_uuid:
                return team.list_player_uuid 


    # Every tournament a team has played and the result (WON/LOST)
    def get_team_history():
        pass

