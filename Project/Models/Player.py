"""
Author: Elmar Sigmarsson <elmars25@ru.is>
Date: 2025-12-02

Model class for Players

Contributors:
    Kristinn Hrafn <kristinnd25@ru.is>
    Ísak Elí Hauksson <isak25@ru.is>
"""


class Player:
    """
    Represents a player in the system.

    Stores personal information, contact details, and in-game handle.

    :param uuid: Unique identifier for the player
    :type uuid: str
    :param name: Full name of the player (3-39 characters)
    :type name: str
    :param date_of_birth: Player's date of birth (YYYY-MM-DD)
    :type date_of_birth: str
    :param home_address: Player's home address (street name number city)
    :type home_address: str
    :param email: Player's email address
    :type email: str
    :param phone_number: Player's phone number (8 digits (xxx-xxxx))
    :type phone_number: str
    :param handle: Unique in-game handle (3-39 characters)
    :type handle: str
    :param url: Optional URL to player's social or homepage
    :type url: str
    :rtype: None
    """

    def __init__(
        self,
        uuid: str,
        name: str,
        date_of_birth: str,
        home_address: str,
        email: str,
        phone_number: str,
        handle: str,
        url: str = "",
    ) -> None:
        """
        Initialize a Player instance.

        Sets all personal and contact details along with in-game handle.

        :param uuid: Unique identifier for the player
        :param name: Full name of the player (3-39 characters)
        :param date_of_birth: Player's date of birth (YYYY-MM-DD)r
        :param home_address: Player's home address (street name number city)
        :param email: Player's email address
        :param phone_number: Player's phone number (8 digits (xxx-xxxx))
        :param handle: Unique in-game handle (3-39 characters)
        :param url: Optional URL to player's social or homepage
        :rtype: None
        """

        self.uuid = uuid
        self.name = name
        self.date_of_birth = date_of_birth
        self.home_address = home_address
        self.email = email
        self.phone_number = phone_number
        self.handle = handle
        self.url = url
