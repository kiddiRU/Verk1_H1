"""
Author: Elmar Sigmarsson <elmars25@ru.is>
Date: 2025-12-03

Created the PlayerLL class and added the functions
"""

##TODO add nessecery imports
from uuid import uuid4
from DataLayer import DataLayerAPI
from Models.Player import Player
from Models.Team import Team
from LogicLayer.Validation import validate, validate_name, validate_home_address, validate_phone_number, validate_date, validate_unique_name, validate_email

class PlayerLL():
    def __init__(self, data_api: DataLayerAPI) -> None:
        self._data_api: DataLayerAPI = data_api


    """info from player to validate"""

    #TODO call a file that checks validations for name
    def validate_name(self):
        pass

    #TODO call a file that checks validations for date of birth
    def validate_date_of_birth(self):
        pass

    #TODO call a file that checks validations for name
    def validate_home_address(self):
        pass
    
    #TODO call a file that checks validations for email
    def validate_email(self):
        pass
    
    #TODO call a file that checks validations for phone number
    def validate_phone_number(self):
        pass
    
    #TODO call a file that checks validations for unique handle
    def validate_handle(self):
        pass

    """
    Takes in player info.

    Validates the given info, creates a player object if valid. Sends the 
    object to the data layer to be stored and returns the new player
    """
    def create_player(self,
                name: str,
                date_of_birth: str,
                home_address: str,
                email: str,
                phone_number: str,
                handle: str,
                url: str
                ) -> Player:
        
        uuid = str(uuid4())

        params: dict[str, str] = {k: v for k, v in locals().copy().items() if not k == 'self'}
        for attr, value in params.items():
            try:
                validate(attr, value.strip(), name_type = 'PLAYER')
            except Exception as error:
                raise error

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
        except Exception as error:
            raise error
        
        return new_player

    '''
    Takes in a Player object and potential attribute updates.

    Sends updated values to the data layer, and returns and updated Player object.
    '''
    def change_player_info(
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
        
        params: dict[str, str] = {k: v for k, v in locals().items() if k not in ('self', 'player')}
        for attr, value in params.items():
            if value == '':
                continue
            
            try:
                validate(attr, value, name_type='PLAYER')
                setattr(player, attr, value)
            except Exception as error:
                raise error
        
        player_attr: dict[str, str] = player.__dict__.items()
        for k, v in player_attr:
            self._data_api.update_player(player.uuid, k, v)

        updated_player = player
        return updated_player
    
    '''
    Takes in the teams name, its captain, club, url and ascii art.

    Creates a new Team object and sends it the data layer to be stored.
    '''
    # TODO Fetch club uuid once ClubIO has been implemented. Return new Team? 
    def create_team(self, name: str, team_captain: Player, club: str, url: str, ascii_art: str) -> Team:
        self.uuid = str(uuid4())

        # At the moment the clubs name is registerd, not its uuid
        new_team = Team(self.uuid, name, [team_captain.uuid], team_captain.uuid, club, None, url, ascii_art)

        self._data_api.store_team(new_team)
        
        # return new_team ?

        

    #TODO implement leaving a team
    def leave_team(self, name: str, team: str) -> None:
        pass


    """function for viewing players"""

    #TODO implement 
    def list_players(self) -> list[Player]:
        
        model_players: list = DataLayerAPI.load_players()
        return model_players
    
    
    def get_player_info(self, player_uuid) -> Player:
        
        model_players: list = DataLayerAPI.load_players()
        
        for player in model_players:
            if player.uuid == player_uuid:
                return player
