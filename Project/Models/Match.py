"""
Author: Elmar Sigmarsson > elmars25@ru.is <
Date: 2025-12-02

Match model class
"""

from datetime import date, time


class Match:
    """Match model class"""

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
        losing_players: None | list[str] = None
    ) -> None:
        """
        Initializer for Match model class

        Args:
            uuid (str): uuid of a match
            tournament_id (str): uuid of the tournament the match is held in
            date (str): date of the match (YYYY-MM-DD)
            time_of_match (str): time of the match (12:34)
            team_1 (str): uuid of the team in the match
            team_2 (str): uuid of the other team in the match
            winner (str): None | uuid of the winning team of the match (when a winner is chosen the match is marked as completed)
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
