'''
Author: Kristjan Hagalin <kristjanhj24@ru.is>
Date: 2025-12-05

Functions for tournament logic.
'''

import random
from uuid import uuid4
from datetime import date, time, timedelta, datetime
from Models import Team, Tournament, Server, Match, ValidationError
from DataLayer import DataLayerAPI
from LogicLayer import MatchLL, TeamLL

class TournamentLL:
    ''' Tournamnet logic. '''

    def __init__(self, team_logic: TeamLL, match_logic: MatchLL):
        self._team_logic = team_logic
        self._match_logic = match_logic

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
        Creates a new Tournament object and sends it to be stored.
        
        :param name:
            The tournaments name.
        :type name: str

        :param start_date:
            The tournamnets starting date.
        :type start_date: date

        :param end_date:
            The tournaments ending date.
        :type end_date: date

        :param time_frame_start:
            The start of the tournaments time frame.
        :type time_frame_start: time

        :param time_frame_end:
            The end of the tournaments time frame.
        :type time_frame_end: time

        :param venue:
            The tournaments venue.
        :type venue: str

        :param email:
            The tournaments contact email.
        :type email: str

        :param phone_number:
            The tournaments contact phone number.
        :type phone_number: str

        :param amount_of_servers:
            The tournaments amount of servers.
        :type amount_of_servers: int
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
        Adds a team to the list of teams playing in a tournament.
        
        :param tournament_name:
            The name of the tournament.
        :type tournament_name: str

        :param team_name:
            The name of the team to add.
        :type team_name: str
        '''
        tournament: Tournament = self.get_tournament_by_name(tournament_name)
        team: Team = self._team_logic.get_team_by_name(team_name)

        if team.uuid in tournament.teams_playing:
            raise ValidationError(
                f'The team \'{team_name}\' is already in the tournament \'{tournament_name}\'!'
            )

        tournament.teams_playing.append(team.uuid)
        DataLayerAPI.update_tournament(tournament.uuid, tournament)

    def remove_team(self, tournament_name: str, team_name: str) -> None:
        '''
        Removes a team from the list of teams playing in a tournament.
        
        :param tournament_name:
            The name of the tournament.
        :type tournament_name: str

        :param team_name:
            The name of the team to remove.
        :type team_name: str
        '''
        tournament: Tournament = self.get_tournament_by_name(tournament_name)
        team: Team = self._team_logic.get_team_by_name(team_name)

        if team.uuid in tournament.teams_playing:
            tournament.teams_playing.remove(team.uuid)

        DataLayerAPI.update_tournament(tournament.uuid, tournament)

    # Isn't used, remove?
    # def update_info(
    #     self,
    #     name: str,
    #     venue: str,
    #     email: str,
    #     phone_number: str
    # ) -> None:
    #     '''
    #     Takes in a tournaments name, venue, email and phone number.

    #     Takes the given info and applies it a tournament. Performs
    #     no validation on the given info.
    #     '''
    #     tournament: Tournament = self.get_tournament_by_name(name)

    #     tournament.name = name
    #     tournament.venue = venue
    #     tournament.email = email
    #     tournament.phone_number = phone_number

    #     DataLayerAPI.update_tournament(tournament.uuid, tournament)

    # Isn't used, remove?
    # def update_tournament_datetime(
    #     self,
    #     name: str,
    #     start_date: date,
    #     end_date: date,
    #     time_frame_start: time,
    #     time_frame_end: time
    # ) -> None:
    #     '''
    #     Takes in a start date, end date, time frame start, and a time frame end.

    #     Takes the given info and applies it a tournament. Performs no validation
    #     on the given info.
    #     '''
    #     tournament: Tournament = self.get_tournament_by_name(name)

    #     if tournament.status == Tournament.StatusType.active:
    #         raise ValidationError('You can\'t change the time of an active tournament!')

    #     tournament.start_date = start_date
    #     tournament.end_date = end_date
    #     tournament.time_frame_start = time_frame_start
    #     tournament.time_frame_end = time_frame_end

    #     DataLayerAPI.update_tournament(tournament.uuid, tournament)

    def list_tournaments(self) -> list[Tournament]:
        '''
        Gets a list of all stored tournamnets.
        
        :return:
            A list of all Tournament objects.
        :rtype: list[Tournament]
        '''
        tournaments: list[Tournament] = DataLayerAPI.load_tournaments()
        return tournaments

    def end_tournament(self, uuid: str) -> None:
        """Ends an active tournament.

        Finds the tournament with the same uuid as the uuid given, sets
        it's status to archived and releases it's servers, the tournament
        has to be active to be able to end it.

        :param uuid:
            The uuid of the tournament to update.
        """

        tournament = self.get_tournament_by_uuid(uuid)

        # Checking to make sure the tournament is active.
        if tournament.status != Tournament.StatusType.active:
            raise ValidationError("Can't end tournaments that aren't active.")

        # Setting the tournaments status to archived.
        tournament.status = Tournament.StatusType.archived
        for idx, _ in enumerate(tournament.list_servers):
            tournament.list_servers[idx] = "NoServer"

        DataLayerAPI.update_tournament(uuid, tournament)


    def next_round(self, uuid: str) -> None:
        """
        Parameters: uuid of tournament which will proceed to next round

        This can be called when all matches of current round have a winner
        and will fill future matches with a teams competing.
        """

        tournament = self.get_tournament_by_uuid(uuid)

        # Gets all matches tied to the tournament.
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

        #print("debug", competing_teams)
        #input()

        if len(competing_teams) == 0:
            raise ValidationError("No teams found to compete.")

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

        tournament = self.get_tournament_by_uuid(uuid)
        if tournament.status != Tournament.StatusType.inactive:
            raise ValidationError("Tournament isn't inactive.")

        # Changes status from inactive to active
        tournament.status = Tournament.StatusType.active

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

                # Here I find the next time slot to use.
                current_datetime += one_hour
                if current_datetime.time() >= tournament.time_frame_end:
                    if tournament.time_frame_start < tournament.time_frame_end:
                        current_datetime += one_day

                    current_datetime = datetime.combine(
                            date = current_datetime.date(),
                            time = tournament.time_frame_start
                    )

        if len(times_used) == 0:
            raise ValidationError("No available time slots to use.")

        if times_used[-1] >= datetime.combine(
                date = tournament.end_date,
                time = tournament.time_frame_end
            ):
            raise ValidationError("Too little time for tournament")

        # Creates the matches needed.
        for match_datetime in times_used:
            self._match_logic.create_match(
                    tournament_id = uuid,
                    date = match_datetime.date(),
                    time = match_datetime.time(),
                    team_1 = "To be revealed",
                    team_2 = "To be revealed"
            )

        matches = self._match_logic.get_matches(tournament.uuid)

        # Creates servers for the tournament.
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
        :rtype: list[Match]
        """
        tournament = self.get_tournament_by_uuid(uuid)

        if tournament.status != Tournament.StatusType.active:
            raise ValidationError("Tournament isn't active.")

        # Get's all matches tied to the tournament.
        matches = self._match_logic.get_matches(uuid)

        # Ignores all matches which have a winner.
        matches = [match for match in matches if match.winner is None]

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

        tournament = self.get_tournament_by_uuid(tournament_uuid)


        # Updates match itself
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
        '''
        Gets a Tournament object by its name.
        
        :param tournament_name:
            The name of the tournament to fetch.
        :type tournament_name: str

        :return:
            The object of the tournament with the given name.
        :rtype: Tournament
        '''
        tournaments: list[Tournament] = DataLayerAPI.load_tournaments()
        tournament: Tournament | None = next((t for t in tournaments if t.name == name), None)

        if tournament is None:
            raise ValidationError(f'No tournament found named: {name}')

        return tournament

    def get_tournament_by_uuid(self, uuid: str) -> Tournament:
        '''
        Gets a Tournament object by its UUID.
        
        :param tournament_uuid:
            The UUID of the tournament to fetch.
        :type tournament_uuid: str

        :return:
            The object of the tournament with the given UUID.
        :rtype: Tournament
        '''
        tournaments: list[Tournament] = DataLayerAPI.load_tournaments()
        tournament: Tournament | None = next((t for t in tournaments if t.uuid == uuid), None)

        if tournament is None:
            raise ValidationError(f'No tournament found with the UUID: {uuid}')

        return tournament

    def tournament_name_to_uuid(self, name: str) -> str:
        '''
        Converts a tournaments name, to its UUID.
        
        :param tournament_name:
            The name of the tournament.
        :type tournament_name: str

        :return:
            Returns the UUID of the tournament with the given name.
        :rtype: str
        '''
        tournament = self.get_tournament_by_name(name)
        return tournament.uuid
