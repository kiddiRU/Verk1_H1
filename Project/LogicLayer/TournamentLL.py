'''
Author: Kristjan Hagalin <kristjanhj24@ru.is>
Date: 2025-12-05

Functions for tournament logic.
'''

from Models import Team, Tournament, Server, Match, ValidationError
from DataLayer import DataLayerAPI
from uuid import uuid4
from datetime import date, time, timedelta, datetime
from LogicLayer.MatchLL import MatchLL
from LogicLayer import LogicUtility
import random

class TournamentLL:
    def __init__(self):
        self.MatchAPI = MatchLL()
        pass

    def create_tournament(self,
        name: str,
        start_date: date,
        end_date: date,
        time_frame_start: time,
        time_frame_end: time, 
        venue: str,
        email: str,
        phone_number: str,
        server_amount: int
    ) -> None:
        '''
        Takes in tournament info.

        Creates a new Tournaments object and sends it to the data
        layer to be stored. Performs no validation on the given info.
        '''
        uuid = str(uuid4())
        new_tournament = Tournament(
            uuid,
            name,
            start_date,
            end_date,
            venue,
            email,
            phone_number,
            time_frame_start,
            time_frame_end,
            number_of_servers = server_amount
        )

        DataLayerAPI.store_tournament(new_tournament)

    def add_team(self, tournament_name: str, team_name: str) -> None:
        '''
        Takes in a tournament and team name.

        Adds the teams UUID to the teams_playing list in the tournament.
        '''
        tournament: Tournament = LogicUtility.get_tournament_by_name(tournament_name)
        team: Team = LogicUtility.get_team_by_name(team_name)
        
        if team.uuid in tournament.teams_playing:
            raise Exception(f'The team \'{team_name}\' is already in the tournament \'{tournament_name}\'!')
        
        tournament.teams_playing.append(team.uuid)
        DataLayerAPI.update_tournament(tournament.uuid, tournament)

    def remove_team(self, tournament_name: str, team_name: str) -> None:
        '''
        Takes in a tournament and team name.

        Removes the teams UUID from the teams_playing list in the tournament.
        '''
        tournament: Tournament = LogicUtility.get_tournament_by_name(tournament_name)
        team: Team = LogicUtility.get_team_by_name(team_name)
        
        if team.uuid in tournament.teams_playing:
            tournament.teams_playing.remove(team.uuid)

        DataLayerAPI.update_tournament(tournament.uuid, tournament)

    def update_info(
        self,
        name: str,
        venue: str,
        email: str,
        phone_number: str
    ) -> None:
        '''
        Takes in a tournaments name, venue, email and phone number.

        Takes the given info and applies it a tournament. Performs
        no validation on the given info.
        '''
        params: dict[str, str] = {k: v for k, v in locals().copy().items() if not k == 'self'}
        tournament: Tournament = LogicUtility.get_tournament_by_name(name)

        for attr, value in params.items():
            if value == '':
                continue
        
            setattr(tournament, attr, value)

        DataLayerAPI.update_tournament(tournament.uuid, tournament)
    
    def update_tournament_datetime(
        self,
        name: str,
        start_date: date,
        end_date: date,
        time_frame_start: time,
        time_frame_end: time
    ) -> None:
        '''
        Takes in a start date, end date, time frame start, and a time frame end.

        Takes the given info and applies it a tournament. Performs no validation
        on the given info.
        '''
        params: dict[str, str] = {k: v for k, v in locals().copy().items() if not k == 'self'}
        tournament: Tournament = LogicUtility.get_tournament_by_name(name)

        if tournament.status == Tournament.StatusType.active:
            raise Exception('You can\'t change the time of an active tournament!')

        for attr, value in params.items():
            setattr(tournament, attr, value)

        DataLayerAPI.update_tournament(tournament.uuid, tournament)

    def list_tournaments(self) -> list[Tournament]:
        tournaments: list[Tournament] = DataLayerAPI.load_tournaments()
        return tournaments

    def end_tournament(self, uuid: str) -> None:
        """
        Parameters: uuid of tournament

        Archives the tournament tied to the given uuid and releases
        it's servers.
        """
        # Looks for the tournament with the given uuid.
        tournaments: list[Tournament] = DataLayerAPI.load_tournaments()
        for item in tournaments:
            if item.uuid == uuid:
                tournament: Tournament = item
                break
        else:
            raise ValidationError("Tournament with given uuid not found.")
        
        tournament.status = Tournament.StatusType.archived


    def next_round(self, uuid: str) -> None:
        """
        Parameters: uuid of tournament which will proceed to next round

        This can be called when all matches of current round have a winner
        and will fill future matches with a teams competing.
        """

        # Looks for the tournament with the given uuid.
        tournaments: list[Tournament] = DataLayerAPI.load_tournaments()
        for item in tournaments:
            if item.uuid == uuid:
                tournament: Tournament = item
                break
        else:
            raise ValidationError("Tournament with given uuid not found.")

        # Gets all matches tied to the tournament.
        matches: list[Match] = self.MatchAPI.get_matches(tournament.uuid)

        if len(matches) == 0:
            raise ValidationError("No matches tied to tournament.")
        
        # Finds all teams competing in the tournament which havent lost already.
        # These are the teams which will be competing in the next round.
        competing_teams: list[str] = []
        for team in tournament.teams_playing:
            for match in matches:
                if match.winner == None: continue
                if team == match.team_1 or team == match.team_2:
                    if team != match.winner:
                        break
            else:
                competing_teams.append(team)

        if len(competing_teams) == 0:
            raise ValidationError("No teams found to compete.")

        if len(competing_teams) == 1:
            self.end_tournament(uuid)
            return None

        # Shuffles the teams randomly for matchmaking.
        random.shuffle(competing_teams)
        
        # Gets the list of available matches, matches which haven't
        # been assigned a winner.
        matches = [match for match in matches if match.winner == None]
    
        # Loops through the competing teams assigning teams next to eachother
        # to compete against eachother, in case of odd number of teams the
        # last team in the list will have a bye round.
        for i in range(1, len(competing_teams), 2):
            matches[i//2].team_1 = competing_teams[i-1]
            matches[i//2].team_2 = competing_teams[i]
            DataLayerAPI.update_match(matches[i//2].uuid, matches[i//2])


    def publish(self, name: str) -> None:
        """
        Parameters: uuid of tournament to publish

        Can be called to publish an inactive tournament, this will
        create a schedule, create the matches for in the schedule
        and assign the teams to compete in the first round.
        """
        uuid = LogicUtility.tournament_name_to_uuid(name)

        # Gets the tournament with the given uuid.
        tournaments: list[Tournament] = DataLayerAPI.load_tournaments()

        for item in tournaments:
            if item.uuid == uuid:
                tournament: Tournament = item
                break
        else:
            raise ValidationError("Tournament tied to uuid not found.") 

        if tournament.status != Tournament.StatusType.inactive:
            raise ValidationError("Tournament isn't inactive.")

        # Changes status from inactive to active
        tournament.status = Tournament.StatusType.active

        # Creates servers for the tournament.
        for idx, _ in enumerate(tournament.list_servers):
            new_server = Server(str(uuid4()), "NoMatch")
            tournament.list_servers[idx] = new_server.uuid
            DataLayerAPI.store_server(new_server)

        # Calculates how many matches are needed for each round.
        number_of_players: int = len(tournament.teams_playing)
        matches_per_round: list[int] = []

        while 1 < number_of_players:
            matches_per_round.append(number_of_players // 2)
            number_of_players -= matches_per_round[-1]

        # Calculates which times should be used for matches in the tournament.
        # Every match in a certain round should have finished before starting
        # matches in the next round.
        # Time slots for matches should respect the tournament time frame.
        times_used: list[datetime] = []
        one_day: timedelta = timedelta(days=1)
        one_hour: timedelta = timedelta(hours=1)
        current_datetime: datetime = datetime.combine(
                date = tournament.start_date,
                time = tournament.time_frame_start
        )

        for rounds in matches_per_round:
            while 0 < rounds:
                to_use: int = min(rounds, len(tournament.list_servers))
                for _ in range(to_use):
                    times_used.append(current_datetime)

                rounds -= to_use

                current_datetime += one_hour
                if current_datetime.time() >= tournament.time_frame_end:
                    if tournament.time_frame_start < tournament.time_frame_end:
                        current_datetime += one_day
                    
                    current_datetime = datetime.combine(
                            date = current_datetime.date(),
                            time = tournament.time_frame_start
                    )

        if times_used[-1] >= datetime.combine(
                date = tournament.end_date,
                time = tournament.time_frame_end
            ):
            raise ValidationError("Too little time for tournament")

        # Creates the matches needed.
        for match_datetime in times_used:
            self.MatchAPI.create_match(
                    tournament_id = uuid,
                    date = match_datetime.date(),
                    time = match_datetime.time(),
                    team_1 = "To be revealed",
                    team_2 = "To be revealed"
            )
    
        # Starts the first round.
        self.next_round(uuid)

        # Stores the newly updated tournament.
        DataLayerAPI.update_tournament(tournament.uuid, tournament)

    def next_games(self, uuid: str) -> list[Match]:
        """
        Parameters: uuid of tournament

        Returns a list of matches which are next on the schedule,
        matches next in the schedule are matches which don't have
        a winner and there doesn't exist a match which happens
        before it and needs a winner.
        """
        
        # Finds the tournament with a given uuid.
        tournaments: list[Tournament] = DataLayerAPI.load_tournaments()

        for item in tournaments:
            if item.uuid == uuid:
                tournament: Tournament = item
                break
        else:
            raise ValidationError("Tournament with given uuid not found.")
       
        if tournament.status != Tournament.StatusType.active:
            raise ValidationError("Tournament isn't active.")
    
        # Get's all matches tied to the tournament.
        matches = self.MatchAPI.get_matches(uuid)
    
        # Ignores all matches which have a winner.
        matches = [match for match in matches if match.winner == None]
        # Ignores all matches which happen after
        # the first match without a winner.
        matches = [
                match for match in matches
                if match.match_date == matches[0].match_date and
                   match.match_time == matches[0].match_time
        ]

        return matches
    
    def change_match_winner(
            self,
            tournament_uuid: str,
            match_uuid: str,
            team_uuid: str
        ) -> None:
        """
        Parameters:
            tournament_uuid, uuid of tournament the match belongs to.
            match_uuid, uuid of match you want to update.
            team_uuid, uuid of the team which won.

        Updates the match to set a winner, will continue to next round
        and update servers in use of the tournament if needed.
        """
        # Finds the tournament with a given uuid.
        tournaments: list[Tournament] = DataLayerAPI.load_tournaments()

        for item in tournaments:
            if item.uuid == tournament_uuid:
                tournament: Tournament = item
                break
        else:
            raise ValidationError("Tournament with given uuid not found.")

        # Updates match itself
        self.MatchAPI.change_match_winner(match_uuid, team_uuid)
        
        matches: list[Match] = self.MatchAPI.get_matches(tournament_uuid)

        # Finds the updated match in matches list
        i: int = 0
        while i < len(matches):
            if matches[i].uuid == match_uuid:
                break
            i+=1
        else:
            raise ValidationError("Match with given uuid not found.")

        # Checks if the finished match results in a new round
        if i == len(matches) - 1 or matches[i+1].team_1 == "To be revealed":
            self.next_round(tournament_uuid)

        # Assign a new match to the server that was in use if needed.
        j: int = i + len(tournament.list_servers)
        servers: list[Server] = DataLayerAPI.load_servers()
        for server in servers:
            if server.match_in_server == match_uuid:
                if j < len(matches):
                    server.match_in_server = matches[j].uuid
                else:
                    server.match_in_server = "NoMatch"
                DataLayerAPI.update_server(server.uuid, server)
                break
        else:
            raise ValidationError("Tournament server error.")
