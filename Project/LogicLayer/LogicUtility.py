"""
Author: Elmar Sigmarsson <elmars25@ru.is>
Date: 2025-12-05

Takes in handles and names of teams, and gets the uuid of them
"""

from DataLayer import DataLayerAPI
from Models import Team, Tournament, ValidationError


def get_player_uuid(player_handle: str) -> str:
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
        
    return ValidationError("Player not found")



def get_players_team_uuid(player_uuid) -> str:
    """
    Takes in player handle
    looks through all teams until it finds the player in a team
    and returns the teams uuid
    If no player is found an error is raised
    """
    model_teams: list = DataLayerAPI.load_teams()
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



def get_club_by_name(club_name) -> Club:
    """
    Takes in club name
    looks through all clubs until it finds the right club name
    and returns the teams uuid
    if no team is found an error is raised
    """

    model_clubs: list = DataLayerAPI.load_clubs()
    for club in model_clubs:
        if club_name == club.name:
            return club
        
    raise ValidationError("Club not found")

def get_tournament_by_name(name: str) -> Tournament:
        tournaments: list[Tournament] = DataLayerAPI.load_tournaments()
        tournament: Tournament | None = next((t for t in tournaments if t.name == name), None)

        if tournament is None:
            raise Exception(f'No tournament found named: {name}')
        
        return tournament


def tournament_name_to_uuid(uuid: str) -> str:
        tournaments: list[Tournament] = DataLayerAPI.load_tournaments()
        tournament: Tournament | None = next((t for t in tournaments if t.uuid == uuid), None)

        if tournament is None:
            raise Exception(f'No tournament found named: {uuid}')
        
        return tournament.name
    
def get_team_by_name(name: str) -> Team:
    teams: list[Team] = DataLayerAPI.load_teams()
    team: Team | None = next((t for t in teams if t.name == name), None)

    if team is None:
        raise Exception(f'No team found named: {name}')
    
    return team

def get_team_by_uuid(uuid: str) -> Team:
    teams: list[Team] = DataLayerAPI.load_teams()
    team: Team | None = next((t for t in teams if t.uuid == uuid), None)

    if team is None:
        raise Exception(f'No team found with the UUID: {uuid}')
    
    return team