"""
Author: Elmar Sigmarsson <elmars25@ru.is>
Date: 2025-12-03

Created the PlayerLL class and added the functions
"""

# TODO add nessecery imports
from uuid import uuid4
from DataLayer import DataLayerAPI
from Models import Player, Team, ValidationError
from LogicLayer.Validation import validate

class PlayerLL():
    def __init__(self, data_api: DataLayerAPI) -> None:
        self._data_api: DataLayerAPI = data_api

<<<<<<< HEAD
    # TODO Alter validation functionality?
=======
    """
    Takes in player info.

    Validates the given info, creates a player object if valid. Sends the 
    object to the data layer to be stored and returns the new player
    """
    # B-requirement allow player to input attribute one at a time which allows the user to know errors
>>>>>>> ffdaaf470264cebd72b926a96f386cebc4c6e1c6
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
            try:
                validate(attr, value.strip(), name_type = 'PLAYER')
            except Exception:
                raise

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

        try:
            DataLayerAPI.store_player(new_player)
        except Exception:
            raise
        
        return new_player

    # TODO Alter validation functionality?
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
            
            try:
                validate(attr, value, name_type='PLAYER')
                setattr(player, attr, value)
            except Exception:
                raise
        
        try:
            self._data_api.update_player(player.uuid, player)
        except Exception:
            raise

        return player
    
    # TODO Fetch club uuid once ClubIO has been implemented. Return new Team? 
    def create_team(self, name: str, team_captain: Player, club: str, url: str, ascii_art: str) -> Team:
        '''
        Takes in the teams name, its captain, club, url and ascii art.

        Creates a new Team object, sends it the data layer to be stored and returns it.
        '''

        uuid = str(uuid4())

        # At the moment the clubs name is registerd, not its uuid
        new_team = Team(uuid, name, [team_captain.uuid], team_captain.uuid, club, None, url, ascii_art)

        try:
            self._data_api.store_team(new_team)
        except Exception:
            raise
        
        return new_team
        

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

    # TODO implement 
    def list_players(self) -> list[Player]:
        """ Returns a list of stored players. """

        model_players: list = DataLayerAPI.load_players()
        return model_players
    
    
    def get_player_info(self, player_uuid) -> Player:
        
        model_players: list = DataLayerAPI.load_players()
        
        for player in model_players:
            if player.uuid == player_uuid:
                return player
