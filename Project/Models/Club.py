"""
Author: Elmar Sigmarsson > elmars25@ru.is <
Date: 2025-12-02

Club model class

Contributor:
    Ísak Elí Hauksson <isak25@ru.is>
"""


class Club:
    """
    Represents a club, including its name, color, country, and hometown.

    Each club has a unique identifier and stores basic information
    about the club's identity.

    :param uuid: Unique identifier for the club.
    :type uuid: str
    :param name: Name of the club (3-39 characters).
    :type name: str
    :param club_color: (RED, BLUE, YELLOW, GREEN).
    :type club_color: str
    :param country: Country of the club's origin (3-39 characters).
    :type country: str
    :param home_town: Club's hometown (3-39 characters).
    :type home_town: str
    :rtype: None
    """

    def __init__(
        self,
        uuid: str,
        name: str,
        club_color: str,
        country: str,
        home_town: str,
    ) -> None:
        """
        Initialize a Club object.

        Stores basic information about a club.

        :param uuid: Unique identifier for the club.
        :param name: Name of the club.
        :param club_color: Name of the club color.
        :param country: Country of origin.
        :param home_town: Club's hometown.
        :rtype: None
        """

        self.uuid = uuid
        self.name = name
        self.club_color = club_color
        self.country = country
        self.home_town = home_town
