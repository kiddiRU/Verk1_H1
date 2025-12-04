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



    def add_player(self, team_uuid: str, player_uuid: str) -> Team:
        
        model_teams: list = DataLayerAPI.load_teams()
        for team in model_teams:
            if team.uuid == team_uuid:
                if len(team.list_player_uuid) == 5:
                    continue

                else:
                    team.list_player_uuid.append(player_uuid)
                    DataLayerAPI.update_team(team_uuid, team)
                


    def remove_player(self, team_uuid: str, player_uuid: str) -> Team:

        model_teams: list = DataLayerAPI.load_teams()
        for team in model_teams:
            if team.uuid == team_uuid:
                team.list_player_uuid.remove(player_uuid)
                DataLayerAPI.update_team(team_uuid, team)
        


    def get_team_members(self, team_uuid: str) -> list:
        
        model_teams: list = DataLayerAPI.load_teams()
        for team in model_teams:
            if team.uuid == team_uuid:
                return team.list_player_uuid 



    #TODO implement if the team won the tournament add WIN and LOST to if they lost
    def get_team_history(self, team_uuid) -> list:
        
        teams_history: list = []

        model_tournaments: list = DataLayerAPI.load_tournaments()
        for tournament in model_tournaments:
            if team_uuid in tournament.teams_playing: 
                teams_history.append(tournament.name)

        return teams_history