"""
Author: Kristjan Hagalin <kristjanhj24@ru.is>
Date: 2025-12-03

Minor change: Andri Már Kristjánsson <andrik25@ru.is>

Logic layer API.
"""

from Models import Club, Match, Player, Server, Team, Tournament
from LogicLayer import PlayerLL, TeamLL, TournamentLL, ClubLL
from LogicLayer.Validation import validate_attr
from datetime import date, time

''' Validation API '''
def validate(attr: str, value: str, name_type: str):
    return validate_attr(attr, value, name_type)

''' Player API '''
player_logic = PlayerLL()

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
    
    player_logic.update_player_info(
        player,
        name,
        date_of_birth,
        home_address,
        email,
        phone_number,
        handle,
        url
    )

def create_team(name: str, team_captain: Player, club_name: str, url: str, ascii_art: str) -> Team:
    return player_logic.create_team(name, team_captain, club_name, url, ascii_art)

def leave_team(team_name: str, player: Player) -> None:
    return player_logic.leave_team(team_name, player)

def list_players() -> list[Player]:
    return player_logic.list_players()

def get_player_object(player_handle: str) -> Player | None:
    return player_logic.get_player_object(player_handle)

def promote_captain(current_player: Player, handle_to_promote: str) -> None:
    player_logic.promote_captain(current_player, handle_to_promote)

''' Team API '''
team_logic = TeamLL()

# TODO implement add_player and call it
def add_player(player_handle: str, current_player: Player) -> Team:
    return team_logic.add_player(player_handle, current_player)

# TODO implement remove_player and call it
def remove_player(player_handle: str, current_player: Player) -> Team:
    return team_logic.remove_player(player_handle, current_player)

# TODO implement get_team_members and call it
def get_team_members(team_name: str) -> list[str]:
    return team_logic.get_team_members(team_name)

def list_teams() -> list[Team]:
    return team_logic.list_teams()

def get_team_object(team_name: str) -> Team:
    return team_logic.get_team_object(team_name)

# TODO implement get_team_history and call it
def get_team_history(team_name: str) -> list[str]:       
    return team_logic.get_team_history(team_name)

def get_team_wins(team_name: str) -> str:
    return team_logic.get_team_wins(team_name)

def get_team_points(team_name: str) -> str:
    return team_logic.get_team_points(team_name)

''' Tournament API '''
tournament_logic = TournamentLL()

def create_tournament(
    name: str,
    start_date: date,
    end_date: date,
    time_frame_start: time,
    time_frame_end: time, 
    venue: str,
    email: str,
    phone_number: str,
    amount_of_servers: int = 1
) -> None:

    return tournament_logic.create_tournament(
        name,
        start_date,
        end_date,
        time_frame_start,
        time_frame_end, 
        venue,
        email,
        phone_number,
        amount_of_servers
    )

def publish(tournament_name: str) -> None:
    tournament_logic.publish(tournament_name)

def add_team(tournament_name: str, team_name: str) -> None:
    tournament_logic.add_team(tournament_name, team_name)

def remove_team(tournament_name: str, team_name: str) -> None:
    tournament_logic.remove_team(tournament_name, team_name)

def update_tournament_info(
    tournament_name: str = '',
    venue: str = '',
    email: str = '',
    phone_number: str = ''
) -> None:
    
    tournament_logic.update_info(
        tournament_name,
        venue,
        email,
        phone_number
    )

def update_tournament_datetime(
    tournament_name: str,
    start_date: date,
    end_date: date,
    time_frame_start: time,
    time_frame_end: time,
) -> None:
    
    tournament_logic.update_tournament_datetime(
        tournament_name,
        start_date,
        end_date,
        time_frame_start,
        time_frame_end
    )

def list_tournaments() -> list[Tournament]:
    return tournament_logic.list_tournaments()

# TODO implement next_round and call it
def next_round() -> None:
    pass

# TODO implement cancel_tournament and call it (C Requirement)
def cancel_tournament(tournament: Tournament) -> None:
    pass

''' Club API '''
club_logic: ClubLL =  ClubLL()

# TODO implement create_club and call it
def create_club(name: str, club_color: str, country: str, home_town: str) -> Club:
    return club_logic.create_club(name,club_color, country, home_town)

def list_clubs() -> list[Club]:
    return club_logic.list_clubs()

def get_teams_in_club(club_name: str) -> list[Team]:
    return club_logic.get_teams_in_club(club_name)

# TODO implement change_club_info and call it
def change_club_info(club: Club) -> None:
    pass

''' Match API '''

# TODO implement input_match_results and call it
def input_match_results(match: Match) -> None:
    pass


def save_player(player_handle: str | None = None) -> str | None:
    return player_logic.save_player(player_handle)


def get_player_team(player_handle: str) -> tuple:
    return player_logic.get_player_team(player_handle)

def get_team_club(team_name: str) -> str:
    return team_logic.get_team_club(team_name)