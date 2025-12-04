"""
Author: Kristinn Hrafn <kristinnd25@ru.is>
Date: 2025-12-03

Data layer API
"""

from Models import Club, Match, Player, Server, Team, Tournament
from DataLayer import PlayerIO, TeamIO

""" Player API """

"""
Takes in model class Player.

Inserts information about the Player class into a json file
for storage.

Have to call it within try except.
"""
def store_player(player: Player) -> None:
    PlayerIO.store_player(player)

"""
No parameters

Reads json file containing players and creates a list of
Player model objects of each entry in the json file.

Returns the created player list.

Have to call it within try except.
"""
def load_players() -> list[Player]:
    return PlayerIO.load_players()

"""
Takes in uuid, key and value as parameters.

uuid and key have to exist in the json file.

Will attempt to find player with given uuid and update the
value tied to given key of that player.

Have to call withing try except.
"""
def update_player(uuid: str, key: str, value: str) -> None:
    PlayerIO.update_player(uuid, key, value)

""" Team API """

# TODO implement load_teams and call it
def load_teams() -> list[Team]:
    return TeamIO.load_teams()

# TODO implement update_team and call it
def update_team(uuid: str, key: str, value:str) -> None:
    TeamIO.update_team(uuid, key, value)

# TODO implement store_team and call it
def store_team(team: Team) -> None:
    TeamIO.store_team(team)

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
