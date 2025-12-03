"""
Author: Elmar Sigmarsson > elmars25@ru.is <
Date: 2025-12-02

Club model class
"""


class Club:
    """Club model class"""

    def __init__(
        self,
        uuid: str,
        name: str,
        list_teams_uuid: list[str],
        club_color: str,
        country: str,
        home_town: str,
    ) -> None:
        """
        The initializer for the Club model class

        Args:
            uuid (str): unique identifier
            name (str): name of club (3-30 char length)
            list_teams_uuid (list[str]): list of all teams associated with the club
            club_color (str): name of the club color (RED, BLUE, YELLOW, GREEN)
            country (str): clubs home country (3-30 char length)
            home_town (str): clubs home town (3-30 char length)
        """

        self.uuid = uuid
        self.name = name
        self.list_teams_uuid = list_teams_uuid
        self.club_color = club_color
        self.country = country
        self.home_town = home_town
