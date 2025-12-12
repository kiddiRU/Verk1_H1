"""
Author: Kristjan Hagalin <kristjanhj24@ru.is>
Date: 2025-12-03

Minor change: Andri Már Kristjánsson <andrik25@ru.is>

Logic layer API.
"""

from datetime import date, time
from Models import Club, Match, Player, Team, Tournament
from LogicLayer import PlayerLL, TeamLL, TournamentLL, ClubLL, MatchLL, Validation

team_logic = TeamLL()
match_logic = MatchLL()

club_logic =  ClubLL(match_logic)
player_logic = PlayerLL(team_logic, match_logic)
tournament_logic = TournamentLL(team_logic, match_logic)

team_logic.set_player_logic(player_logic)
team_logic.set_club_logic(club_logic)
team_logic.set_match_logic(match_logic)

# Validation API

def validate(attr: str, value: str, name_type: str):
    """Validates all attributes that need validating.

    :param attribute:
        The type of attribute which needs validating, available options are

        -   name
        -   date_of_birth
        -   home_address
        -   email
        -   phone_number
        -   handle
        -   tournament_date
        -   tournament_time
        -   color
        -   number

    :param value:
        The value that needs validating.

    :param name_type:
        Only used for attribute handle, this determines the type of handle
        want validated, available options are.

        -   PLAYER
        -   TEAM
        -   TOURNAMENT
        -   CLUB

    :returns:
        Returns the same value back if it's valid, otherwise it raises a
        ValidationError. The only exception is when you call with date
        attribute, in that case it will return date object if it's valid.
    """
    return Validation.validate_attr(attr, value, name_type)


# Player API
def create_player(
    name: str,
    date_of_birth: str,
    home_address: str,
    email: str,
    phone_number: str,
    handle: str,
    url: str = ''
) -> Player:
    '''Creates a new Player object, sends it to be stored and returns it.

    :param name:
        The players name.
    :type name: str

    :param date_of_birth:
        The players date of birth.
    :type date_of_birth: str

    :param home_address:
        The players address.
    :type home_address: str

    :param email:
        The players email.
    :type email: str

    :param phone_number:
        The players phone number.
    :type phone_number: str

    :param handle:
        The players unique user handle.
    :type handle: str

    :param url:
        The players personal URL
    :type url: str

    :returns:
        A new Player object.
    :rtype: Player
    '''
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
    name: str,
    date_of_birth: str,
    home_address: str,
    email: str,
    phone_number: str,
    handle: str,
    url: str
) -> Player:
    '''Takes in a Player object and attribute updates. Applies the updates to
    the object, sends it to be stored and returns the updated Player object.

    :param name:
        The players name.
    :type name: str

    :param date_of_birth:
        The players date of birth.
    :type date_of_birth: str

    :param home_address:
        The players address.
    :type home_address: str

    :param email:
        The players email.
    :type email: str

    :param phone_number:
        The players phone number.
    :type phone_number: str

    :param handle:
        The players unique user handle.
    :type handle: str

    :param url:
        The players personal URL
    :type url: str

    :returns:
        An updated Player object.
    :rtype: Player
    '''
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


def promote_captain(current_player: Player, handle_to_promote: str) -> None:
    '''Promotes a teams player to its captain.

    :param current_player:
        The object of the player calling the function.
    :type current_player: Player

    :param handle_to_promote:
        The handle of the player to promote.
    :type handle_to_promote: str
    '''
    player_logic.promote_captain(current_player, handle_to_promote)

# TODO add doc string
def save_player(player_handle: str | None = None) -> str | None:
    """Takes in a player handle and saves them as the current active user.

    :param player_handle:
        The current users unique handle
    :type player_handle: str | None

    :return:
        Returns the unique handle if the method has been called before
        If function has not been called before
        and no handle is put into the method the function will return None
    :rtype: str | None
    """
    return player_logic.save_player(player_handle)

def get_player_team_and_rank(player_handle: str) -> tuple[str, str]:
    '''Gets a players team name and their rank.
    
    :param player_handle:
        The players unique handle.
    :type player_handle: str

    :return:
        Returns a tuple of the players team name and their rank.
    :rtype: tuple[str, str]
    '''
    return player_logic.get_player_team_and_rank(player_handle)

