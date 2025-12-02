"""
<<<<<<< HEAD
Author: Elmar Sigmarsson > elmars25@ru.is <
Date: 2025-12-02

Player model class
=======
Author: Elmar Sig > elmars25@ru.is <
Date: 2025-12-02

Model class for Players
>>>>>>> bce1c28 (PlayerIO class with write function, not tested)
"""

class Player():
    """Player model class"""
    def __init__(self,
                 name: str,
                 date_of_birth: str,
                 home_address: str,
                 email: str,
                 phone_number: int,
                 handle: str,
                 url: str = "") -> None:
        
        """
        Args:
            name (str): full name (3-30 char lengt)
            date_of_birth (str): players date of birth (YYYY-MM-DD)
            home_address (str): players home_address (street_name street_number, Frostafold 12)
            email (str): players email (johnDoe@gmail.com) 
            phone_number (int): 1234567
            handle (str): players handle ingame has to be UNIQE (3-30 char lengt)
            url (str): url to players social (optional)
        """

        self.name = name
        self.date_of_birth = date_of_birth
        self.home_address = home_address
        self.email = email
        self.phone_number = phone_number
        self.handle = handle
        self.url = url

    
