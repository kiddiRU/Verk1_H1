"""
Author: Elmar Sigmarsson <elmars25@ru.is>
Date: 2025-12-03

Created the TeamLL class and added the functions
"""

from Models import Team, Player, ValidationError
from DataLayer import DataLayerAPI
from LogicLayer.LogicUtility import get_player_uuid

class TeamLL():

    def __init__(self) -> None:
        pass

    
    def get_team_uuid(self, player: Player) -> str:
        player_uuid = player.uuid
        model_teams: list = DataLayerAPI.load_teams()

        for team in model_teams:
            if player_uuid in team.list_player_uuid:
                self.team_uuid = team.uuid




    def add_player(self, team_uuid: str, player_handle) -> Team:
        """
        Takes in team uuid and a player,
        First looks through all teams to see if the player uuid is already in a team
        then looks through a list of all the teams and 
        finds the right team uuid and
        adds the new player uuid to the teams player list 
        """
        player_uuid: str = get_player_uuid(player_handle)
        model_teams: list = DataLayerAPI.load_teams()
        
        for team in model_teams:
            if player_uuid in team.list_player_uuid:
                raise ValidationError("Player is already in team")

            else:
                for team in model_teams:            
                    if team.uuid == team_uuid:
                        if len(team.list_player_uuid) == 5:
                            raise ValidationError("Max player count in team: 5")

                        else:
                            team.list_player_uuid.append(player_uuid)
                            DataLayerAPI.update_team(team_uuid, team)
                    


    def remove_player(self, team_uuid: str, player_uuid: str) -> Team:
        """
        Takes in team uuid and a player uuid,
        Looks through a list of all the teams and 
        finds the right team uuid and
        checks if the player is the team captain and if so he can not be removed
        otherwise removes the player uuid from the teams player list
        try-except for if the player uuid is not in the team 
        """
        model_teams: list = DataLayerAPI.load_teams()
        for team in model_teams:
            if team.uuid == team_uuid:
                if player_uuid == team.team_captain_uuid:
                    raise ValidationError("Can't remove team captain from team")

                else:
                    try:
                        team.list_player_uuid.remove(player_uuid)
                        DataLayerAPI.update_team(team_uuid, team)

                    except ValueError:
                        raise ValidationError("Player not in team")


    def get_team_members(self, team_uuid: str) -> list:
        """
        Takes in team uuid
        Looks through a list of all the teams and
        finds the right team uuid and
        returns a list of the team members uuid
        """        
        model_teams: list = DataLayerAPI.load_teams()
        for team in model_teams:
            if team.uuid == team_uuid:
                return team.list_player_uuid 
            


    def get_team_info(self, team_uuid: str) -> Team:
        """
        Takes in the uuid
        Looks through a list of all the teams and
        finds the right team uuid and
        returns the model class of the team
        """
        
        model_teams: list = DataLayerAPI.load_teams()
        for team in model_teams:
            if team.uuid == team_uuid:
                return team



    #TODO implement if the team won the tournament add WIN and LOST to if they lost
    def get_team_history(self, team_uuid) -> list:
        """
        Takes in team uuid,
        looks through a list of all the tournaments
        and finds every tournament the team uuid is in (team played in tournament)
        returns a list of those tournaments
        """
        teams_history: list = []

        model_tournaments: list = DataLayerAPI.load_tournaments()
        for tournament in model_tournaments:
            if team_uuid in tournament.teams_playing: 
                teams_history.append(tournament.name)

        return teams_history