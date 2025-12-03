"""
Author: Ísak Eli Hauksson <isak25@ru.is>
Date: 2025-12-02

Team Model Class
"""


class Team:
    def __init__(
        self,
        name: str,
        list_player_uuid: list[str],
        team_captain_uuid: str,
        club_uuid: str,
        in_tournament: None | str,
        url_homepage: str = "",
        ascii_art: str = "",
    ) -> None:
        """
        The initializer for the Team model class

        Args:
            name (str): an unique name for the team (3-30 char length)
            list_player_uuid (list[str]): players apart of the team
            team_captain_uuid (str): uuid of the player captain
            club_uuid (str): uuid of the club connected to the team
            in_tournament (None | str): None or string for the uuid of the tournament
            url_homepage (str, optional): url link to a teams homepage. Defaults to "".
            ascii_art (str, optional): ascii art logo for a team. Defaults to "".
        """

        self.name = name
        self.list_player_uuid = list_player_uuid
        self.team_captain_uuid = team_captain_uuid
        self.club_uuid = club_uuid
        self.in_tournament = in_tournament
        self.url_homepage = url_homepage
        self.ascii_art = ascii_art
