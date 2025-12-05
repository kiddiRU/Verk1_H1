"""
Author: Kristjan Hagalin <kristjanhj24@ru.is>
Date: 2025-12-03

Logic layer API
"""

from Models import Club, Match, Player, Server, Team, Tournament
from DataLayer import DataLayerAPI
from LogicLayer import PlayerLL
from LogicLayer.Validation import validate_attr

''' Validation API '''
def validate(attr, value, name_type):
    validate_attr(attr, value, name_type)


''' Player API '''
player_logic: PlayerLL = PlayerLL(DataLayerAPI) # Make the API pass validate() to PlayerLL?

def create_player(
        name: str,
        date_of_birth: str, 
        home_address: str,
        email: str,
        phone_number: str, 
        handle: str, 
        url: str = ''
        ) -> Player:

    return player_logic.create_player(
        name,
        date_of_birth,
        home_address,
        email,
        phone_number,
        handle,
        url
    )

def update_player_info(
        player: Player,
        name: str = '',
        date_of_birth: str = '', 
        home_address: str = '',
        email: str = '',
        phone_number: str = '', 
        handle: str = '', 
        url: str = ''
        ) -> None:
    
    return player_logic.update_player_info(
        player,
        name,
        date_of_birth,
        home_address,
        email,
        phone_number,
        handle,
        url
    )

def create_team(name: str, team_captain: Player, club: Club, url: str, ascii_art: str) -> Team:
    return player_logic.create_team(name, team_captain, club, url, ascii_art)

def leave_team(team_name: str, player: Player) -> None:
    return player_logic.leave_team(team_name, player)

''' Team API '''

# TODO implement add_player and call it
def add_player(team: Team, player: Player) -> None:
    pass

# TODO implement remove_player and call it
def remove_player(team: Team, player: Player) -> None:
    pass

# TODO implement get_team_members and call it
def get_team_members(team: Team) -> list[Player]:
    pass

# TODO implement get_team_history and call it
def get_team_history(team: Team) -> list:       
    pass

''' Tournament API '''

# TODO implement validate_unique_name and call it
def validate_unique_name(name: str) -> bool:
    pass

# TODO implement create_tournament and call it
def create_tournament(
        name: str,
        start_date: str,
        end_date: str,
        venue: str,
        teams: dict[Team, list[Player]],
        teams_playing: list[Team],
        email: str,
        phone_number: str,
        status: Tournament.StatusType = Tournament.StatusType.inactive
        # list_of_servers: list[uuid: str] ?
        ) -> Tournament:

    pass

# TODO implement publish and call it
def publish(tournament: Tournament) -> None:
    pass

# TODO implement add_team and call it
def add_team(tournament: Tournament, team: Team) -> None:
    pass

# TODO implement remove_team and call it
def remove_team(tournament: Tournament, team: Team) -> None:
    pass

# TODO implement change_info and call it
def change_info(tournament: Tournament) -> None:
    pass

# TODO implement next_round and call it
def next_round() -> None:
    pass

# TODO implement cancel_tournament and call it
def cancel_tournament(tournament: Tournament) -> None:
    pass

''' Club API '''

# TODO implement validate_unique_name and call it
def validate_unique_name(name: str) -> None:
    pass

# TODO implement create_club and call it
def create_club() -> Club:
    pass

# TODO implement change_club_info and call it
def change_club_info(club: Club) -> None:
    pass

''' Match API '''

# TODO implement input_match_results and call it
def input_match_results(match: Match) -> None:
    pass