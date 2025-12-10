"""
Author: Kristjan Hagalin <kristjanhj24@ru.is>
Date: 2025-12-03

Minor change: Andri Már Kristjánsson <andrik25@ru.is>

Logic layer API.
"""

from Models import Club, Match, Player, Server, Team, Tournament
from LogicLayer import PlayerLL, TeamLL, TournamentLL, ClubLL, LogicUtility, MatchLL
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

def get_player_object(player_uuid: str) -> Player | str:
    return player_logic.get_player_object(player_uuid)

def promote_captain(current_player: Player, handle_to_promote: str) -> None:
    player_logic.promote_captain(current_player, handle_to_promote)

def save_player(player_handle: str | None = None) -> str | None:
    return player_logic.save_player(player_handle)

def get_player_team(player_handle: str) -> tuple:
    return player_logic.get_player_team(player_handle)

def get_player_wins(player_handle: str) -> str:
    return player_logic.get_player_wins(player_handle)

def get_player_points(player_handle: str) -> str:
    return player_logic.get_player_points(player_handle)


# "Created" by Sindri Freysson
def get_player_points(player_handle) -> str:
    return player_logic.get_player_points(player_handle)
''' Team API '''
team_logic = TeamLL()

# TODO implement add_player and call it
def add_player(player_handle: str, current_player: Player) -> Team | str:
    return team_logic.add_player(player_handle, current_player)

# TODO implement remove_player and call it
def remove_player(player_handle: str, current_player: Player) -> Team:
    return team_logic.remove_player(player_handle, current_player)

# TODO implement get_team_members and call it
def get_team_members(team_name: str) -> list[str]:
    return team_logic.get_team_members(team_name)

def get_team_members_object(team_name: str) -> list[Player]:
    return team_logic.get_team_members_object(team_name)

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

def get_team_club(team_name: str) -> str:
    return team_logic.get_team_club(team_name)


''' Tournament API '''
tournament_logic = TournamentLL()
match_logic = MatchLL()

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

def change_match_winner(
        tournament_uuid: str,
        match_uuid: str,
        team_uuid: str
    ) -> None:
    tournament_logic.change_match_winner(
            tournament_uuid,
            match_uuid,
            team_uuid
        )

def get_all_matches(tournament_uuid: str) -> list[Match]:
    """
    Parameters: uuid of tournaemnt

    Returns a list of all matches in the tournament
    tied to the uuid given.
    """
    return match_logic.get_matches(tournament_uuid)

def get_next_matches(tournament_uuid: str) -> list[Match]:
    """
    Parameters: uuid of tournament

    Returns a list of matches which are next on the schedule,
    matches next in the schedule are matches which don't have
    a winner and there doesn't exist a match which happens
    before it and needs a winner.
    """
    return tournament_logic.next_games(tournament_uuid)


# TODO implement cancel_tournament and call it (C Requirement)
def cancel_tournament(tournament: Tournament) -> None:
    pass

def get_teams_from_tournament_name(tournament_name) -> list[Team]:
    return tournament_logic.get_teams_from_tournament_name(tournament_name)

# TO help create a Tournament
def to_time(value: str) -> time:
    return tournament_logic.to_time(value)

def to_date(value: str) -> date:
    return tournament_logic.to_date(value)

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

def get_club_wins(club_name: str) -> str:
    return club_logic.get_club_wins(club_name)

def get_club_points(club_name: str) -> str:
    return club_logic.get_club_points(club_name)

# Is using depracated UtilityLogic
def get_club_by_name(club_name) -> Club:
    return LogicUtility.get_club_by_name(club_name)

''' Match API '''

# TODO implement input_match_results and call it
def input_match_results(match: Match) -> None:
    pass

# Created by Sindri
def get_club_wins(club_name) -> str:
    return club_logic.get_club_wins(club_name)

# Created by Sindri
def get_club_points(club_name) -> str:
    return club_logic.get_club_points(club_name)


""" Utility API """

def get_player_uuid(player_handle: str) -> str:
    return LogicUtility.get_player_uuid(player_handle)

def get_players_team_uuid(team_name: str) -> str:
    return LogicUtility.get_players_team_uuid(team_name)

def get_tournament_by_name(tournament_name: str) -> Tournament:
    return LogicUtility.get_tournament_by_name(tournament_name)

def tournament_name_to_uuid(uuid: str) -> str:
    return LogicUtility.tournament_name_to_uuid(uuid)

def get_team_by_name(team_name: str) -> Team:
    return LogicUtility.get_team_by_name(team_name)

def get_team_by_uuid(team_uuid: str) -> Team:
    return LogicUtility.get_team_by_name(team_uuid)

