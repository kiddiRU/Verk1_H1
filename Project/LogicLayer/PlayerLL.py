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
from LogicLayer.Validation import validate_name, validate_home_address, validate_phone_number, validate_date, validate_unique_name, validate_email

class PlayerLL():


    def __init__(self) -> None:
        pass


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

    
    """functions for player"""

    #TODO implement creating a player
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
        Validates player info, sends info to Player file in Module folder
        to create a player
        """
        name_stripped: str = name.strip()
        date_of_birth_stripped: str = date_of_birth.strip()
        home_address_stripped: str = home_address.strip()
        email_stripped: str = email.strip()
        phone_number_stripped: str = phone_number.strip()
        handle_stripped: str = handle.strip()
        url_stripped: str = url.strip()

        # Sends the player info to validation file to check for validation
        #TODO implement what to do if the validation returns False
        uuid = uuid4
        final_name = validate_name(name_stripped)
        final_date_of_birth = validate_date(date_of_birth_stripped)
        final_home_address = validate_home_address(home_address_stripped)
        final_email = validate_email(email_stripped)
        final_phone_number = validate_phone_number(phone_number_stripped)
        final_handle = validate_unique_name(handle_stripped)
        final_url = url_stripped

        # sends the info to the Player module class to create a player
        player = Player(uuid, final_name, final_date_of_birth, final_home_address, final_email, final_phone_number, final_handle, final_url)
        
        # tries to input the player to the DataLayerAPI
        try:
            DataLayerAPI.store_player(player)

        #TODO add error message 
        except:
            return ""


    #TODO implement changing player info
    def change_player_info(self, ) -> None:
        pass

    #TODO implement creating a team
    def create_team(self, name: str, club: str, url: str, ascii_art: str) -> Team:
        
        # Calls a function 

        self.uuid = uuid4

    #TODO implement leaving a team
    def leave_team(self, name: str, team: str) -> None:
        pass


    """function for viewing players"""

    #TODO implement 
    def list_players(self) -> list[Player]:
        pass
    
    
    def get_player_info(self) -> Player:
        pass
    