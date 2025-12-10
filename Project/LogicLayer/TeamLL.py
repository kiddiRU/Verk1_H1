"""
Author: Elmar Sigmarsson <elmars25@ru.is>
Date: 2025-12-03

Created the TeamLL class and added the functions
"""

from Models import Team, ValidationError
from DataLayer import DataLayerAPI
from Models import Team
from Models import Player
from Models import Tournament
from Models import Match
from LogicLayer.MatchLL import MatchLL
from LogicLayer.ClubLL import ClubLL
from LogicLayer.LogicUtility import get_player_uuid, get_players_team_uuid, get_team_uuid

class TeamLL():
    def __init__(self) -> None:
        pass

    def add_player(self, player_handle: str, current_player: Player) -> Team | str:
        """
        Takes in team uuid and a player,
        First looks through all teams to see if the player uuid is already in a team
        then looks through a list of all the teams and 
        finds the right team uuid and
        adds the new player uuid to the teams player list 
        """
        player_uuid: str = get_player_uuid(player_handle)
        team_uuid: str = get_players_team_uuid(current_player.uuid)
        model_teams: list[Team] = DataLayerAPI.load_teams()


        for team in model_teams:            
            if team.uuid == team_uuid:
                if len(team.list_player_uuid) == 5:
                    return "Your Team Is Full"

                else:
                    team.list_player_uuid.append(player_uuid)
                    DataLayerAPI.update_team(team_uuid, team)
                    return team
                
        return ""
                    


    def remove_player(self, player_handle: str, current_player: Player) -> Team:
        """
        Takes in team uuid and a player uuid,
        Looks through a list of all the teams and 
        finds the right team uuid and
        checks if the player is the team captain and if so he can not be removed
        otherwise removes the player uuid from the teams player list
        try-except for if the player uuid is not in the team 
        """
        player_uuid: str = get_player_uuid(player_handle)
        team_uuid: str = get_players_team_uuid(current_player.uuid)
        model_teams: list[Team] = DataLayerAPI.load_teams()
        
        for team in model_teams:
            if team.uuid == team_uuid:
                if player_uuid == team.team_captain_uuid:
                    raise ValidationError("Can't remove team captain from team")

                else:
                    try:
                        team.list_player_uuid.remove(player_uuid)
                        DataLayerAPI.update_team(team_uuid, team)
                        return team

                    except ValueError:
                        raise ValidationError("Player not in team")

        raise ValidationError("Team not found")
    

    def get_team_members(self, team_name: str) -> list[str]:
        """
        Takes in team uuid
        Looks through a list of all the teams and
        finds the right team uuid and
        returns a list of the team members uuid
        """        
        model_teams: list[Team] = DataLayerAPI.load_teams()
        for team in model_teams:
            if team.name == team_name:
                return team.list_player_uuid 
            
        raise ValidationError("Team not found")
    

    def list_teams(self): 
        """Returns a list of stored clubs"""

        teams: list[Team] = DataLayerAPI.load_teams()
        return teams


    def get_team_object(self, team_name: str) -> Team:
        """
        Takes in the uuid
        Looks through a list of all the teams and
        finds the right team uuid and
        returns the model class of the team
        """
        
        model_teams: list = DataLayerAPI.load_teams()
        for team in model_teams:
            if team.name == team_name:
                return team

        raise ValidationError("Team not found")


    #TODO implement if the team won the tournament add WIN and LOST to if they lost
    def get_team_history(self, team_name: str) -> list[str]:
        """
        Takes in team uuid,
        looks through a list of all the tournaments
        and finds every tournament the team uuid is in (team played in tournament)
        returns a list of those tournaments
        """
        teams_history: list = []
        team_uuid: str = get_team_uuid(team_name)

        model_tournaments: list = DataLayerAPI.load_tournaments()
        for tournament in model_tournaments:
            if team_uuid in tournament.teams_playing: 
                teams_history.append(tournament.name)

        return teams_history
    

    def get_team_wins(self, team_name: str) -> str:
        """
        takes in a team name and finds the team uuid from name
        loads and looks through all matches 
        and adds one to counter for ever match won
        returns the count
        """
        model_matches: list[Match] = DataLayerAPI.load_matches()
        team_uuid: str = get_team_uuid(team_name)
        win_count = 0

        for match in model_matches:
            if match.winner == team_uuid:
                win_count += 1
        
        return str(win_count)
            
    

    # TODO Implement so a team gets a point for every match it wins 
    # and the points increase. Match 1 win: +1, Match 2 win: +2,
    # Match 3 loss: total 3 points for tournament 
    def get_team_points(self, team_name: str) -> str:
        """
        takes in a team name and finds the team uuid from name
        loads and looks through all tournament and takes there uuid
        looks through every match in tournament and checks the last match
        if the winning team uuid is the same as the team uuid
        three points are added
        returns points
        """
        model_tournaments: list[Tournament] = DataLayerAPI.load_tournaments()
        team_uuid: str = get_team_uuid(team_name)
        match = MatchLL()
        points = 0

        for tournament in model_tournaments:
            try:
                matches_list: list[Match] = match.get_matches(tournament.uuid)
                tour_final_match: Match = matches_list[-1]
                winner = tour_final_match.winner
                loser = tour_final_match.losing_team

                if winner == team_uuid:
                    points += 3

                if loser == team_uuid:
                    points += 1

            except:
                pass

        return str(points)
    

    def get_team_club(self, team_name: str) -> str:
        clubll = ClubLL()

        clubs = clubll.list_clubs()

        for club in clubs:
            teams = clubll.get_teams_in_club(club.name)

            if team_name in teams:
                return club.name
        
        return ""
