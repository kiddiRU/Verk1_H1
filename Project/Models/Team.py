"""
Author: Ísak Eli Hauksson <isak25@ru.is>
Date: 2025-12-02

Team Model Class
"""


class Team:
    """
    Represents a team within a club, including its players,
    captain, tournament participation, and optional
    metadata such as a homepage URL and ASCII art logo.

    Each team has a unique name and identifier,
    and keeps track of the players that belong to it.
    Teams can optionally be associated with a tournament and a club.

    :param uuid: Unique identifier for the team.
    :type uuid: str
    :param name: Unique team name (3-39 characters).
    :type name: str
    :param list_player_uuid: List of UUIDs of players in the team.
    :type list_player_uuid: list[str]
    :param team_captain_uuid: UUID of the team captain.
    :type team_captain_uuid: str
    :param club_uuid: UUID of the club associated with the team.
    :type club_uuid: str
    :param in_tournament: UUID of the tournament the team is
    participating in, or None.
    :type in_tournament: str | None
    :param url_homepage: Optional URL for the team's homepage.
    :type url_homepage: str
    :param ascii_art: Optional ASCII art logo for the team.
    :type ascii_art: str
    :rtype: None
    """
    def __init__(
        self,
        uuid: str,
        name: str,
        list_player_uuid: list[str],
        team_captain_uuid: str,
        club_uuid: str,
        in_tournament: None | str,
        url_homepage: str = "",
        ascii_art: str = "",
    ) -> None:
        """
        Initialize a Team object.

        Represents a team within a club, including players,
        captain, and tournament participation.
        Can optionally include a homepage URL and ASCII art logo.

        :param uuid: Unique identifier for the team
        :param name: Unique name for the team (3-39 characters)
        :param list_player_uuid: List of UUIDs of players in the team
        :param team_captain_uuid: UUID of the team captain
        :param club_uuid: UUID of the club the team belongs to
        :param in_tournament: UUID of the tournament the team is in, or None
        :param url_homepage: Optional URL of the team's homepage
        :param ascii_art: Optional ASCII art logo for the team
        :rtype: None
        """

        self.uuid = uuid
        self.name = name
        self.list_player_uuid = list_player_uuid
        self.team_captain_uuid = team_captain_uuid
        self.club_uuid = club_uuid
        self.in_tournament = in_tournament
        self.url_homepage = url_homepage
        self.ascii_art = ascii_art