def get_player_wins(player_handle: str) -> str:
    """Gets the player handle

    First gets the players uuid,
    Then loads all matches and if the players uuid is in the
    winning players 3 points are added and for losing players
    1 point is added.
    If a match is not finished the winning and losing players is none
    and that match is skipped
    
    :param player_handle:
        The player handle for finding the player in won matches
    :type player_handle: str

    :return: Returns a string number of the amount of wins in matches
    :rtype: str
    """
    return player_logic.get_player_wins(player_handle)

# "Created" by Sindri Freysson
def get_player_points(player_handle: str) -> str:
    """Gets the player handle

    First gets the players uuid, 
    Then loads all tournaments and gets a list of all matches in
    the tournament with the tournament uuid,
    Finds the last match of the tournament (Finals) and finds the
    winning and losing players of the match, and if the player is in
    winning players he gets 3 points and one points in the losing players
    
    :param player_handle:
        The player handle to find the total points from tournaments
    :type player_handle: str

    :return: Returns a string number of total points from tournaments
    :rtype: str
    """
    return player_logic.get_player_points(player_handle)

def list_all_players() -> list[Player]:
    """When called loads a list of all player objects

    :return:
        Returns a list of player objects
    :rtype: list[Player]
    """
    return player_logic.list_all_players()

def get_player_by_handle(player_handle: str) -> Player | str:
    '''Gets a player object by their handle.
    
    :param player_handle:
        The handle of the player to get.
    :type player_handle: str

    :return:
        Returns a Player object with the given handle, returns an empty string
        if the player isn't found.
    :rtype: Player | str
    '''
    return player_logic.get_player_by_handle(player_handle)

def get_player_by_uuid(player_uuid: str) -> Player | str:
    '''Gets a player object by their UUID.
    
    :param player_uuide:
        The UUID of the player to get.
    :type player_uuid: str

    :return:
        Returns a Player object with the given UUID, returns an empty string
        if the player isn't found.
    :rtype: Player | str
    '''
    return player_logic.get_player_by_uuid(player_uuid)

def player_handle_to_uuid(player_handle: str) -> str:
    '''Converts a players unique handle, to their UUID.
    
    :param player_handle:
        The handle of the player.
    :type player_handle: str

    :return:
        Returns the UUID of the player with the given handle.
    :rtype: str
    '''
    return player_logic.player_handle_to_uuid(player_handle)

def get_players_team_uuid(player_uuid: str) -> str:
    """Gets the player uuid

    First loads all team objects,
    Then finds the team object where the players uuid is
    listed in the teams player list
    
    :param player_uuid:
        The players uuid to find his team uuid
    :type player_uuid: str

    :return: Returns a teams uuid
    :rtype: str
    """
    return player_logic.get_players_team_uuid(player_uuid)

def get_all_players_not_in_team() -> list[Player]:
    """Gets all players that are not apart of any teams
    
    :return: A list of Player objects that are not apart of any teams
    :rtype: list[Player]
    """
    return player_logic.get_all_players_not_in_team()

# Team API

def create_team(
    name: str,
    team_captain: Player,
    club_name: str,
    url: str,
    ascii_art: str
) -> Team:
    '''Creates a new team, sends it to be stored and returns the new Team object.
    
    :param name:
        The name of the team.
    :type name: str

    :param team_captain:
        The object of the player creating the team.
    :type team_captain: Player

    :param club_name:
        The name of teams club.
    :type club_name: str

    :param url:
        The teams URL.
    :type url: str

    :param ascii_art:
        The teams ASCII art.
    :type ascii_art: str

    :return:
        A new Team object.
    :rtype: Team
    '''
    return team_logic.create_team(name, team_captain, club_name, url, ascii_art)

def add_player(player_handle: str, current_player: Player) -> Team | str:
    """Gets the handle of the player to add and
    the player object of the captain

    First checks if the player is already in a team
    Then finds the team of the captain and
    adds the player to the team        
    
    :param player_handle:
        The player handle of the player to add to the team
    :type player_handle: str

    :param current_player:
        current player is the team captain and
        is used to get the uuid of the team
    :type current_player: Player

    :return:
        Returns the team object
    :rtype: Team
    """
    return team_logic.add_player(player_handle, current_player)

