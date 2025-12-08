"""
Authors: Elmar Sigmarsson <elmars25@ru.is>
Date: 2025-12-03

Co: Kristjan Hagalin <kristjanhj24@ru.is>

Functions for player logic.
"""

# TODO add nessecery imports
from uuid import uuid4
from DataLayer import DataLayerAPI
from Models import Player, Team, Club, ValidationError
from LogicLayer.Validation import validate_attr

class PlayerLL():
    def __init__(self) -> None:
        self._data_api = DataLayerAPI

    # TODO Alter validation functionality?
    def create_player(self,
        name: str,
        date_of_birth: str,
        home_address: str,
        email: str,
        phone_number: str,
        handle: str,
        url: str
    ) -> Player:

        """
        Takes in player info.

        Validates the given info and creates a player object. Sends the
        object to the data layer to be stored and returns the new player.
        """

        uuid = str(uuid4())

        params: dict[str, str] = {k: v for k, v in locals().copy().items() if not k == 'self'}
        for attr, value in params.items():
            validate_attr(attr, value.strip(), name_type = 'PLAYER')

        new_player = Player(
            uuid,
            params["name"],
            params["date_of_birth"],
            params["home_address"],
            params["email"],
            params["phone_number"],
            params["handle"],
            params["url"],
        )

        DataLayerAPI.store_player(new_player)
        return new_player

    # TODO Remove Player objec, alter validation functionality?
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

        '''
        Takes in a Player object and potential attribute updates.

        Sends updated values to the data layer, and returns and updated Player object.
        '''

        params: dict[str, str] = {k: v for k, v in locals().items() if k not in ('self', 'player')}
        for attr, value in params.items():
            if value == '':
                continue

            validate_attr(attr, value, name_type='PLAYER')
            setattr(player, attr, value)

        self._data_api.update_player(player.uuid, player)
        return player

    # TODO Remove Player object, check if player is in team
    def create_team(self, name: str, team_captain: Player, club_name: str, url: str, ascii_art: str) -> Team:
        '''
        Takes in the teams name, its captain, club, url and ascii art.

        Creates a new Team object, sends it the data layer to be stored and returns it.
        '''
        teams: list[Team] = self._data_api.load_teams()
        players_in_teams: list[str] = [uuid for t in teams for uuid in t.list_player_uuid]

        if team_captain.uuid in players_in_teams:
            raise Exception('You can\'t create a team when you\'re already in one!')

        validate_attr('handle', name, 'TEAM')
        uuid = str(uuid4())

        clubs: list[Club] = self._data_api.load_clubs()
        club_uuid = next((c.uuid for c in clubs if c.name == club_name), 'NO_CLUB_UUID') # UUID for no club is ..?
        
        new_team = Team(uuid, name, [team_captain.uuid], team_captain.uuid, club_uuid, None, url, ascii_art)

        self._data_api.store_team(new_team)
        return new_team

    # TODO Remove Player objec
    def leave_team(self, team_uuid: str, player: Player) -> None:
        '''
        Takes in a teams UUID and a Player object.

        Removes the player from the team, raises an exception if the player
        is the captain of said team.
        '''

        teams: list[Team] = self._data_api.load_teams()
        team = next((t for t in teams if t.uuid == team_uuid), None)

        if team is None:
            raise Exception('Team not found!')

        if team.team_captain_uuid == player.uuid:
            raise Exception('You must promote a new captain before leaving your team!')

        team.list_player_uuid.remove(player.uuid)
        self._data_api.update_team(team.uuid, team)

    def list_players(self) -> list[Player]:
        """ Returns a list of stored players. """

        players: list[Player] = DataLayerAPI.load_players()
        return players

    def get_player_object(self, player_uuid: str) -> Player:
        ''' Takes in a players UUID and returns the players object. '''

        players: list[Player] = DataLayerAPI.load_players()
        player = next((p for p in players if p.uuid == player_uuid), None)

        if player is None:
            raise Exception(f"No player found with UUID: {player_uuid}")

        return player


    def save_player(self, player_handle=None):
        if player_handle is not None:
            self.player = player_handle
        return self.player