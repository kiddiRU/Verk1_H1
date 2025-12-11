"""
Author: Elmar Sigmarsson <elmars25@ru.is>
Date: 2025-12-08

Functions for Club logic
"""

from uuid import uuid4
from DataLayer import DataLayerAPI
from Models import Club, Team, Match, Tournament, ValidationError
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
        First takes in the info that has already been validated
        and creates a uuid for the club,
        Then creates the object using the uuid and info and
        points the object to Data Layer API to be stored as a club        

        :param name:
            The name of the club
        :type name: str

        :param club_color:
            The color of the club
        :type club_color: str

        :param country:
            The country of the club
        :type country: str

        :param home_town:
            The home town of the club
        :type home_town: str

        :return: Returns the newly created club object
        :rtype: Club
        """       
        uuid = str(uuid4())

        new_club = Club(uuid, name, club_color, country, home_town)

        DataLayerAPI.store_club(new_club)
        return new_club


    def list_all_clubs(self) -> list[Club]: 
        """
        Loads a list of all club objects from the Data Layer API

        :return: Returns a list of all club objects
        :rtype: list[Club]
        """

        clubs: list[Club] = DataLayerAPI.load_clubs()
        return clubs

        
    def get_teams_in_club(self, club_name: str) -> list[Team]:
        """Gets club name

        First gets the clubs uuid,
        Then loads all team objects and
        lists all team objects that have the club uuid of the wanted club
        
        :param club_name:
            club name to find all teams that are in the club
        :type club_name: str

        :return: Returns a list of team objects that are in the club
        :rtype: list[Team]
        """
        # Loads all team objects and get the clubs uuid
        teams_in_club: list[Team] = []
        club_uuid: str = self.get_club_by_name(club_name).uuid
        model_teams: list[Team] = DataLayerAPI.load_teams()

        # Loops through all team objects 
        for team in model_teams:

            # adds a team to the list when the uuid's match
            if team.club_uuid == club_uuid:
                teams_in_club.append(team)

        return teams_in_club
    

    def get_club_wins(self, club_name: str) -> str:
        """Gets club name
        
        First gets the uuid of the club
        Then Loads all teams and finds all the teams in the club
        and lists their team uuid's

        Then Loads all matches and if the match winner
        is in the list of teams in the club one is added to the count
        
        :param club_name:
            The clubs name to find the total won matches
        :type club_name: str

        :return: 
        Returns a string number of the total won matches
        of the teams in the club
        :rtype: str
        """
        # Loads matches and team objects
        # gets the club uuid and starts a win counter
        model_matches: list[Match] = DataLayerAPI.load_matches()
        model_teams: list[Team] = DataLayerAPI.load_teams()
        club_uuid: str = self.get_club_by_name(club_name).uuid
        win_count: int = 0

        # Lists all teams uuid's that are in the club
        teams_in_club: list[str] = [
            team.uuid for team in model_teams
            if team.club_uuid == club_uuid
            ]

        # Loops through all match objects
        for match in model_matches:

            # Adds +1 to win counter if the match winner
            # is in the list of teams
            if match.winner in teams_in_club:
                win_count += 1

        return str(win_count)
        


    def get_club_points(self, club_name: str) -> str:
        """Gets the club name

        First gets the uuid of the club,
        Then Loads all teams and finds all the teams in the club
        and lists their team uuid's

        Then loads all tournaments and gets a list of all matches in a
        the tournament with the tournament uuid,
        Finds the last match of the tournament (Finals) and finds the
        winning and losing teams of the match, and if the winner is in
        the list of teams of the club 3 points are added
        and 1 point for the loser

        :param club_name:
            The name of the club to find the total points from tournaments
        :type club_name: str

        :return: Returns a string number of the total points from tournaments
        :rtype: str
        """
        # Loads tournaments and team objects
        # Gets the clubs uuid and starts a point counter
        model_tournaments: list[Tournament] = DataLayerAPI.load_tournaments()
        model_teams: list[Team] = DataLayerAPI.load_teams()
        club_uuid: str = self.get_club_by_name(club_name).uuid
        match = MatchLL()
        points: int = 0

        # Lists all team's uuid's that are in the club
        teams_in_club: list[str] = [
            team.uuid for team in model_teams
            if team.club_uuid == club_uuid
            ]
        
        # Loops through all tournament objects
        for tournament in model_tournaments:           
            try:
                matches_list: list[Match] = match.get_matches(tournament.uuid)

                # gets the final match of the tournament (Finals)
                tour_final_match: Match = matches_list[-1]

                # gets the winning and losing teams
                winner = tour_final_match.winner
                loser = tour_final_match.losing_team

                # if the winning team is in the list of teams in club
                if winner in teams_in_club:
                    points += 3

                # if the losing team is in the list of teams in club
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