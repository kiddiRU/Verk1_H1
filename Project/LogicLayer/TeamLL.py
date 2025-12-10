"""
Author: Elmar Sigmarsson <elmars25@ru.is>
Date: 2025-12-03

Created the TeamLL class and added the functions
"""

from Models import Team, ValidationError
from DataLayer import DataLayerAPI
from Models import Team, Player, Tournament, Match, Club
from LogicLayer import MatchLL, ClubLL, PlayerLL, Validation
from uuid import uuid4

class TeamLL():
    def __init__(self) -> None:
        self._player_logic: PlayerLL

    def set_player_logic(self, player_logic: PlayerLL) -> None:
        self._player_logic = player_logic

    def set_club_logic(self, club_logic: ClubLL) -> None:
        self._club_logic = club_logic

    def set_match_logic(self, match_logic: MatchLL) -> None:
        self._match_logic = match_logic

    def create_team(self, name: str, team_captain: Player, club_name: str, url: str, ascii_art: str) -> Team:
        '''
        Takes in the teams name, its captain, club, url and ascii art.

        Creates a new Team object, sends it the data layer to be stored and returns it.
        '''
        teams: list[Team] = DataLayerAPI.load_teams()
        players_in_teams: list[str] = [uuid for t in teams for uuid in t.list_player_uuid]

        if team_captain.uuid in players_in_teams:
            raise Exception('You can\'t create a team when you\'re already in one!')

        Validation.validate_attr('handle', name, 'TEAM')
        uuid = str(uuid4())

        clubs: list[Club] = DataLayerAPI.load_clubs()
        club_uuid = next((c.uuid for c in clubs if c.name == club_name), 'NO_CLUB_UUID') # UUID for no club is ..?
        
        new_team = Team(uuid, name, [team_captain.uuid], team_captain.uuid, club_uuid, None, url, ascii_art)

        DataLayerAPI.store_team(new_team)
        return new_team

    def add_player(self, player_handle: str, current_player: Player) -> Team | str:
        """
        Takes in team uuid and a player,
        First looks through all teams to see if the player uuid is already in a team
        then looks through a list of all the teams and 
        finds the right team uuid and
        adds the new player uuid to the teams player list 
        """

        player_uuid: str = self._player_logic.player_handle_to_uuid(player_handle)
        team_uuid: str = self._player_logic.get_players_team_uuid(current_player.uuid)
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
        player_uuid: str = self._player_logic.player_handle_to_uuid(player_handle)
        team_uuid: str = self._player_logic.get_players_team_uuid(current_player.uuid)
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
    

    def list_all_teams(self) -> list[Team]: 
        """Returns a list of stored clubs"""

        teams: list[Team] = DataLayerAPI.load_teams()
        return teams
    
    
    def get_team_members_object(self, team_name: str) -> list[Player]:
        """
        Takes in team name and gets the list of player uuid in the team
        loads and looks through all the players
        and lists all player object that have the player uuid
        return list of player objects in the team
        """
        player_list_uuid: list[str] = self.get_team_members(team_name)

        players = DataLayerAPI.load_players()

        players = [
            player for player in players
            if player.uuid in player_list_uuid
        ]

        return players
        

    #TODO implement if the team won the tournament add WIN and LOST to if they lost
    def get_team_history(self, team_name: str) -> list[str]:
        """
        Takes in team uuid,
        looks through a list of all the tournaments
        and finds every tournament the team uuid is in (team played in tournament)
        returns a list of those tournaments
        """
        teams_history: list[str] = []
        team_uuid: str = self.get_team_by_name(team_name).uuid

        model_tournaments: list[Tournament] = DataLayerAPI.load_tournaments()
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
        team_uuid: str = self.get_team_by_name(team_name).uuid
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
        team_uuid: str = self.get_team_by_name(team_name).uuid
        points = 0

        for tournament in model_tournaments:
            try:
                matches_list: list[Match] = self._match_logic.get_matches(tournament.uuid)
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
    
    # Changed by Sindri
    def get_team_club(self, team_name: str) -> str:
        clubs = self._club_logic.list_all_clubs()

        for club in clubs:
            teams_in_club: list[str] = [t.name for t in self._club_logic.get_teams_in_club(club.name)]

            if team_name in teams_in_club:
                return club.name
        
        return ""

# Fra utility
    
    def get_team_by_name(self, name: str) -> Team:
        teams: list[Team] = DataLayerAPI.load_teams()
        team: Team | None = next((t for t in teams if t.name == name), None)

        if team is None:
            raise Exception(f'No team found named: {name}')
        
        return team

    def get_team_by_uuid(self, uuid: str) -> Team:
        teams: list[Team] = DataLayerAPI.load_teams()
        team: Team | None = next((t for t in teams if t.uuid == uuid), None)

        if team is None:
            raise Exception(f'No team found with the UUID: {uuid}')
        
        return team
    
    def team_name_to_uuid(self, team_name: str) -> str:
        team = self.get_team_by_name(team_name)
        return team.uuid