def remove_player(player_handle: str, current_player: Player) -> Team:
    """Gets the handle of the player to add and
    the player object of the captain

    Looks through all teams to find the team of the captain
    First checks that the player to remove is not the captain
    Otherwise it removes the player from the team
    if the player is not found and error message will be raised 
    
    :param player_handle:
        the player handle of the player to remove from the team
    :type player_handle: str

    :param current_player
        the player object of the team captain and
        is used to get the uuid of the team
    :type current_player: Player

    :return: Returns the team object
    :rtype: Team
    """
    return team_logic.remove_player(player_handle, current_player)

def get_team_members(team_name: str) -> list[str]:
    """Gets the name of the team

    Looks through all teams to find the correct team object
    and extracts the list of player uuid in the team
    
    :param team_name:
        The team name is used to find the team object
    :type team_name: str

    :return: Returns a list of the team members uuid's
    :rtype: list[str]
    """
    return team_logic.get_team_members(team_name)

def list_all_teams() -> list[Team]:
    """Is called to get a list of all teams
    
    :return: Returns a list of all team objects
    :rtype: list[Team]
    """
    return team_logic.list_all_teams()

def get_team_members_object(team_name: str) -> list[Player]:
    """Gets the team name

    First gets the uuid of the players in the team,
    Then loads all player objects and
    lists all players objects that have the
    uuid of the players in the team
    
    :param team_name:
        The team name of the team to get the player objects
    :type team_name: str

    :return: Returns a list of all player objects in a team
    :rtype: list[Player]
    """
    return team_logic.get_team_members_object(team_name)

def get_team_history(team_name: str) -> list[str]:
    """Gets the team name

    First gets the team uuid, Then loads all Tournaments
    and lists all tournaments that the teams uuid is in
    teams playing 

    :param team_name:
        The team name to find the tournaments they participated in
    :type team_name: str

    :return:
    Returns a list of tournament names that the team has participated in
    :rtype: list[str]
    """
    return team_logic.get_team_history(team_name)

def get_team_wins(team_name: str) -> str:
    """Gets the team name

    First gets the uuid of the team,
    Then Loads all matches and adds one to the count 
    when the winner uuid matches the teams uuid
    
    :param team_name:
        The team name of the team to find the total of won matches
    :type team_name: str

    :return: Returns a string number of the total won matches
    :rtype: str
    """
    return team_logic.get_team_wins(team_name)

def get_team_points(team_name: str) -> str:
    """Gets the team name
    
    First gets the teams uuid,
    Then loads all tournaments and get a list of all matches
    with the tournament uuid,
    Finds the last match of the tournament (Finals) and finds the
    winning and losing team of the match, and if the team is the
    winner they get 3 points and if the loser gets 1 point
    
    :param team_name:
        The team name of the team to find the total points from tournaments
    :type team_name: str

    :return: Returns a string number of total points from tournaments
    :rtype: str
    """
    return team_logic.get_team_points(team_name)

def get_team_club(team_name: str) -> str:
    """Gets the team name

    First loads all clubs, and gets a list of all team names in the club
    and if the team name is in the list it is their club
    
    :param team_name:
        The team name to get the club name from
    :type team_name: str
    
    :return: Returns the name of the club that the team is in
    :rtype: str
    """
    return team_logic.get_team_club(team_name)

def get_team_by_name(team_name: str) -> Team:
    '''Gets a Team object by its name.
    
    :param team_name:
        The name of the team to fetch.
    :type team_name: str

    :return:
        The object of the team with the given name.
    :rtype: Team
    '''
    return team_logic.get_team_by_name(team_name)

def get_team_by_uuid(team_uuid: str) -> Team:
    '''Gets a Team object by its UUID.
    
    :param team_uuid:
        The UUID of the team to fetch.
    :type team_uuid: str

    :return:
        The object of the team with the given UUID.
    :rtype: Team
    '''
    return team_logic.get_team_by_uuid(team_uuid)

