"""
Author: Elmar Sigmarsson <elmars25@ru.is>
Date: 2025-12-08

Functions for Club logic
"""

from uuid import uuid4
from DataLayer import DataLayerAPI
from Models import Club, Team, Match, Tournament, ValidationError
from LogicLayer.Validation import validate_attr
from LogicLayer.MatchLL import MatchLL

class ClubLL():

    def __init__(self) -> None:
        pass


    def create_club(self,
        name: str,
        club_color: str,
        country: str,
        home_town: str
        ) -> Club:
        """
        Takes in club info.

        Validates the given info and creates a club object. Sends the
        object to the data layer to be stored and returns the new club.
        """
        
        validate_attr("handle", name, "CLUB")
        validate_attr("name", country)
        validate_attr("name", home_town)
        uuid = str(uuid4())

        new_club = Club(uuid, name, club_color, country, home_town)

        DataLayerAPI.store_club(new_club)
        return new_club


    def list_all_clubs(self): 
        """Returns a list of stored clubs"""

        clubs: list[Club] = DataLayerAPI.load_clubs()
        return clubs

        
    def get_teams_in_club(self, club_name: str) -> list[Team]:
        """
        Takes in club name

        Goes through all teams and appends to a lis every team that is in the club
        """

        teams_in_club: list[Team] = []
        club_uuid: str = self.get_club_by_name(club_name).uuid
        model_teams: list[Team] = DataLayerAPI.load_teams()

        for team in model_teams:
            if team.club_uuid == club_uuid:
                teams_in_club.append(team)

        return teams_in_club
    

    def get_club_wins(self, club_name: str) -> str:
        """
        Takes in club name and gets the club uuid
        loads and looks through all teams and lists
        all teams that are in the club
        loads and looks though all matches and
        if a team in the list wins the counter adds one
        returns the counter 
        """
        model_matches: list[Match] = DataLayerAPI.load_matches()
        model_teams: list[Team] = DataLayerAPI.load_teams()
        club_uuid: str = self.get_club_by_name(club_name).uuid
        win_count = 0

        teams_in_club: list[str] = [
            team.uuid for team in model_teams
            if team.club_uuid == club_uuid
            ]

        for match in model_matches:
            if match.winner in teams_in_club:
                win_count += 1

        return str(win_count)
        


    def get_club_points(self, club_name: str) -> str:
        """
        Takes in club name and gets the club uuid
        loads and looks through all teams and lists
        all teams that are in the club
        Loads through all tournaments and checks the last match
        and if the winning team uuid is in the list of teams
        three points are added
        and if the losing team uuid is in the list of teams
        one point is added
        returns points
        """
        model_tournaments: list[Tournament] = DataLayerAPI.load_tournaments()
        model_teams: list[Team] = DataLayerAPI.load_teams()
        club_uuid: str = self.get_club_by_name(club_name).uuid
        match = MatchLL()
        points = 0

        teams_in_club: list[str] = [
            team.uuid for team in model_teams
            if team.club_uuid == club_uuid
            ]
        
        for tournament in model_tournaments:           
            try:
                matches_list: list[Match] = match.get_matches(tournament.uuid)
                tour_final_match: Match = matches_list[-1]
                winner = tour_final_match.winner
                loser = tour_final_match.losing_team

                if winner in teams_in_club:
                    points += 3

                if loser in teams_in_club:
                    points += 1

            except:
                pass

        return str(points)

# Fra utility

    def get_club_by_name(self, club_name: str) -> Club:
        """
        Takes in club name
        looks through all clubs until it finds the right club name
        and returns the teams uuid
        if no team is found an error is raised
        """

        model_clubs: list[Club] = DataLayerAPI.load_clubs()
        for club in model_clubs:
            if club_name == club.name:
                return club
            
        raise ValidationError("Club not found")