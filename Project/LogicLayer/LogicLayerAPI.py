"""
Author: Kristjan Hagalin <kristjanhj24@ru.is>
Date: 2025-12-03

Minor change: Andri Már Kristjánsson <andrik25@ru.is>

Logic layer API.
"""

from Models import Club, Match, Player, Team, Tournament
from LogicLayer import PlayerLL, TeamLL, TournamentLL, ClubLL, MatchLL, Validation
from datetime import date, time

team_logic = TeamLL()
match_logic = MatchLL()
club_logic =  ClubLL()

player_logic = PlayerLL(team_logic, match_logic)
tournament_logic = TournamentLL(team_logic, match_logic)

team_logic.set_player_logic(player_logic)
team_logic.set_club_logic(club_logic)
team_logic.set_match_logic(match_logic)

''' Validation API '''
def validate(attr: str, value: str, name_type: str):
    return Validation.validate_attr(attr, value, name_type)

''' Player API '''

def create_player(
    name: str,
    date_of_birth: str,
    home_address: str,
    email: str,
    phone_number: str,
    handle: str,
    url: str = ''
) -> Player:
    '''
    Creates a new Player object, sends it to be stored and
    returns it.

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
    '''
    Takes in a Player object and attribute updates. Applies the updates to
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

# Isn't used, remove?
# def leave_team(team_name: str, player: Player) -> None:
#     return player_logic.leave_team(team_name, player)

def promote_captain(current_player: Player, handle_to_promote: str) -> None:
    '''
    Promotes a teams player to its captain.
    
    :param current_player:
        The object of the player calling the function.
    :type current_player: Player

    :param handle_to_promote:
        The handle of the player to promote.
    :type handle_to_promote: str
    '''
    player_logic.promote_captain(current_player, handle_to_promote)

def save_player(player_handle: str | None = None) -> str | None:
    return player_logic.save_player(player_handle)

def get_player_team_and_rank(player_handle: str) -> tuple[str, str]:
    return player_logic.get_player_team_and_rank(player_handle)

def get_player_wins(player_handle: str) -> str:
    return player_logic.get_player_wins(player_handle)

# "Created" by Sindri Freysson
def get_player_points(player_handle: str) -> str:
    return player_logic.get_player_points(player_handle)

def list_all_players() -> list[Player]:
    return player_logic.list_all_players()

def get_player_by_handle(player_handle: str) -> Player | str:
    return player_logic.get_player_by_handle(player_handle)

def get_player_by_uuid(player_uuid: str) -> Player | str:
    return player_logic.get_player_by_uuid(player_uuid)

def player_handle_to_uuid(player_handle: str) -> str:
    return player_logic.player_handle_to_uuid(player_handle)

def get_players_team_uuid(player_uuid: str) -> str:
    return player_logic.get_players_team_uuid(player_uuid)

def get_all_players_not_in_team() -> list[Player]:
    """
    Gets all players that are not apart of any teams
    
    :return: A list of Player objects that are not apart of any teams
    :rtype: list[Player]
    """
    return player_logic.get_all_players_not_in_team()

''' Team API '''

def create_team(name: str, team_captain: Player, club_name: str, url: str, ascii_art: str) -> Team:
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
    return team_logic.get_team_by_name(team_name)

def get_team_by_uuid(team_uuid: str) -> Team:
    return team_logic.get_team_by_uuid(team_uuid)

def team_name_to_uuid(team_name: str) -> str:
    return team_logic.team_name_to_uuid(team_name)

''' Tournament API '''

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

def add_team(tournament_name: str, team_name: str) -> None:
    tournament_logic.add_team(tournament_name, team_name)

def remove_team(tournament_name: str, team_name: str) -> None:
    tournament_logic.remove_team(tournament_name, team_name)

def update_tournament_info(
    tournament_name: str,
    venue: str,
    email: str,
    phone_number: str
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

def publish(tournament_name: str) -> None:
    """Publish an inactive tournament.

    Call to publish an inactive tournament, this will...
    
    -   Create a match schedule according to tournament time and date.
    -   Assign teams to the first round of matches.
    -   Create servers to host the matches.
    -   Assign the first matches to servers.

    :param tournament_name:
        Publishes the tournament with the given name.
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

    :returns:
        The list of matches next on the schedule.
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

def get_teams_from_tournament_name(tournament_name: str) -> list[Team]:
    return tournament_logic.get_teams_from_tournament_name(tournament_name)

# TO help create a Tournament
def to_time(value: str) -> time:
    return tournament_logic.to_time(value)

def to_date(value: str) -> date:
    return tournament_logic.to_date(value)

def get_tournament_by_name(tournament_name: str) -> Tournament:
    return tournament_logic.get_tournament_by_name(tournament_name)

def tournament_name_to_uuid(tournament_name: str) -> str:
    return tournament_logic.tournament_name_to_uuid(tournament_name)

''' Club API '''

def create_club(name: str, club_color: str, country: str, home_town: str) -> Club:
    return club_logic.create_club(name,club_color, country, home_town)

def list_all_clubs() -> list[Club]:
    return club_logic.list_all_clubs()

def get_teams_in_club(club_name: str) -> list[Team]:
    return club_logic.get_teams_in_club(club_name)

# Created by Sindri
def get_club_wins(club_name: str) -> str:
    return club_logic.get_club_wins(club_name)

# Created by Sindri
def get_club_points(club_name: str) -> str:
    return club_logic.get_club_points(club_name)

def get_club_by_name(club_name: str) -> Club:
    return club_logic.get_club_by_name(club_name)

''' Match API '''

def get_all_matches(tournament_uuid: str) -> list[Match]:
    """
    Parameters: uuid of tournaemnt

    Returns a list of all matches in the tournament
    tied to the uuid given.
    """
    return match_logic.get_matches(tournament_uuid)


# TODO implement input_match_results and call it
def input_match_results(match: Match) -> None:
    pass

def get_match(tournament_id: str, match_team1: str, match_team2: str) -> Match | str:
    return match_logic.get_match(tournament_id, match_team1, match_team2)