def team_name_to_uuid(team_name: str) -> str:
    '''Converts a teams name, to their UUID.
    
    :param team_name:
        The name of the team.
    :type team_name: str

    :return:
        Returns the UUID of the team with the given name.
    :rtype: str
    '''
    return team_logic.team_name_to_uuid(team_name)

# Tournament API

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
    '''Creates a new Tournament object and sends it to be stored.
    
    :param name:
        The tournaments name.
    :type name: str

    :param start_date:
        The tournaments starting date.
    :type start_date: date

    :param end_date:
        The tournaments ending date.
    :type end_date: date

    :param time_frame_start:
        The start of the tournaments time frame.
    :type time_frame_start: time

    :param time_frame_end:
        The end of the tournaments time frame.
    :type time_frame_end: time

    :param venue:
        The tournaments venue.
    :type venue: str

    :param email:
        The tournaments contact email.
    :type email: str

    :param phone_number:
        The tournaments contact phone number.
    :type phone_number: str

    :param amount_of_servers:
        The tournaments amount of servers.
    :type amount_of_servers: int
    '''
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

def add_team(tournament_name: str, team_name: str) -> None:
    '''Adds a team to the list of teams playing in a tournament.
    
    :param tournament_name:
        The name of the tournament.
    :type tournament_name: str

    :param team_name:
        The name of the team to add.
    :type team_name: str
    '''
    tournament_logic.add_team(tournament_name, team_name)

def remove_team(tournament_name: str, team_name: str) -> None:
    '''Removes a team from the list of teams playing in a tournament.
    
    :param tournament_name:
        The name of the tournament.
    :type tournament_name: str

    :param team_name:
        The name of the team to remove.
    :type team_name: str
    '''
    tournament_logic.remove_team(tournament_name, team_name)

def list_tournaments() -> list[Tournament]:
    '''Gets a list of all stored tournaments.
    
    :return:
        A list of all Tournament objects.
    :rtype: list[Tournament]
    '''
    return tournament_logic.list_tournaments()

def publish(tournament_name: str) -> None:
    """Publish an inactive tournament.

    Call to publish an inactive tournament, this will...
    
    -   Create a match schedule according to tournament time and date.
    -   Assign teams to the first round of matches.
    -   Create servers to host the matches.
    -   Assign the first matches to servers.

    :param tournament_name:
        Publishes the tournament with the given name.
    :type tournament_name: str
    """
    tournament_logic.publish(tournament_name)

def get_next_matches(tournament_uuid: str) -> list[Match]:
    """Gets the matches next on the schedule in a certain tournament.

    Gets a list of matches which are next on the schedule in a certain
    tournament, a match is next on the schedule if it needs a winner and
    no other match which needs a winner is before it on the schedule.

    :param tournament_uuid:
        The tournament to get the matches will have the same uuid as
        tournament_uuid
    :type tournament_uuid: str

    :returns:
        The list of matches next on the schedule.
    :rtype: list[Match]
    """
    return tournament_logic.next_games(tournament_uuid)

def change_match_winner(
        tournament_uuid: str,
        match_uuid: str,
        team_uuid: str
    ) -> None:
    """Updates match winner of a specific match in a specific tournament.

    Given the uuid of a specific tournament and the uuid of a specific match,
    will update the winner of this match, will set a new match into the server
    used if needed, will move onto next round of tournament if needed and will
    archive tournament if needed.

    :param tournament_uuid:
        The uuid of the tournament which the match belongs to.

    :param match_uuid:
        The uuid of the match you want to update.

    :param team_uuid:
        The uuid of the winner.
    """
    tournament_logic.change_match_winner(
            tournament_uuid,
            match_uuid,
            team_uuid
        )

# TODO docstring
def get_teams_from_tournament_name(tournament_name: str) -> list[Team]:
    return tournament_logic.get_teams_from_tournament_name(tournament_name)

# TO help create a Tournament
def to_time(value: str) -> time:
    return tournament_logic.to_time(value)

def to_date(value: str) -> date:
    return tournament_logic.to_date(value)

