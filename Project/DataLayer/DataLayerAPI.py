"""
Author: Kristinn Hrafn <kristinnd25@ru.is>
Date: 2025-12-03

Data layer API
"""

from Models import Club, Match, Player, Server, Team, Tournament
from DataLayer import PlayerIO, TeamIO, TournamentIO, ClubIO, MatchIO, ServerIO

""" Player API """

def store_player(player: Player) -> None:
    """
    Args: Model class Player
    
    Store new players in a json file to be fetched later.
    """
    PlayerIO.store_player(player)

def load_players() -> list[Player]:
    """
    Args: None

    Returns a list of all players stored with the store_player function
    as a model class Player object.
    """
    return PlayerIO.load_players()

def update_player(uuid: str, updated_player: Player) -> None:
    """
    Args: uuid and model class Player

    Looks up the player with given uuid and updates them to the given
    Player object.
    """
    PlayerIO.update_player(uuid, updated_player)

""" Team API """

def store_team(team: Team) -> None:
    """
    Args: Model class Team

    Store new teams in a json file to be fetched later.
    """
    TeamIO.store_team(team)

def load_teams() -> list[Team]:
    """
    Args: None

    Returns a list of all teams stored with the store_team function
    as a model class Team object.
    """
    return TeamIO.load_teams()

def update_team(uuid: str, updated_team: Team) -> None:
    """
    Args: uuid and model class Team

    Looks up the team with given uuid and updates them to the given
    Team object.
    """
    TeamIO.update_team(uuid, updated_team)

""" Club API """

def store_club(club: Club) -> None:
    """
    Args: Model class Club

    Store new clubs in a json file to be fetched later.
    """
    ClubIO.store_club(club)

def load_clubs() -> list[Club]:
    """
    Args: None

    Returns a list of all clubs stored with the store_club function
    as a model class Club object.
    """
    return ClubIO.load_club()

def update_club(uuid: str, updated_club: Club) -> None:
    """
    Args: uuid and Model class Club

    Looks up the club with given uuid and updates them to the given
    Club object.
    """
    ClubIO.update_club(uuid, updated_club)

""" Tournament API """

def store_tournament(tournament: Tournament) -> None:
    """
    Args: Model class Tournament

    Store new tournaments in a json file to be fetched later.
    """
    TournamentIO.store_tournament(tournament)

def load_tournaments() -> list[Tournament]:
    """
    Args: None

    Returns a list of all tournaments stored with the store_tournament function
    as a Model class Tournament object.
    """
    return TournamentIO.load_tournaments()

def update_tournament(uuid: str, updated_tournament: Tournament) -> None:
    """
    Args: uuid and model class Tournament

    Looks up the Tournament with given uuid and updates them to the given
    Tournament object.
    """
    TournamentIO.update_tournament(uuid, updated_tournament)

""" Match API """

def store_match(match: Match) -> None:
    """
    Args: Model class Match

    Store new matches in a json file to be fetched later.
    """
    MatchIO.store_match(match)

def load_matches() -> list[Match]:
    """
    Args: None

    Returns a list of all matches stored with the store_match function
    as a model class Match object.
    """
    return MatchIO.load_match()

def update_match(uuid: str, updated_match: Match) -> None:
    """
    Args: uuid and model class Match

    Looks up the Match with given uuid and updates them to the given
    Match object.
    """
    MatchIO.update_match(uuid, updated_match)

""" Server API """

def store_server(server: Server) -> None:
    """
    Args: Model class Server

    Store new servers in a json file to be fetched later.
    """
    ServerIO.store_server(server)

def load_servers() -> list[Server]:
    """
    Args: None

    Returns a list of all servers stored with the store_server function
    as a model class Server object.
    """
    return ServerIO.load_server()

def update_server(uuid: str, updated_server: Server) -> None:
    """
    Args: uuid and model class Server

    Looks up the server with given uuid and updates them to the given
    Match object.
    """
    ServerIO.update_server(uuid, updated_server)
