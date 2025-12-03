"""
Author: Elmar Sigmarsson
Date: 2025-12-03

Created the PlayerLL class and added the functions
"""

##TODO add nessecery imports
from uuid import uuid4
from Models.Player import Player
from Models.Team import Team

class PlayerLL():
    def __init__(self):
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
                home_address: str,
                phone_number: str,
                date_of_birth: str,
                handle: str,
                email: str,
                url: str
                ) -> Player:
        
        # sends name to a validation file to check for validation
        # sends home address to a validation file to check for validation
        # sends phone number to a validation file to check for validation
        # sends date of birth to a validation file to check for validation
        # sends handle to a validation file to check for validation 
        # sends email to a validation file to check for validation 

        self.uuid = uuid4

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
    