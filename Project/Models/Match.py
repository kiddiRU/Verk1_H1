"""
Author: Elmar Sigmarsson > elmars25@ru.is <
Date: 2025-12-02

Match model class

Contributor:
    Ísak Elí Hauksson <isak25@ru.is>
"""

from datetime import date, time


class Match:
    """
    Represents a match in a tournament.

    Stores information about the competing teams, match date and time,
    and results if available.

    :param uuid: Unique identifier for the match
    :type uuid: str
    :param tournament_id: UUID of the tournament where the match is held
    :type tournament_id: str
    :param match_date: Date of the match (YYYY-MM-DD)
    :type match_date: date
    :param match_time: Time of the match
    :type match_time: time
    :param team_1: UUID of the first team
    :type team_1: str
    :param team_2: UUID of the second team
    :type team_2: str
    :param winner: UUID of the winning team, or None if not yet played
    :type winner: str | None
    :param winning_players: List of UUIDs of winning team players, or None
    :type winning_players: list[str] | None
    :param losing_team: UUID of the losing team, or None if not yet played
    :type losing_team: str | None
    :param losing_players: List of UUIDs of losing team players, or None
    :type losing_players: list[str] | None
    :rtype: None
    """

    def __init__(
        self,
        uuid: str,
        tournament_id: str,
        match_date: date,
        match_time: time,
        team_1: str,
        team_2: str,
        winner: None | str = None,
        winning_players: None | list[str] = None,
        losing_team: None | str = None,
        losing_players: None | list[str] = None,
    ) -> None:
        """
        Initialize a Match instance.

        Sets all match details, including participating teams, date, time,
        and optionally results if the match has concluded.

        :param uuid: Unique identifier for the match
        :param tournament_id: UUID of the tournament where the match is held
        :param match_date: Date of the match (YYYY-MM-DD)
        :param match_time: Time of the match
        :param team_1: UUID of the first team
        :param team_2: UUID of the second team
        :param winner: UUID of the winning team, or None if not yet played
        :param winning_players: List of UUIDs of winning team players, or None
        :param losing_team: UUID of the losing team, or None if not yet played
        :param losing_players: List of UUIDs of losing team players, or None
        :rtype: None
        """

        self.uuid = uuid
        self.tournament_id = tournament_id
        self.match_date = match_date
        self.match_time = match_time
        self.team_1 = team_1
        self.team_2 = team_2
        self.winner = winner
        self.winning_players = winning_players
        self.losing_team = losing_team
        self.losing_players = losing_players
