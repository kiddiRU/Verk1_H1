"""
Author: Elmar Sigmarsson <elmars25@ru.is>
Date: 2025-12-08

Functions for Club logic
"""

from uuid import uuid4
from DataLayer import DataLayerAPI
from Models import Club, Team
from LogicLayer.Validation import validate_attr
from LogicLayer.LogicUtility import get_club_uuid

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


    def list_clubs(self): 
        """Returns a list of stored clubs"""

        clubs: list[Club] = DataLayerAPI.load_clubs()
        return clubs

        
    def get_teams_in_club(self, club_name: str) -> list[Team]:
        """
        Takes in club name

        Goes through all teams and appends to a lis every team that is in the club
        """

        teams_in_club: list = []
        club_uuid: str = get_club_uuid(club_name)
        model_teams: list = DataLayerAPI.load_teams()

        for team in model_teams:
            if team.club_uuid == club_uuid:
                teams_in_club.append(team)

        return teams_in_club