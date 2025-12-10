"""
Authors: Elmar Sigmarsson <elmars25@ru.is>
Date: 2025-12-03

Co: Kristjan Hagalin <kristjanhj24@ru.is>

Functions for player logic.
"""

# TODO add nessecery imports
from uuid import uuid4
from DataLayer import DataLayerAPI
from Models import Player, Team, Club, Match, Tournament#, ValidationError
from LogicLayer.Validation import validate_attr
from LogicLayer.LogicUtility import get_player_uuid
from LogicLayer.MatchLL import MatchLL
from LogicLayer.TeamLL import TeamLL

class PlayerLL():
    def __init__(self) -> None:
        pass
    
    # TODO Alter validation functionality?
    def create_player(self,
        name: str,
        date_of_birth: str,
        home_address: str,
        email: str,
        phone_number: str,
        handle: str,
        url: str
    ) -> Player:

        """
        Takes in player info.

        Validates the given info and creates a player object. Sends the
        object to the data layer to be stored and returns the new player.
        """
        
        params: dict[str, str] = {k: v for k, v in locals().copy().items() if not k == 'self'}
        for attr, value in params.items():
            validate_attr(attr, value.strip(), name_type = 'PLAYER')

        uuid = str(uuid4())

        new_player = Player(
            uuid,
            params["name"],
            params["date_of_birth"],
            params["home_address"],
            params["email"],
            params["phone_number"],
            params["handle"],
            params["url"],
        )

        DataLayerAPI.store_player(new_player)
        return new_player

    def update_player_info(
        self,
        player: Player,
        name: str,
        date_of_birth: str,
        home_address: str,
        email: str,
        phone_number: str,
        handle: str,
        url: str
    ) -> Player:

        '''
        Takes in a Player object and potential attribute updates.

        Sends updated values to the data layer, and returns and updated Player object.
        '''

        DataLayerAPI.update_player(player.uuid, player)
        return player

    def create_team(self, name: str, team_captain: Player, club_name: str, url: str, ascii_art: str) -> Team:
        '''
        Takes in the teams name, its captain, club, url and ascii art.

        Creates a new Team object, sends it the data layer to be stored and returns it.
        '''
        teams: list[Team] = DataLayerAPI.load_teams()
        players_in_teams: list[str] = [uuid for t in teams for uuid in t.list_player_uuid]

        if team_captain.uuid in players_in_teams:
            raise Exception('You can\'t create a team when you\'re already in one!')

        validate_attr('handle', name, 'TEAM')
        uuid = str(uuid4())

        clubs: list[Club] = DataLayerAPI.load_clubs()
        club_uuid = next((c.uuid for c in clubs if c.name == club_name), 'NO_CLUB_UUID') # UUID for no club is ..?
        
        new_team = Team(uuid, name, [team_captain.uuid], team_captain.uuid, club_uuid, None, url, ascii_art)

        DataLayerAPI.store_team(new_team)
        return new_team

    # TODO Remove Player objec
    def leave_team(self, team_name: str, player: Player) -> None:
        '''
        Takes in a teams UUID and a Player object.

        Removes the player from the team, raises an exception if the player
        is the captain of said team.
        '''

        teams: list[Team] = DataLayerAPI.load_teams()
        team = next((t for t in teams if t.name == team_name), None)

        if team is None:
            raise Exception('Team not found!')

        if team.team_captain_uuid == player.uuid:
            raise Exception('You must promote a new captain before leaving your team!')

        team.list_player_uuid.remove(player.uuid)
        DataLayerAPI.update_team(team.uuid, team)

    def list_players(self) -> list[Player]:
        """ Returns a list of stored players. """

        players: list[Player] = DataLayerAPI.load_players()
        return players

    def get_player_object(self, player_uuid: str) -> Player | str:
        ''' Takes in a players UUID and returns the players object. '''

        players: list[Player] = DataLayerAPI.load_players()
        player = next((p for p in players if p.uuid == player_uuid), None)

        if player is None:
            return ""

        return player
    
    def promote_captain(self, current_player: Player, handle_to_promote: str) -> None:
        team_to_edit = next((t for t in DataLayerAPI.load_teams() if current_player.uuid == t.team_captain_uuid), None)
        
        if team_to_edit is None:
            raise Exception('You are not a captain!')

        players: list[Player] = DataLayerAPI.load_players()
        player_to_promote: Player | None = next((p for p in players if p.handle == handle_to_promote), None)

        if player_to_promote is None:
            raise Exception(f'No player found with the handle: {handle_to_promote}')
        
        if player_to_promote.uuid not in team_to_edit.list_player_uuid:
            raise Exception(f'The player \'{handle_to_promote}\' exists, but is not in your team!')
        
        team_to_edit.team_captain_uuid = player_to_promote.uuid
        DataLayerAPI.update_team(team_to_edit.uuid, team_to_edit)

    def save_player(self, player_handle: str | None = None):
        """Takes in a player handle and saves them as the current active user"""
        if player_handle is not None:
            self.player = player_handle

        return self.player
    

    def get_player_team(self, player_handle) -> tuple:
        """Takes in a player handle and returns the name of their team and their rank"""
        teamll = TeamLL()

        player_uuid = get_player_uuid(player_handle)
        teams = teamll.list_teams()
        
        for team in teams:
            players = teamll.get_team_members(team.name)

            if player_uuid in players:
                if team.team_captain_uuid == player_uuid:
                    return team.name, "Captain"
                return team.name, "Player"
            
        return ("","") # This will never be returned (it is just to appease the type hinting gods)


    # TODO find a way to get a players wins and points
    # Problem if a player swaps team
    def get_player_wins(self, player_handle) -> str:
        """
        takes in a player handle and finds the player uuid
        loads and looks through all matches 
        and adds one to counter for every match that the player uuid
        is in the winning players
        returns the count        
        """
        model_matches: list[Match] = DataLayerAPI.load_matches()
        player_uuid: str = get_player_uuid(player_handle)
        win_count: int = 0

        for match in model_matches:
            if match.winning_players is None:
                pass
            
            elif player_uuid in match.winning_players:
                win_count += 1

        return str(win_count)
    

    def get_player_points(self, player_handle) -> str:
        """
        takes in a player handle and finds the player uuid from handle
        loads and looks through all tournament and takes there uuid
        looks through every match in tournament and checks the last match
        if the player uuid is in the winning players
        three points are added
        if the player uuid is in the losing players
        one point is added
        returns points
        """
        model_tournaments: list[Tournament] = DataLayerAPI.load_tournaments()
        player_uuid = get_player_uuid(player_handle)
        match = MatchLL()
        points = 0

        for tournament in model_tournaments:
            try:
                matches_list: list[Match] = match.get_matches(tournament.uuid)
                tour_final_match: Match = matches_list[-1]
                winning_players = tour_final_match.winning_players
                losing_player = tour_final_match.losing_players

                if winning_players is None:
                    pass

                elif player_uuid in winning_players:
                    points += 3

                elif player_uuid in losing_player:
                    points += 1
                
            except:
                pass

        return str(points)
