"""
Author: Elmar Sigmarsson <elmars25@ru.is>
Date: 2025-12-08

Functions for Match logic
"""

from uuid import uuid4
from Models.Match import Match
from Models.Team import Team
from DataLayer import DataLayerAPI
from datetime import date,time

class MatchLL():
    
    def __init__(self) -> None:
        pass

    
    def create_match(self, tournament_id: str, date: date, time: time, team_1: str, team_2: str) -> Match:
        """
        takes in tournament id, date, time, team_1 and team_2
        and creates a new match using the info
        """
        uuid = str(uuid4())
        new_match = Match(uuid, tournament_id, date, time, team_1, team_2)
        DataLayerAPI.store_match(new_match)
        return new_match


    def get_matches(self, tournament_id: str) -> list[Match]:
        """
        takes in a tournament uuid
        and finds all matches in the tournament
        and returns list of Match object sorted by their time
        """
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


    def change_match_winner(self, match_uuid: str, team_uuid: str) -> Match:
        """
        takes in match uuid and team uuid of the winning team
        updates the info of a match
        changes the winning and losing team
        and adds a list of all the players in the teams
        """
        model_matches: list[Match] = DataLayerAPI.load_matches()
        model_teams: list[Team] = DataLayerAPI.load_teams()

        for match in model_matches:
            
            # stores the winning team
            if match.uuid == match_uuid and match.winner is None:
                match.winner = team_uuid

                for w_team in model_teams:

                    # stores the winning players
                    if w_team.uuid == team_uuid:
                        winning_players: list[str] = w_team.list_player_uuid
                        match.winning_players = winning_players
            

                # Checks which of the teams is the loser
                if team_uuid != match.team_1:
                    losing_team = match.team_1

                else:
                    losing_team = match.team_2
                
                match.losing_team = losing_team
                # Looks through all teams to find the loser team
                print(f"Losing Team id: {losing_team}")
                for l_team in model_teams:
                    if l_team.uuid == losing_team:
                        # Takes a list of the players on the losing team
                        losing_players: list[str] = l_team.list_player_uuid
                        match.losing_players = losing_players
                        
                DataLayerAPI.store_match(match)

                return match

    
    def get_match(self, tournament_id: str, match_team1: str, match_team2: str) -> Match | str:
        
        matches: list[Match] = self.get_matches(tournament_id)

        for match in matches:
            if match.team_1 == match_team1 and match.team_2 == match_team2:
                return match

        return ""
