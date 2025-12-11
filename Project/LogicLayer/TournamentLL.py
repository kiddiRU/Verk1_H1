'''
Author: Kristjan Hagalin <kristjanhj24@ru.is>
Date: 2025-12-05

Functions for tournament logic.
'''

from Models import Team, Tournament, Server, Match, ValidationError
from DataLayer import DataLayerAPI
from uuid import uuid4
from datetime import date, time, timedelta, datetime
from LogicLayer import MatchLL, TeamLL
import random

class TournamentLL:
    def __init__(self, team_logic: TeamLL, match_logic: MatchLL):
        self._team_logic = team_logic
        self._match_logic = match_logic
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
        tournament: Tournament = self.get_tournament_by_name(tournament_name)
        team: Team = self._team_logic.get_team_by_name(team_name)
        
        if team.uuid in tournament.teams_playing:
            raise Exception(f'The team \'{team_name}\' is already in the tournament \'{tournament_name}\'!')
        
        tournament.teams_playing.append(team.uuid)
        DataLayerAPI.update_tournament(tournament.uuid, tournament)

    def remove_team(self, tournament_name: str, team_name: str) -> None:
        '''
        Takes in a tournament and team name.

        Removes the teams UUID from the teams_playing list in the tournament.
        '''
        tournament: Tournament = self.get_tournament_by_name(tournament_name)
        team: Team = self._team_logic.get_team_by_name(team_name)
        
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
        
        #params: dict[str, str] = {k: v for k, v in locals().copy().items() if not k == 'self'}
        tournament: Tournament = self.get_tournament_by_name(name)

        # for attr, value in params.items():
        #     if value == '':
        #         continue
        
        #     setattr(tournament, attr, value)

        tournament.name = name
        tournament.venue = venue
        tournament.email = email
        tournament.phone_number = phone_number

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
        tournament: Tournament = self.get_tournament_by_name(name)

        if tournament.status == Tournament.StatusType.active:
            raise Exception('You can\'t change the time of an active tournament!')

        for attr, value in params.items():
            setattr(tournament, attr, value)

        DataLayerAPI.update_tournament(tournament.uuid, tournament)

    def list_tournaments(self) -> list[Tournament]:
        tournaments: list[Tournament] = DataLayerAPI.load_tournaments()
        return tournaments

    def uuid_to_tournament(self, uuid: str) -> Tournament:
        """Looks for a tournament with a specific uuid.

        :param uuid:
            The uuid of the tournament you want to get.

        :returns:
            The tournament object found.
        """
        
        # Loads all tournaments to look through.
        tournaments: list[Tournament] = DataLayerAPI.load_tournaments()

        # If a tournament in the list has the same uuid as the uuid given,
        # then it is returned.
        for item in tournaments:
            if item.uuid == uuid:
                return item
        
        # Otherwise I raise an error message to let know it wasn't found.
        else:
            raise ValidationError("Tournament with given uuid not found.")


    def end_tournament(self, uuid: str) -> None:
        """Ends an active tournament.

        Finds the tournament with the same uuid as the uuid given, sets
        it's status to archived and releases it's servers, the tournament
        has to be active to be able to end it.

        :param uuid:
            The uuid of the tournament to update.
        """
        
        tournament = self.uuid_to_tournament(uuid)

        # Checking to make sure the tournament is active.
        if tournament.status != Tournament.StatusType.active:
            raise ValidationError("Can't end tournaments that aren't active.")
        
        # Setting the tournaments status to archived.
        tournament.status = Tournament.StatusType.archived

        # Releasing all servers from the tournament.
        for idx, _ in enumerate(tournament.list_servers):
            tournament.list_servers[idx] = "NoServer"

        # Saves the changes made to the tournament.
        DataLayerAPI.update_tournament(uuid, tournament)


    def next_round(self, uuid: str) -> None:
        """Moves a tournament to the next round.

        Moves a tournament to the next round by removing all teams that lost
        in the current round and pairing the rest of the teams into matches.
        This is also used to matchmake the first round, if the tournament
        just finished the last round it will end the tournament.

        :param uuid:
            The uuid of the tournament that will move to the next round.
        """

        tournament = self.uuid_to_tournament(uuid)

        # Gets all matches tied to the tournament, this list is
        # in sorted order according to match date and time.
        matches: list[Match] = self._match_logic.get_matches(tournament.uuid)

        if len(matches) == 0:
            raise ValidationError("No matches tied to tournament.")
        
        # Finds all teams competing in the tournament which havent lost already.
        # These are the teams which will be competing in the next round.
        competing_teams: list[str] = []
        
        # For each team it will loop through each match, if it doesn't find a
        # match where the team lost then it's a competing team, otherwise it
        # isn't.
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

        # If there is only one team left then the tournament is over.
        if len(competing_teams) == 1:
            self.end_tournament(uuid)
            return None

        # Shuffles the teams randomly for matchmaking.
        random.shuffle(competing_teams)
        
        # Gets the list of matches which can be used for the next round.
        matches = [match for match in matches if match.winner == None]
    
        # Loops through the competing teams assigning teams next to eachother
        # to compete against eachother, in case of odd number of teams the
        # last team in the list will have a bye round.
        for i in range(1, len(competing_teams), 2):
            matches[i//2].team_1 = competing_teams[i-1]
            matches[i//2].team_2 = competing_teams[i]
            DataLayerAPI.update_match(matches[i//2].uuid, matches[i//2])


    def publish(self, name: str) -> None:
        """Publish an inactive tournament.

        Call to publish an inactive tournament, this will...
        
        -   Create a match schedule according to tournament time and date.
        -   Assign teams to the first round of matches.
        -   Create servers to host the matches.
        -   Assign the first matches to servers.

        :param tournament_name:
            Publishes the tournament with the given name.
        """
        uuid = self.tournament_name_to_uuid(name)

        tournament = self.uuid_to_tournament(uuid) 

        if tournament.status != Tournament.StatusType.inactive:
            raise ValidationError("Tournament isn't inactive.")

        # Changes status from inactive to active
        tournament.status = Tournament.StatusType.active

        # Calculates how many matches are needed for each round
        # by simulating each round and counting how many matches
        # are held each round.
        number_of_players: int = len(tournament.teams_playing)
        matches_per_round: list[int] = []

        while 1 < number_of_players:
            matches_per_round.append(number_of_players // 2)
            number_of_players -= matches_per_round[-1]


        # Calculates which timeslots should be used for matches in the
        # tournament. Every match in a certain round should have finished
        # before starting matches in the next round. Time slots for matches
        # should respect the tournament time frame.
        times_used: list[datetime] = []
        one_day: timedelta = timedelta(days=1)
        one_hour: timedelta = timedelta(hours=1)
        current_datetime: datetime = datetime.combine(
                date = tournament.start_date,
                time = tournament.time_frame_start
        )

        for rounds in matches_per_round:
            while 0 < rounds:
                # If the amount of matches left in a round is less then the
                # amount of servers then I only have to create that many
                # matches to finish the round, otherwise I can only create
                # amount of matches equal to the amount servers in a single
                # time slot.
                to_use: int = min(rounds, len(tournament.list_servers))
                for _ in range(to_use):
                    times_used.append(current_datetime)

                rounds -= to_use
                
                # Here I find the next time slot to use.
                current_datetime += one_hour
                # If the current time is equal to the end of the tournaments
                # time frame I have to jump to the next day/timeframe
                if current_datetime.time() == tournament.time_frame_end:
                    # Only if the start of the time frame is less than the end
                    # of the time frame do I have to add a day, this allows
                    # for tournaments to be able to run past midnight.
                    if tournament.time_frame_start < tournament.time_frame_end:
                        current_datetime += one_day
                    
                    current_datetime = datetime.combine(
                            date = current_datetime.date(),
                            time = tournament.time_frame_start
                    )

        # Raises an error if no time slots are created or the last time slots
        # runs past the runtime of the tournament.
        if len(times_used) == 0:
            raise ValidationError("No available time slots to use.")

        if times_used[-1] >= datetime.combine(
                date = tournament.end_date,
                time = tournament.time_frame_end
            ):
            raise ValidationError("Too little time for tournament")

        # Creates the matches needed, teams will not be filled in until
        # next_round is called.
        for match_datetime in times_used:
            self._match_logic.create_match(
                    tournament_id = uuid,
                    date = match_datetime.date(),
                    time = match_datetime.time(),
                    team_1 = "To be revealed",
                    team_2 = "To be revealed"
            )

        matches = self._match_logic.get_matches(tournament.uuid)

        # Creates servers for the tournament, adds the first matches into the
        # tournament.
        for idx, _ in enumerate(tournament.list_servers):
            new_server = Server(str(uuid4()), matches[idx].uuid)
            tournament.list_servers[idx] = new_server.uuid
            DataLayerAPI.store_server(new_server)

        # Stores the newly updated tournament.
        DataLayerAPI.update_tournament(tournament.uuid, tournament)

        # Starts the first round.
        self.next_round(uuid)


    def next_games(self, uuid: str) -> list[Match]:
        """Gets the matches next on the schedule in a certain tournament.

        Gets a list of matches which are next on the schedule in a certain
        tournament, a match is next on the schedule if it needs a winner and
        no other match which needs a winner is before it on the schedule.

        :param tournament_uuid:
            The tournament to get the matches will have the same uuid as
            tournament_uuid

        :returns:
            The list of matches next on the schedule.
        """
       
        tournament = self.uuid_to_tournament(uuid)
       
        if tournament.status != Tournament.StatusType.active:
            raise ValidationError("Tournament isn't active.")
    
        # Get's all matches tied to the tournament.
        matches = self._match_logic.get_matches(uuid)
    
        # Ignores all matches which have a winner.
        matches = [match for match in matches if match.winner == None]

        # Ignores all matches which happen after the first match without
        # a winner.
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
        """Updates match winner of a specific match in a specific tournament.

        Given the uuid of a specific tournament and the uuid of a specific match,
        will update the winner of this match, will set a new match into the server
        used if needed, will move onto next round of tournament if needed and will
        archive tournament if needed.

        :param tournament_uuid:
            The uuid of the tournament which the match belongs to.

        :param match_uuid:
            The uuid of the match you want to update.

        :param team_uuid:
            The uuid of the winner.
        """
        
        tournament = self.uuid_to_tournament(tournament_uuid)

        # Updates the match.
        self._match_logic.change_match_winner(match_uuid, team_uuid)
        
        matches: list[Match] = self._match_logic.get_matches(tournament_uuid)

        # Finds the updated match in matches list
        i: int = 0
        while i < len(matches):
            if matches[i].uuid == match_uuid:
                break
            i+=1
        else:
            raise ValidationError("Match with given uuid not found.")

        # Assigns a new match to the server that was in used if needed.
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

        # Checks if the finished match results in a new round
        if i == len(matches) - 1 or matches[i+1].team_1 == "To be revealed":
            self.next_round(tournament_uuid)


    def get_teams_from_tournament_name(self, tournament_name:str) -> list[Team]:
        """
        Takes in a tournament name

        Returns a list of Team objects
        """
        model_tournaments: list[Tournament] = DataLayerAPI.load_tournaments()
        teams_list: list[Team] = []

        for tournament in model_tournaments:
            if tournament_name == tournament.name:
                teams = tournament.teams_playing
                for team_uuid in teams:
                    teams_list.append(self._team_logic.get_team_by_uuid(team_uuid))

        return teams_list
    
    
    def to_time(self, value: str) -> time:
        # Split into parts
        parts = value.split(":")

        # Fill missing values with "00"
        while len(parts) < 3:
            parts.append("00")

        hour, minute, second = parts

        return time(
            hour=int(hour),
            minute=int(minute),
            second=int(second)
        )

    def to_date(self, value: str) -> date:
        return datetime.strptime(value, "%Y-%m-%d").date()

# Fra utility

    def get_tournament_by_name(self, name: str) -> Tournament:
            tournaments: list[Tournament] = DataLayerAPI.load_tournaments()
            tournament: Tournament | None = next((t for t in tournaments if t.name == name), None)

            if tournament is None:
                raise Exception(f'No tournament found named: {name}')
            
            return tournament


    def tournament_name_to_uuid(self, name: str) -> str:
            tournament = self.get_tournament_by_name(name)
            return tournament.uuid
