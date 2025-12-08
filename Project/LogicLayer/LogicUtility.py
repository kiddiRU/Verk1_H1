"""
Author: Elmar Sigmarsson <elmars25@ru.is>
Date: 2025-12-05

Takes in handles and names of teams, and gets the uuid of them
"""

from DataLayer import DataLayerAPI
from Models import ValidationError


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



def get_players_team_uuid(player_handle) -> str:
    """
    Takes in player handle
    looks through all teams until it finds the player in a team
    and returns the teams uuid
    If no player is found an error is raised
    """
    model_teams: list = DataLayerAPI.load_teams()
    player_uuid = get_player_uuid(player_handle)
    for team in model_teams:
        if player_uuid in team.list_player_uuid:
            return team.uuid
        
    raise ValidationError("Player not found in any team")



def get_team_uuid(team_name):
    """
    Takes in team name
    looks through all teams until it finds the team name
    and returns the teams uuid
    if no team is found an error is raised
    """
    model_teams: list = DataLayerAPI.load_teams()
    for team in model_teams:
        if team_name == team.name:
            return team.uuid
    
    raise ValidationError("Team not found")



def get_club_uuid(club_name):
    """
    Takes in club name
    looks through all clubs until it finds the right club name
    and returns the teams uuid
    if no team is found an error is raised
    """

    model_clubs: list = DataLayerAPI.load_clubs()
    for club in model_clubs:
        if club_name == club.name:
            return club.uuid
        
    raise ValidationError("Club not found")