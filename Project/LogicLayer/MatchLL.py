"""
Author: Elmar Sigmarsson <elmars25@ru.is>
Date: 2025-12-08

Functions for Match logic
"""

from uuid import uuid4
from Models.Match import Match
from DataLayer import DataLayerAPI
from datetime import date,time

class MatchLL():
    
    def __init__(self) -> None:
        pass

    
    def create_match(self, tournament_id: str, date: date, time: time, team_1: str, team_2: str) -> Match:

        uuid = str(uuid4())
        new_match = Match(uuid, tournament_id, date, time, team_1, team_2)
        DataLayerAPI.store_match(new_match)
        return new_match


    def get_matches(self, tournament_id: str) -> list[Match]:
        model_matches: list[Match] = DataLayerAPI.load_matches()
        model_matches = [
            match
            for match in model_matches
            if match.tournament_id == tournament_id
        ]
        sorted_matches = sorted(
            model_matches,
            key = lambda match: (match.match_date, match.match_time)
        )
        return sorted_matches