def get_tournament_by_name(tournament_name: str) -> Tournament:
    '''Gets a Tournament object by its name.
    
    :param tournament_name:
        The name of the tournament to fetch.
    :type tournament_name: str

    :return:
        The object of the tournament with the given name.
    :rtype: Tournament
    '''
    return tournament_logic.get_tournament_by_name(tournament_name)

def get_tournament_by_uuid(tournament_uuid: str) -> Tournament:
    '''Gets a Tournament object by its UUID.
    
    :param tournament_uuid:
        The UUID of the tournament to fetch.
    :type tournament_uuid: str

    :return:
        The object of the tournament with the given UUID.
    :rtype: Tournament
    '''
    return tournament_logic.get_tournament_by_uuid(tournament_uuid)

def tournament_name_to_uuid(tournament_name: str) -> str:
    '''Converts a tournaments name, to its UUID.
    
    :param tournament_name:
        The name of the tournament.
    :type tournament_name: str

    :return:
        Returns the UUID of the tournament with the given name.
    :rtype: str
    '''
    return tournament_logic.tournament_name_to_uuid(tournament_name)

# Club API

def create_club(name: str, club_color: str, country: str, home_town: str) -> Club:
    """First takes in the info that has already been validated
    and creates a uuid for the club,
    Then creates the object using the uuid and info and
    points the object to Data Layer API to be stored as a club        

    :param name:
        The name of the club
    :type name: str

    :param club_color:
        The color of the club
    :type club_color: str

    :param country:
        The country of the club
    :type country: str

    :param home_town:
        The home town of the club
    :type home_town: str

    :return: Returns the newly created club object
    :rtype: Club
    """
    return club_logic.create_club(name,club_color, country, home_town)

def list_all_clubs() -> list[Club]:
    """Loads a list of all club objects from the Data Layer API

    :return: Returns a list of all club objects
    :rtype: list[Club]
    """
    return club_logic.list_all_clubs()

def get_teams_in_club(club_name: str) -> list[Team]:
    """Gets club name

    First gets the clubs uuid,
    Then loads all team objects and
    lists all team objects that have the club uuid of the wanted club
    
    :param club_name:
        club name to find all teams that are in the club
    :type club_name: str

    :return: Returns a list of team objects that are in the club
    :rtype: list[Team]
    """
    return club_logic.get_teams_in_club(club_name)

# Created by Sindri
def get_club_wins(club_name: str) -> str:
    """Gets club name
    
    First gets the uuid of the club
    Then Loads all teams and finds all the teams in the club
    and lists their team uuid's

    Then Loads all matches and if the match winner
    is in the list of teams in the club one is added to the count
    
    :param club_name:
        The clubs name to find the total won matches
    :type club_name: str

    :return: 
    Returns a string number of the total won matches
    of the teams in the club
    :rtype: str
    """
    return club_logic.get_club_wins(club_name)

# Created by Sindri
def get_club_points(club_name: str) -> str:
    """Gets the club name

    First gets the uuid of the club,
    Then Loads all teams and finds all the teams in the club
    and lists their team uuid's

    Then loads all tournaments and gets a list of all matches in a
    the tournament with the tournament uuid,
    Finds the last match of the tournament (Finals) and finds the
    winning and losing teams of the match, and if the winner is in
    the list of teams of the club 3 points are added
    and 1 point for the loser

    :param club_name:
        The name of the club to find the total points from tournaments
    :type club_name: str

    :return: Returns a string number of the total points from tournaments
    :rtype: str
    """
    return club_logic.get_club_points(club_name)

# TODO fix docstring
def get_club_by_name(club_name: str) -> Club:
    """Takes in club name
    looks through all clubs until it finds the right club name
    and returns the teams uuid
    if no team is found an error is raised
    """
    return club_logic.get_club_by_name(club_name)

# Match API

def get_all_matches(tournament_uuid: str) -> list[Match]:
    """
    Parameters: uuid of tournaemnt

    Returns a list of all matches in the tournament
    tied to the uuid given.
    """
    return match_logic.get_matches(tournament_uuid)


# TODO docstring?
def get_match(tournament_id: str, match_team1: str, match_team2: str) -> Match | str:
    return match_logic.get_match(tournament_id, match_team1, match_team2)


