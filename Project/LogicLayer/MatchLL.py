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


class MatchLL:
    """ Match logic."""

    def __init__(self) -> None:
        pass

    def create_match(
        self,
        tournament_id: str,
        match_date: date,
        match_time: time,
        team_1: str,
        team_2: str
    ) -> Match:
        """Creates new Match object, sends it to be
        stored and returns the new Match object.

        :param tournament_id:
            The UUID of the tournament the match should belong to.
        :type tournament_id: str

        :param date:
            The date of the match.
        :type date: date

        :param time:
            The time of the match.
        :type time: time

        :param team_1:
            The UUID of one team playing in the match.
        :type team_1: str

        :param team_2:
            The UUID of the other team playing in the match.
        :type team_2: str

        :return:
            Returns the new Match object.
        :rtype: Match
        """
        # Create a new Match object with a unique UUID.
        uuid: str = str(uuid4())
        new_match: Match = Match(
            uuid,
            tournament_id,
            match_date,
            match_time,
            team_1,
            team_2
        )

        # Send the new Match object to be stored, and return it.
        DataLayerAPI.store_match(new_match)
        return new_match

    def get_matches(self, tournament_uuid: str) -> list[Match]:
        """Gets a list of all matches in the tournament
        with the given UUID, sorted by their date and time.

        :param tournament_uuid:
            The tournament uuid to get all matches from
        :type tournament_uuid: str

        :return:
            Returns a list of Match objects.
        :rtype: list[Match]
        """
        # Loads all matches and lists the matches in a specific tournament
        model_matches: list[Match] = DataLayerAPI.load_matches()
        model_matches: list[Match] = [
            match
            for match in model_matches
            if match.tournament_id == tournament_uuid
        ]

        # Sorts the list of matches by their date and time
        sorted_matches: list[Match] = sorted(
            model_matches,
            key=lambda match: (match.match_date, match.match_time)
        )

        return sorted_matches

    def change_match_winner(
        self,
        match_uuid: str,
        team_uuid: str
    ) -> Match | None:
        """Updates match winner of a specific match in a specific tournament.

        Given the uuid of a specific tournament and the uuid of a
        specific match, will update the winner of this match, will set a new
        match into the server used if needed, will move onto next round of
        tournament if needed and will archive tournament if needed.

        :param tournament_uuid:
            The uuid of the tournament which the match belongs to.

        :param match_uuid:
            The uuid of the match you want to update.

        :param team_uuid:
            The uuid of the winner.
        """
        # Get lists of matches and teams.
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

    def get_match(
        self,
        tournament_uuid: str,
        match_team1_uuid: str,
        match_team2_uuid: str
    ) -> Match | str:
        """Finds the match of two teams competing in a tounrnament.

        :param tournament_uuid:
            The UUID of the tournament the teams are competing in.
        :type tournament_uuid: str

        :param team1_uuid:
            The UUID of one team.
        :type team1_uuid: str

        :param team2_uuid:
            The UUID of the other team.
        :type team2_uui: str

        :return:
            If a match is found with the two teams, an object of that match
            is returned, else an empty string.
        :rtype: Match | str
        """
        # Loads all match objects in a tournament
        matches: list[Match] = self.get_matches(tournament_uuid)

        # Looks for a match with both teams in it
        for match in matches:
            if (
                match.team_1 == match_team1_uuid
                and match.team_2 == match_team2_uuid
            ):
                return match

        return ""
