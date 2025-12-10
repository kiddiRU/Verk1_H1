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
        '''
        Takes in tournament info.

        Creates a new Tournaments object and sends it to the data
        layer to be stored. Performs no validation on the given info.
 {
    "f3a33b54-a8a9-4f07-9adc-197db99cb160": {
        "uuid": "f3a33b54-a8a9-4f07-9adc-197db99cb160",
        "tournament_id": "12ba73ac-8375-4489-9a21-baad9b507a70",
        "match_date": "2025-12-05",
        "match_time": "12:00:00",
        "team_1": "b26a8d5e-b571-41f8-a657-b5ad616299d2",
        "team_2": "7ffe196a-495e-4e77-b94d-ea6799c2e572",
        "winner": "b26a8d5e-b571-41f8-a657-b5ad616299d2",
        "winning_players": [
            "2cc090bc-2351-4c43-bb08-2f578d26154a",
            "35e63bfc-3349-4131-b197-c569d71d6b90",
            "7d45cca7-bbe1-47e9-9855-63ec8e01f4a3"
        ],
        "losing_team": "7ffe196a-495e-4e77-b94d-ea6799c2e572",
        "losing_players": [
            "e9ecf404-a192-48c5-9f61-99387bad32f8",
            "b2ee9a85-bb85-49d8-bb10-1eddf19a6509",
            "ae4cb519-d61b-486c-9835-c40ab8b2a4ff"
        ]
    },
    "5b413a5b-077e-4edc-850b-987680595cc6": {
        "uuid": "5b413a5b-077e-4edc-850b-987680595cc6",
        "tournament_id": "269675a5-b277-43a0-8449-cda8803190b7",
        "match_date": "2004-01-21",
        "match_time": "00:12:23",
        "team_1": "382f652f-efdf-4298-9d15-922877e5e1b5",
        "team_2": "b6f18db4-e778-4b72-84e6-91aed8125bb4",
        "winner": null,
        "winning_players": null,
        "losing_team": null,
        "losing_players": null
    },
    "1de6c60f-6fed-4e70-b1c5-d24c5ae98ae8": {
        "uuid": "1de6c60f-6fed-4e70-b1c5-d24c5ae98ae8",
        "tournament_id": "269675a5-b277-43a0-8449-cda8803190b7",
        "match_date": "2004-01-21",
        "match_time": "00:12:23",
        "team_1": "0e86df13-949f-497d-916d-6aee0e329516",
        "team_2": "name2",
        "winner": null,
        "winning_players": null,
        "losing_team": null,
        "losing_players": null
    },
    "6d618d2e-842c-4ed4-a588-aa85b577d548": {
        "uuid": "6d618d2e-842c-4ed4-a588-aa85b577d548",
        "tournament_id": "269675a5-b277-43a0-8449-cda8803190b7",
        "match_date": "2004-01-21",
        "match_time": "00:12:23",
        "team_1": "To be revealed",
        "team_2": "To be revealed",
        "winner": null,
        "winning_players": null,
        "losing_team": null,
        "losing_players": null
    },
    "a2c20787-7a4d-46dd-bef9-7e05081609c5": {
        "uuid": "a2c20787-7a4d-46dd-bef9-7e05081609c5",
        "tournament_id": "9f88c82f-7361-4680-9499-098c01ebfeca",
        "match_date": "2025-01-01",
        "match_time": "14:00:00",
        "team_1": "7ffed5fa-83c5-423e-a975-0f67b5782539",
        "team_2": "7ffe196a-495e-4e77-b94d-ea6799c2e572",
        "winner": null,
        "winning_players": null,
        "losing_team": null,
        "losing_players": null
    },
    "ead9bb2c-af25-4641-8165-e0ddb5fae06e": {
        "uuid": "ead9bb2c-af25-4641-8165-e0ddb5fae06e",
        "tournament_id": "9f88c82f-7361-4680-9499-098c01ebfeca",
        "match_date": "2025-01-02",
        "match_time": "14:00:00",
        "team_1": "To be revealed",
        "team_2": "To be revealed",
        "winner": null,
        "winning_players": null,
        "losing_team": null,
        "losing_players": null
    },
    "56e09b3f-0ce3-4a1e-b2c8-648722b24c90": {
        "uuid": "56e09b3f-0ce3-4a1e-b2c8-648722b24c90",
        "tournament_id": "269675a5-b277-43a0-8449-cda8803190b7",
        "match_date": "2004-01-21",
        "match_time": "00:12:23",
        "team_1": "To be revealed",
        "team_2": "To be revealed",
        "winner": null,
        "winning_players": null,
        "losing_team": null,
        "losing_players": null
    },
    "579d2740-6141-4409-95b3-a8fb0a195d9c": {
        "uuid": "579d2740-6141-4409-95b3-a8fb0a195d9c",
        "tournament_id": "269675a5-b277-43a0-8449-cda8803190b7",
        "match_date": "2004-01-21",
        "match_time": "00:12:23",
        "team_1": "To be revealed",
        "team_2": "To be revealed",
        "winner": null,
        "winning_players": null,
        "losing_team": null,
        "losing_players": null
    },
    "e179f9b8-c476-41b1-891b-fbd0ff464ba4": {
        "uuid": "e179f9b8-c476-41b1-891b-fbd0ff464ba4",
        "tournament_id": "33a78757-110e-4837-89de-065e504968ee",
        "match_date": "2006-05-05",
        "match_time": "14:00:00",
        "team_1": "8bf1dc91-1c70-4829-8224-ba9d2ef398bc",
        "team_2": "18ab11f0-3069-42bd-bac7-b5b8204c0383",
        "winner": null,
        "winning_players": null,
        "losing_team": null,
        "losing_players": null
    },
    "2ad7c927-67fa-4854-99b4-6c91e78712d9": {
        "uuid": "2ad7c927-67fa-4854-99b4-6c91e78712d9",
        "tournament_id": "33a78757-110e-4837-89de-065e504968ee",
        "match_date": "2006-05-05",
        "match_time": "15:00:00",
        "team_1": "382f652f-efdf-4298-9d15-922877e5e1b5",
        "team_2": "5b4a4ac3-eebe-456e-a123-8ca0fe90a263",
        "winner": null,
        "winning_players": null,
        "losing_team": null,
        "losing_players": null
    },
    "2e2789ea-5b29-4ad5-8973-c7857355d0ce": {
        "uuid": "2e2789ea-5b29-4ad5-8973-c7857355d0ce",
        "tournament_id": "33a78757-110e-4837-89de-065e504968ee",
        "match_date": "2006-05-05",
        "match_time": "16:00:00",
        "team_1": "To be revealed",
        "team_2": "To be revealed",
        "winner": null,
        "winning_players": null,
        "losing_team": null,
        "losing_players": null
    },
    "edff87ca-6e8a-43d9-8275-e5b645ef3c02": {
        "uuid": "edff87ca-6e8a-43d9-8275-e5b645ef3c02",
        "tournament_id": "e01fdbe7-315b-4b39-bf43-9c0af03e5880",
        "match_date": "2006-05-05",
        "match_time": "14:00:00",
        "team_1": "18ab11f0-3069-42bd-bac7-b5b8204c0383",
        "team_2": "382f652f-efdf-4298-9d15-922877e5e1b5",
        "winner": null,
        "winning_players": null,
        "losing_team": null,
        "losing_players": null
    },
    "b4620e4f-3ce8-44a2-aedb-2b8981a3687a": {
        "uuid": "b4620e4f-3ce8-44a2-aedb-2b8981a3687a",
        "tournament_id": "e01fdbe7-315b-4b39-bf43-9c0af03e5880",
        "match_date": "2006-05-05",
        "match_time": "15:00:00",
        "team_1": "fdedcdfa-4714-4d10-b0db-d5b192b634ec",
        "team_2": "cde9b285-b55b-4788-bb6c-f40bfe9d765f",
        "winner": null,
        "winning_players": null,
        "losing_team": null,
        "losing_players": null
    },
    "edcb0702-7c42-4d60-8cf1-6f3193e76c8a": {
        "uuid": "edcb0702-7c42-4d60-8cf1-6f3193e76c8a",
        "tournament_id": "e01fdbe7-315b-4b39-bf43-9c0af03e5880",
        "match_date": "2006-05-05",
        "match_time": "16:00:00",
        "team_1": "b26a8d5e-b571-41f8-a657-b5ad616299d2",
        "team_2": "b6f18db4-e778-4b72-84e6-91aed8125bb4",
        "winner": null,
        "winning_players": null,
        "losing_team": null,
        "losing_players": null
    },
    "504b3993-0e2f-4f8f-ae0c-597cebd76262": {
        "uuid": "504b3993-0e2f-4f8f-ae0c-597cebd76262",
        "tournament_id": "e01fdbe7-315b-4b39-bf43-9c0af03e5880",
        "match_date": "2006-05-05",
        "match_time": "17:00:00",
        "team_1": "To be revealed",
        "team_2": "To be revealed",
        "winner": null,
        "winning_players": null,
        "losing_team": null,
        "losing_players": null
    },
    "b127f0e7-02fd-400c-ba4e-e4206885271c": {
        "uuid": "b127f0e7-02fd-400c-ba4e-e4206885271c",
        "tournament_id": "e01fdbe7-315b-4b39-bf43-9c0af03e5880",
        "match_date": "2006-05-06",
        "match_time": "14:00:00",
        "team_1": "To be revealed",
        "team_2": "To be revealed",
        "winner": null,
        "winning_players": null,
        "losing_team": null,
        "losing_players": null
    },
    "8c2469a8-67af-4c4d-800e-d378d8ef28a8": {
        "uuid": "8c2469a8-67af-4c4d-800e-d378d8ef28a8",
        "tournament_id": "e01fdbe7-315b-4b39-bf43-9c0af03e5880",
        "match_date": "2006-05-06",
        "match_time": "15:00:00",
        "team_1": "To be revealed",
        "team_2": "To be revealed",
        "winner": null,
        "winning_players": null,
        "losing_team": null,
        "losing_players": null
    },
    "3e72fb27-30cd-4cc9-bf43-483447679cf6": {
        "uuid": "3e72fb27-30cd-4cc9-bf43-483447679cf6",
        "tournament_id": "c099a8c8-4da7-4a12-84d3-2f01dc5ca810",
        "match_date": "2006-05-05",
        "match_time": "14:00:00",
        "team_1": "382f652f-efdf-4298-9d15-922877e5e1b5",
        "team_2": "b6f18db4-e778-4b72-84e6-91aed8125bb4",
        "winner": "382f652f-efdf-4298-9d15-922877e5e1b5",
        "winning_players": null,
        "losing_team": "382f652f-efdf-4298-9d15-922877e5e1b5",
        "losing_players": [
            "0b8ea6ae-1acf-45f9-9b05-fe1c85973e68",
            "8b368c80-729e-4e76-9341-18d2be561b7c",
            "57a15dc5-bdb2-46b5-9777-f08d36bffdb9"
        ]
    },
    "ed842939-a404-4c93-811f-8459fe8902c4": {
        "uuid": "ed842939-a404-4c93-811f-8459fe8902c4",
        "tournament_id": "c099a8c8-4da7-4a12-84d3-2f01dc5ca810",
        "match_date": "2006-05-05",
        "match_time": "15:00:00",
        "team_1": "fdedcdfa-4714-4d10-b0db-d5b192b634ec",
        "team_2": "b26a8d5e-b571-41f8-a657-b5ad616299d2",
        "winner": null,
        "winning_players": null,
        "losing_team": null,
        "losing_players": null
    },
    "d9d3d019-393f-49cd-bbac-5bb042c28c01": {
        "uuid": "d9d3d019-393f-49cd-bbac-5bb042c28c01",
        "tournament_id": "c099a8c8-4da7-4a12-84d3-2f01dc5ca810",
        "match_date": "2006-05-05",
        "match_time": "16:00:00",
        "team_1": "To be revealed",
        "team_2": "To be revealed",
        "winner": null,
        "winning_players": null,
        "losing_team": null,
        "losing_players": null
    }
}       '''
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

    def end_tournament(self, uuid: str) -> None:
        """
        Parameters: uuid of tournament

        Archives the tournament tied to the given uuid and releases
        it's servers.
        """
        
        #print("debug: got into end tournament")
        #input()

        # Looks for the tournament with the given uuid.
        tournaments: list[Tournament] = DataLayerAPI.load_tournaments()
        for item in tournaments:
            if item.uuid == uuid:
                tournament: Tournament = item
                break
        else:
            raise ValidationError("Tournament with given uuid not found.")
        
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

        #print("debug: got into next round")
        #input()
        
        # Looks for the tournament with the given uuid.
        tournaments: list[Tournament] = DataLayerAPI.load_tournaments()
        for item in tournaments:
            if item.uuid == uuid:
                tournament: Tournament = item
                break
        else:
            raise ValidationError("Tournament with given uuid not found.")

        # Gets all matches tied to the tournament.
        matches: list[Match] = self._match_logic.get_matches(tournament.uuid)

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

        #print("debug", competing_teams)
        #input()

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
        matches = self._match_logic.get_matches(uuid)
    
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
        # Finds the tournament with a given uuid.
        tournaments: list[Tournament] = DataLayerAPI.load_tournaments()

        for item in tournaments:
            if item.uuid == tournament_uuid:
                tournament: Tournament = item
                break
        else:
            raise ValidationError("Tournament with given uuid not found.")

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
            tournaments: list[Tournament] = DataLayerAPI.load_tournaments()
            tournament: Tournament | None = next((t for t in tournaments if t.name == name), None)

            if tournament is None:
                raise Exception(f'No tournament found named: {name}')
            
            return tournament


    def tournament_name_to_uuid(self, name: str) -> str:
            tournament = self.get_tournament_by_name(name)
            return tournament.uuid
