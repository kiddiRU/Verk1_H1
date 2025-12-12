"""
Author: Elmar Sigmarsson <elmars25@ru.is>
Date: 2025-12-08

Functions for Match logic
"""

from uuid import uuid4
from datetime import date, time
from Models import Match
from Models import Team
from DataLayer import DataLayerAPI

# TODO docstring calss
class MatchLL:
    """ Match Logic"""

    def __init__(self) -> None:
        pass

    # TODO fix docstring
    def create_match(
            self,
            tournament_id: str,
            date: date,
            time: time,
            team_1: str,
            team_2: str
            ) -> Match:
        """
        First takes in the info that has already been validated
        and creates a uuid for the match,
        Then creates the object using the uuid and info and
        points the object to the Data Layer API to be stored as a match

        :param tournament_id:
            The uuid of the tournament that the match belongs to
        :type tournament_id: str

        :param date:
            The date of the match
        :type date: date

        :param time:
            The time of the match
        :type time: time

        :param team_1:
            The uuid of one of the teams playing in the match
        :type team_1: str

        :param team_2:
            The uuid of the other team playing in the match
        :type team_2: str
        """
        uuid: str = str(uuid4())
        new_match: Match = Match(
            uuid,
            tournament_id,
            date,
            time,
            team_1,
            team_2
            )
        DataLayerAPI.store_match(new_match)
        return new_match

    # TODO fix docstring
    def get_matches(self, tournament_id: str) -> list[Match]:
        """Gets the tournament uuid to get matches from

        Loads all matches and lists the matches in a specific tournament,
        then sorts the matches by their date and time

        :param tournament_id:
            The tournament uuid to get all matches from
        :type tournament_id: str

        :return:
            Returns a list of list of match objects
        :rtype: list[Match]
        """
        # Loads all matches and lists the matches in a specific tournament
        model_matches: list[Match] = DataLayerAPI.load_matches()
        model_matches: list[Match] = [
            match
            for match in model_matches
            if match.tournament_id == tournament_id
        ]

        # Sorts the list of matches by their date and time
        sorted_matches: list[Match] = sorted(
            model_matches,
            key=lambda match: (match.match_date, match.match_time)
        )

        return sorted_matches

    # TODO fix docstring
    def change_match_winner(self, match_uuid: str, team_uuid: str) -> Match:
        """Gets the match uuid and the team uuid of the winner

        Docstring for change_match_winner

        :param match_uuid:
            The match uuid of the match to change the winners and losers
        :type match_uuid: str

        :param team_uuid:
            The teams uuid of the winning team
        :type team_uuid: str
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
                for l_team in model_teams:
                    if l_team.uuid == losing_team:
                        # Takes a list of the players on the losing team
                        # stores the losing players
                        losing_players: list[str] = l_team.list_player_uuid
                        match.losing_players = losing_players

                DataLayerAPI.store_match(match)

                return match

    # TODO docstring
    def get_match(
            self,
            tournament_id: str,
            match_team1_uuid: str,
            match_team2_uuid: str
            ) -> Match | str:
        """Gets tournament uuid and both teams uuid's

        Loads all matches and searches for a match that has
        both teams in the match

        :param tournament_id:
            asdf
        :type tournament_id: str

        :param match_team1_uuid:
            asdf
        :type match_team1_uuid: str

        :param match_team2_uuid:
            asdf
        :type match_team2_uuid: str

        :return:
            Returns the Match object,
            if no match is found with those teams and empty string is returned
        :rtype: Match | str
        """
        # Loads all match objects in a tournament
        matches: list[Match] = self.get_matches(tournament_id)

        # Looks for a match with both teams in it
        for match in matches:
            if (
                match.team_1 == match_team1_uuid
                and match.team_2 == match_team2_uuid
            ):
                return match

        return ""
