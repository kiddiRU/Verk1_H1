"""
Author: Kristinn Hrafn <kristinnd25@ru.is>
Date: 2025-12-03

Data layer API
"""

from Models import Club, Match, Player, Server, Team, Tournament
from DataLayer import PlayerIO, TeamIO, TournamentIO, ClubIO, MatchIO, ServerIO

""" Player API """

def store_player(player: Player) -> None:
    """Stores new players in a json file to be fetched later.

    :param player:
        The player object to store.
    """
    PlayerIO.store_player(player)

def load_players() -> list[Player]:
    """Gets a list of all players stored with the store_player function.

    :returns:
        The list of players.
    """
    return PlayerIO.load_players()

def update_player(uuid: str, updated_player: Player) -> None:
    """Updates a player stored with the store_player function.

    Looks for a player stored with the store_player function which
    has the same uuid as the given uuid, then updates that player.

    :param uuid:
        uuid to look up player to update.

    :param updated_player:
        The player object to update the player to.
    """
    PlayerIO.update_player(uuid, updated_player)

""" Team API """

def store_team(team: Team) -> None:
    """Stores new teams in a json file to be fetched later.

    :param team:
        The team object to store.
    """
    TeamIO.store_team(team)

def load_teams() -> list[Team]:
    """Gets a list of all teams stored with the store_team function.

    :returns:
        The list of teams.
    """
    return TeamIO.load_teams()

def update_team(uuid: str, updated_team: Team) -> None:
    """Updates a team stored with the store_team function.

    Looks for a team stored with the store_team function which
    has the same uuid as the given uuid, then updates that team.

    :param uuid:
        uuid to look up the team to update.

    :param updated_team:
        The team object to update the team to.
    """
    TeamIO.update_team(uuid, updated_team)

""" Club API """

def store_club(club: Club) -> None:
    """Stores new clubs in a json file to be fetched later.

    :param club:
        The club object to store.
    """
    ClubIO.store_club(club)

def load_clubs() -> list[Club]:
    """Gets a list of all clubs stored with the store_club function.

    :returns:
        The list of clubs.
    """
    return ClubIO.load_club()

def update_club(uuid: str, updated_club: Club) -> None:
    """Updates a club stored with the store_club function.

    Looks for a club stored with the store_club function which
    has the same uuid as the given uuid, then updates that tournament.

    :param uuid:
        uuid to look up the club to update.

    :param updated_club:
        The club object to update the team to.
    """
    ClubIO.update_club(uuid, updated_club)

""" Tournament API """

def store_tournament(tournament: Tournament) -> None:
    """Stores new tournaments in a json file to be fetched later.

    :param tournament:
        The tournament object to store.
    """
    TournamentIO.store_tournament(tournament)

def load_tournaments() -> list[Tournament]:
    """Gets a list of all tournaments stored with the store_tournament
    function.

    :returns:
        The list of tournaments.
    """
    return TournamentIO.load_tournaments()

def update_tournament(uuid: str, updated_tournament: Tournament) -> None:
    """Updates a tournament stored with the store_tournament function.

    Looks for a tournament stored with the store_tournament function which
    has the same uuid as the given uuid, then updates that tournament.

    :param uuid:
        uuid to look up the tournament to update.

    :param updated_tournament:
        The tournament object to update the tournament to.
    """
    TournamentIO.update_tournament(uuid, updated_tournament)

""" Match API """

def store_match(match: Match) -> None:
    """Stores new matches in a json file to be fetched later.

    :param match:
        The match object to store.
    """
    MatchIO.store_match(match)

def load_matches() -> list[Match]:
    """Gets a list of all matches stored with the store_match function.

    :returns:
        The list of matches.
    """
    return MatchIO.load_match()

def update_match(uuid: str, updated_match: Match) -> None:
    """Updates a match stored with the store_match function.

    Looks for a match stored with the store_match function which
    has the same uuid as the given uuid, then updates that match.

    :param uuid:
        uuid to look up the match to update.

    :param updated_match:
        The match object to update the match to.
    """
    MatchIO.update_match(uuid, updated_match)

""" Server API """

def store_server(server: Server) -> None:
    """Stores new servers in a json file to be fetched later.

    :param server:
        The server object to store.
    """
    ServerIO.store_server(server)

def load_servers() -> list[Server]:
    """Gets a list of all servers stored with the store_server function.
    
    :returns:
        The list of servers.
    """
    return ServerIO.load_server()

def update_server(uuid: str, updated_server: Server) -> None:
    """Updates the server stored with the store_server function.

    Looks for a servers stored with the store_server function which
    has the same uuid as the given uuid, then updates that server.

    :param uuid:
        uuid to look up the server to update.

    :param updated_server:
        The server object to update the server to.
    """
    ServerIO.update_server(uuid, updated_server)
