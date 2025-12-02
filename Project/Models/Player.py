""" Created by: Elmar Sig """

class Player():
    """docstring for Player"""
    def __init__(self,
                 name: str,
                 date_of_birht: str,
                 home_adress: str,
                 email: str,
                 phone_number: int,
                 handle: str,
                 url: str = "") -> None:
        
        """
        Arguments:
            name (str): full name
            date_of_birth (str): players date of birth (YYYY-MM-DD)
            home_adress (str): players home_adress (street_name street_number, Frostafold 12)
            email (str): players email (johnDoe@gmail.com) 
            phone_number (int): 1234567
            handle (str): players handle ingame has to be UNIQE
            url (str): url to players social (optional)
        """

        self.name = name
        self.date_of_birth = date_of_birht
        self.home_adress = home_adress
        self.email = email
        self.phone_number = phone_number
        self.handle = handle
        self.url = url

    