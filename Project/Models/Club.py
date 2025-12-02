""" Creator Elmar Sig"""

class Club():
    """ Club model class"""
    def __init__(
        self,
        name: str,
        list_teams_uuid: list[str],
        club_color: str,
        country: str,
        home_town: str,
    ) -> None:

        """
        The initializer for the Club model class

        name (str): name of club (3-30 char lengt)
        list_teams_uuid (list[str]): list of all teams associated with the club
        club_color (str): name of the club color (RED, BLUE, YELLOW, GREEN)
        country (str): clubs home country (3-30 char lengt)
        home_town (str): clubs home town (3-30 char lengt)
        """

        self.name = name
        self.list_teams_uuid = list_teams_uuid
        self.club_color = club_color
        self.country = country
        self.home_town = home_town