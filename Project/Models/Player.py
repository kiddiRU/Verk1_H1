"""
Author: Elmar Sigmarsson <elmars25@ru.is>
Date: 2025-12-02

Model class for Players

Contributers:
    Kristinn Hrafn <kristinnd25@ru.is>
"""

class Player():
    """Player model class"""
    def __init__(self,
                 uuid: str,
                 name: str,
                 date_of_birth: str,
                 home_address: str,
                 email: str,
                 phone_number: int,
                 handle: str,
                 url: str = "") -> None:
        
        """
        Arguments:
            uuid (str): unique id tied to the player to store and lookup
            name (str): full name (3-30 char lengt)
            date_of_birth (str): players date of birth (YYYY-MM-DD)
            home_address (str): players home_address (street_name street_number, Frostafold 12)
            email (str): players email (johnDoe@gmail.com) 
            phone_number (int): 1234567
            handle (str): players handle ingame has to be UNIQE (3-30 char lengt)
            url (str): url to players social (optional)
        """

        self.uuid = uuid
        self.name = name
        self.date_of_birth = date_of_birth
        self.home_address = home_address
        self.email = email
        self.phone_number = phone_number
        self.handle = handle
        self.url = url    
