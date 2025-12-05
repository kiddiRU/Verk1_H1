"""
Author: Kristinn Hrafn <kristinnd25@ru.is>
Date: 2025-12-03

Data layer API
"""

from Models import Club, Match, Player, Server, Team, Tournament
from DataLayer import PlayerIO, TeamIO, TournamentIO, ClubIO, MatchIO

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
Takes in uuid and update team model object.

uuid has to exist in the json file.

Will attempt to find player with given uuid and update that
player with the new updated player object.

Have to call withing try except.
"""
def update_player(uuid: str, updated_player: Player) -> None:
    PlayerIO.update_player(uuid, updated_player)

""" Team API """

"""
No parameters

Reads json file containing teams and creates a list of
Team model objects of each entry in the json file.

Returns the created team list.

Have to call within try except.
"""
def load_teams() -> list[Team]:
    return TeamIO.load_teams()

"""
Takes in uuid, key and value as parameters.

uuid and key have to exist in the json file.

Will attempt to find team with given uuid and update that
team with the new updated team object.

Have to call within try except.
"""
def update_team(uuid: str, updated_team: Team) -> None:
    TeamIO.update_team(uuid, updated_team)

"""
Takes in model class Team

Inserts information about the Team class into a json file
for storage.
"""
def store_team(team: Team) -> None:
    TeamIO.store_team(team)

""" Club API """

"""
Takes in model class Club

Inserts information about the Club class into a json file
for storage

Have to call withing try except
"""
def store_club(club: Club) -> None:
    ClubIO.store_club(club)

"""
No parameters

Reads json file containing clubs and creates a list of
Club model objects of each entry in the json file.

Returns the created list.
"""
def update_club(uuid: str, updated_club: Club) -> None:
    ClubIO.update_club(uuid, updated_club)

"""
Takes in uuid and the updated Club model object.

uuid has to exist in the json file.

Will attempt to find a blub with given uuid and update that
club with the new updated club object.
"""
def load_clubs() -> list[Club]:
    return ClubIO.load_club()

""" Tournament API """

"""
Takes in model class Tournament.

Inserts information about the class into a json file for.

Have to call within try except.
"""
def store_tournament(tournament: Tournament) -> None:
    TournamentIO.store_tournament(tournament)

"""
No parameters

Reads the json file containing tournaments and creates a list of
Tournament model objects of each entry in the json file.

Returns the created list.

Have to call within try except.
"""
def update_tournament(uuid: str, updated_tournament: Tournament) -> None:
    TournamentIO.update_tournament(uuid, updated_tournament)

"""
Takes in uuid and the updated Tournament model object.

uuid has to exist in the json file.

Will attempt to find tournament with given uuid and update
that team with the new updated tournament object.

Have to call within try except.
"""
def load_tournaments() -> list[Tournament]:
    return TournamentIO.load_tournaments()

""" Match API """

"""
Takes in model class match

Inserts information about the Match class into a json file
for storage.
"""
def store_match(match: Match) -> None:
    MatchIO.store_match(match)

"""
Takes in uuid and the updated Match model object.

uuid has to exist in the json file.

Will attempt to find a match with given uuid and update that
match with the new updated match object.
"""
def update_match(uuid: str, updated_match: Match) -> None:
    MatchIO.update_match(uuid, updated_match)

"""
No parameters

Reads json file containing matches and creates a list of
Match model objects of each entry in the json file.

Returns the created match list.
"""
def load_matches() -> list[Match]:
    return MatchIO.load_match()
