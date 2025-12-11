"""
Author: Elmar Sigmarsson <elmars25@ru.is>
Date: 2025-12-03

Created the TeamLL class and added the functions
"""

from uuid import uuid4
from DataLayer import DataLayerAPI
from Models import Team, Player, Tournament, Match, Club, ValidationError
from LogicLayer import MatchLL, ClubLL, PlayerLL, Validation

class TeamLL():
    ''' Team logic. '''
    
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
            raise ValidationError('You can\'t create a team when you\'re already in one!')

        Validation.validate_attr('handle', name, 'TEAM')
        uuid = str(uuid4())

        clubs: list[Club] = DataLayerAPI.load_clubs()
        club_uuid = next(
            (c.uuid for c in clubs if c.name == club_name),
            'b66ba594-d6a5-4af0-ac3b-f0cc94ca61fa'
        )

        new_team = Team(
            uuid, name, [team_captain.uuid], team_captain.uuid, club_uuid, None, url, ascii_art
        )

        DataLayerAPI.store_team(new_team)
        return new_team

    def add_player(self, player_handle: str, current_player: Player) -> Team | str:
        """Gets the handle of the player to add and
        the player object of the captain

        First checks if the player is already in a team
        Then finds the team of the captain and
        adds the player to the team        
        
        :param player_handle:
            The player handle of the player to add to the team
        :type player_handle: str

        :param current_player:
            current player is the team captain and
            is used to get the uuid of the team
        :type current_player: Player

        :return:
            Returns the team object
        :rtype: Team
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
        """Gets the handle of the player to add and
        the player object of the captain

        Looks through all teams to find the team of the captain
        First checks that the player to remove is not the captain
        Otherwise it removes the player from the team
        if the player is not found and error message will be raised 
        
        :param player_handle:
            the player handle of the player to remove from the team
        :type player_handle: str

        :param current_player
            the player object of the team captain and
            is used to get the uuid of the team
        :type current_player: Player

        :return: Returns the team object
        :rtype: Team
        """
        player_uuid: str = self._player_logic.player_handle_to_uuid(player_handle)
        team_uuid: str = self._player_logic.get_players_team_uuid(current_player.uuid)
        model_teams: list[Team] = DataLayerAPI.load_teams()

        for team in model_teams:
            if team.uuid == team_uuid:
                try:
                    team.list_player_uuid.remove(player_uuid)
                    DataLayerAPI.update_team(team_uuid, team)
                    return team

                except ValueError:
                    raise ValidationError("Player not in team")

        raise ValidationError("Team not found")


    def get_team_members(self, team_name: str) -> list[str]:
        """Gets the name of the team

        Looks through all teams to find the correct team object
        and extracts the list of player uuid in the team
        
        :param team_name:
            The team name is used to find the team object
        :type team_name: str

        :return: Returns a list of the team members uuid's
        :rtype: list[str]
        """    
        model_teams: list[Team] = DataLayerAPI.load_teams()
        for team in model_teams:
            if team.name == team_name:
                return team.list_player_uuid 

        raise ValidationError("Team not found")


    def list_all_teams(self) -> list[Team]: 
        """Is called to get a list of all teams
        
        :return: Returns a list of all team objects
        :rtype: list[Team]
        """

        teams: list[Team] = DataLayerAPI.load_teams()
        return teams

    def get_team_members_object(self, team_name: str) -> list[Player]:
        """Gets the team name

        First gets the uuid of the players in the team,
        Then loads all player objects and
        lists all players objects that have the
        uuid of the players in the team
        
        :param team_name:
            The team name of the team to get the player objects
        :type team_name: str

        :return: Returns a list of all player objects in a team
        :rtype: list[Player]
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
        """Gets the team name

        First gets the team uuid, Then loads all Tournaments
        and lists all tournaments that the teams uuid is in
        teams playing 

        :param team_name:
            The team name to find the tournaments they participated in
        :type team_name: str

        :return:
        Returns a list of tournament names that the team has participated in
        :rtype: list[str]
        """
        teams_history: list[str] = []
        team_uuid: str = self.get_team_by_name(team_name).uuid

        model_tournaments: list[Tournament] = DataLayerAPI.load_tournaments()
        for tournament in model_tournaments:
            if team_uuid in tournament.teams_playing: 
                teams_history.append(tournament.name)

        return teams_history

    def get_team_wins(self, team_name: str) -> str:
        """Gets the team name

        First gets the uuid of the team,
        Then Loads all matches and adds one to the count 
        when the winner uuid matches the teams uuid
        
        :param team_name:
            The team name of the team to find the total of won matches
        :type team_name: str

        :return: Returns a string number of the total won matches
        :rtype: str
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
        """Gets the team name
        
        First gets the teams uuid,
        Then loads all tournaments and get a list of all matches
        with the tournament uuid,
        Finds the last match of the tournament (Finals) and finds the
        winning and losing team of the match, and if the team is the
        winner they get 3 points and if the loser gets 1 point
        
        :param team_name:
            The team name of the team to find the total points from tournaments
        :type team_name: str

        :return: Returns a string number of total points from tournaments
        :rtype: str
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

            except ValidationError:
                pass

        return str(points)

    # Changed by Sindri
    def get_team_club(self, team_name: str) -> str:
        """Gets the team name

        First loads all clubs, and gets a list of all team names in the club
        and if the team name is in the list it is their club
        
        :param team_name:
            The team name to get the club name from
        :type team_name: str
        
        :return: Returns the name of the club that the team is in
        :rtype: str
        """
        clubs = self._club_logic.list_all_clubs()

        for club in clubs:
            teams_in_club: list[str] = [
                t.name for t in self._club_logic.get_teams_in_club(club.name)
            ]

            if team_name in teams_in_club:
                return club.name

        return ""

# Fra utility

    def get_team_by_name(self, name: str) -> Team:
        teams: list[Team] = DataLayerAPI.load_teams()
        team: Team | None = next((t for t in teams if t.name == name), None)

        if team is None:
            raise ValidationError(f'No team found named: {name}')

        return team

    def get_team_by_uuid(self, uuid: str) -> Team:
        teams: list[Team] = DataLayerAPI.load_teams()
        team: Team | None = next((t for t in teams if t.uuid == uuid), None)

        if team is None:
            raise ValidationError(f'No team found with the UUID: {uuid}')

        return team

    def team_name_to_uuid(self, team_name: str) -> str:
        team = self.get_team_by_name(team_name)
        return team.uuid
