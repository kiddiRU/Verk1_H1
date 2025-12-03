""" Data layer API """
from Models.Club import Club
from Models.Match import Match
from Models.Player import Player
from Models.Server import Server
from Models.Team import Team
from Models.Tournament import Tournament
import DataLayer.PlayerIO


""" Player API """

def load_players() -> list[Player]:
    return PlayerIO.load_players()

def store_player(player: Player) -> None:
    PlayerIO.store_player(player)

def update_player(uuid: str, key: str, value: str) -> None:
    PlayerIO.update_player(uuid, key, value)

""" Team API """

# TODO implement load_teams and call it
def load_teams() -> list[Teams]:
    pass

# TODO implement update_team and call it
def update_team(uuid: str, key: str, value:str) -> None:
    pass

# TODO implement store_team and call it
def store_team(team: Team) -> None:
    pass

""" Club API """

# TODO implement store_club and call it
def store_club(club: Club) -> None:
    pass

# def update_club(uuid: str, key: str, value: str) -> None:

# TODO implement load_clubs and call it
def load_clubs() -> list[Club]:
    pass

""" Tournament API """

# TODO implement store_tournament and call it
def store_tournament(tournament: Tournament) -> None:
    pass

# TODO implement update_tournament and call it
def update_tournament(uuid: str, key: str, value: str) -> None:
    pass

# TODO implement load_tournaments and call it
def load_tournaments() -> list[Tournament]:
    pass

""" Match API """

# TODO implement store_match and call it
def store_match(match: Match) -> None:
    pass

# TODO implement update_match and call it
def update_match(uuid: str, key: str, value: str) -> None:
    pass

# TODO implement load_matches and call it
def load_matches() -> list[Match]:
    pass
