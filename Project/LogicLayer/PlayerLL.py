"""
Authors: Elmar Sigmarsson <elmars25@ru.is>
Date: 2025-12-03

Co: Kristjan Hagalin <kristjanhj24@ru.is>
Minor changes: Andri Már Kristjánsson <andrik25@ru.is>

Functions for player logic.
"""

from uuid import uuid4
from DataLayer import DataLayerAPI
from Models import Player, Team, Match, Tournament
from LogicLayer import MatchLL, TeamLL


class PlayerLL:
    ''' Player logic. '''

    def __init__(self, team_logic: TeamLL, match_logic: MatchLL) -> None:
        '''Initialize the PlayerLL instance.

        :param team_logic:
            The logic layer responsible for team operations and validations.
        :type team_logic: TeamLL

        :param match_logic:
            The logic layer responsible for match operations and validations.
        :type match_logic: MatchLL
        '''
        self._team_logic = team_logic
        self._match_logic = match_logic
        self.player: str | None = None

    def create_player(
        self,
        name: str,
        date_of_birth: str,
        home_address: str,
        email: str,
        phone_number: str,
        handle: str,
        url: str
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
        # Create a unique UUID and a new Player object.
        uuid = str(uuid4())
        new_player = Player(
            uuid,
            name,
            date_of_birth,
            home_address,
            email,
            phone_number,
            handle,
            url
        )

        # Store and return the new player.
        DataLayerAPI.store_player(new_player)
        return new_player

    def update_player_info(
        self,
        player: Player,
        name: str,
        date_of_birth: str,
        home_address: str,
        email: str,
        phone_number: str,
        handle: str,
        url: str
    ) -> Player:
        '''Takes in a Player object and attribute updates. Applies the
        updates to the object, sends it to be stored and returns the
        updated Player object.

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

        # Set the attributes of the Player object received.
        player.name = name
        player.date_of_birth = date_of_birth
        player.home_address = home_address
        player.email = email
        player.phone_number = phone_number
        player.handle = handle
        player.url = url

        # Store and return the updated player.
        DataLayerAPI.update_player(player.uuid, player)
        return player

    def promote_captain(
        self,
        current_player: Player,
        handle_to_promote: str
    ) -> None:
        '''Promotes a teams player to its captain.

        :param current_player:
            The object of the player calling the function.
        :type current_player: Player

        :param handle_to_promote:
            The handle of the player to promote.
        :type handle_to_promote: str
        '''
        # Get the captains team.
        teams: list[Team] = DataLayerAPI.load_teams()
        team_to_edit = next(
            (t for t in teams if current_player.uuid == t.team_captain_uuid),
            None
        )

        # If no team is found, raise an error.
        if team_to_edit is None:
            raise KeyError('You are not a captain!')

        # Get an object of the player with the given handle.
        players: list[Player] = DataLayerAPI.load_players()
        player_to_promote: Player | None = next(
            (p for p in players if p.handle == handle_to_promote),
            None
        )

        # If no player is found, raise an error.
        if player_to_promote is None:
            raise KeyError(
                f'No player found with the handle: {handle_to_promote}'
            )

        # If the player to promote is not in the captains team, raise an error.
        if player_to_promote.uuid not in team_to_edit.list_player_uuid:
            raise KeyError(
                f'''The player \'{handle_to_promote}\'exists, but is
                not in your team!'''
            )

        # Set the player with the given handle as the
        # captain of the team, and store the update.
        team_to_edit.team_captain_uuid = player_to_promote.uuid
        DataLayerAPI.update_team(team_to_edit.uuid, team_to_edit)

    def save_player(self, player_handle: str | None = None):
        """ Takes in a player handle and saves them as the current active user.

        :param player_handle:
            The handle of the current player.
        :type player_handle: str
        """
        if player_handle is not None:
            self.player = player_handle

        return self.player

    def get_player_team_and_rank(self, player_handle: str) -> tuple[str, str]:
        '''Gets a players team and rank.

        :param player_handle:
            The players unique handle.
        :type player_handle: str

        :return:
            Returns a tuple of the players team name and their rank.
        :rtype: tuple[str, str]
        '''
        # Get a list of all teams, and the players UUID.
        teams: list[Team] = self._team_logic.list_all_teams()
        player_uuid: Player | str = self.player_handle_to_uuid(player_handle)

        # Get the players team.
        players_team: Team | None = next(
            (t for t in teams if player_uuid in t.list_player_uuid),
            None
        )

        # If the player is in no team, return an empty tuple.
        if players_team is None:
            return ('', '')

        # Return a tuple of the players team and rank.
        return (
            players_team.name, 'Captain'
        ) if players_team.team_captain_uuid == player_uuid else (
            players_team.name, 'Player'
        )

    def get_player_wins(self, player_handle: str) -> str:
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
        model_matches: list[Match] = DataLayerAPI.load_matches()
        player_uuid: str = self.player_handle_to_uuid(player_handle)
        win_count: int = 0

        # Loops all matches
        for match in model_matches:
            if match.winning_players is None:
                pass

            # If player is a winner in a match adds 1
            elif player_uuid in match.winning_players:
                win_count += 1

        return str(win_count)

    def get_player_points(self, player_handle: str) -> str:
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

        model_tournaments: list[Tournament] = DataLayerAPI.load_tournaments()
        player_uuid: str = self.player_handle_to_uuid(player_handle)
        points: int = 0

        # Loops through all tournaments
        for tournament in model_tournaments:
            matches_list: list[Match] = self._match_logic.get_matches(
                tournament.uuid
            )

            # if matches is empty skips tournaments
            if not matches_list:
                continue

            # gets the final match of the tournament (Finals)
            tour_final_match: Match = matches_list[-1]

            # gets the winning and losing players
            winning_players = tour_final_match.winning_players
            losing_players = tour_final_match.losing_players

            # If match is not finished winning players will be None
            if winning_players is None or losing_players is None:
                pass

            # If the player is the winner +3 points
            elif player_uuid in winning_players:
                points += 3

            # if the player is the loser +1 point
            elif player_uuid in losing_players:
                points += 1

        return str(points)

    def list_all_players(self) -> list[Player]:
        """When called loads a list of all player objects

        :return: Returns a list of player objects
        :rtype: list[Player]
        """
        # Get a list of all stored players as objects, and return them.
        players: list[Player] = DataLayerAPI.load_players()
        return players

    def get_player_by_handle(self, player_handle: str) -> Player | str:
        '''Gets a player object by their handle.

        :param player_handle:
            The handle of the player to get.
        :type player_handle: str
        :return:
            Returns a Player object with the given handle, returns an
            empty string if the player isn't found.
        :rtype: Player | str
        '''
        # Get list of all stored players, and find the player with
        # the given handle.
        players: list[Player] = self.list_all_players()
        player = next((p for p in players if p.handle == player_handle), None)

        # If the no player exists with thegivenhandle, return an empty string.
        if player is None:
            return ""

        return player

    def get_player_by_uuid(self, player_uuid: str) -> Player | str:
        '''Gets a player object by their UUID.

        :param player_uuide:
            The UUID of the player to get.
        :type player_uuid: str

        :return:
            Returns a Player object with the given UUID, returns an empty
            string if the player isn't found.
        :rtype: Player | str
        '''
        # Get list of all stored players, and find the player with
        # the given UUID.
        players: list[Player] = self.list_all_players()
        player: Player | None = next(
            (p for p in players if p.uuid == player_uuid),
            None
        )

        # If the no player exists with the given UUID, return an empty string.
        if player is None:
            return ""

        return player

    def player_handle_to_uuid(self, player_handle: str) -> str:
        '''Converts a players unique handle, to their UUID.

        :param player_handle:
            The handle of the player.
        :type player_handle: str

        :return:
            Returns the UUID of the player with the given handle.
        :rtype: str
        '''
        # Get the Player object with the given handle. Return its UUID
        # if it exists, else an empty string.
        player: Player | str = self.get_player_by_handle(player_handle)
        return player.uuid if isinstance(player, Player) else ''

    def get_players_team_uuid(self, player_uuid: str) -> str:
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
        # Get all teams
        teams: list[Team] = DataLayerAPI.load_teams()

        # If the given players UUID is found
        # in the team, return the teams UUID.
        for team in teams:
            if player_uuid in team.list_player_uuid:
                return team.uuid

        return ""

    # Created By Ísak
    def get_all_players_not_in_team(self) -> list[Player]:
        """Gets all players that are not apart of any teams

        :return: A list of Player objects that are not apart of any teams
        :rtype: list[Player]
        """

        # Gets all players and gets all teams
        all_players: list[Player] = DataLayerAPI.load_players()
        model_teams: list[Team] = DataLayerAPI.load_teams()

        # Setup set and list to add to when filtering
        no_team: list[Player] = []
        players_in_teams: set[str] = set()

        # Loops through all teams and adds all players to a set
        for team in model_teams:
            for player in team.list_player_uuid:
                players_in_teams.add(player)

        # Loops through all player uuid's and if not in any team then
        # add to list
        for player in all_players:
            if player.uuid not in players_in_teams:
                no_team.append(player)

        return no_team
