'''
Author: Kristjan Hagalin <kristjanhj24@ru.is>
Date: 2025-12-05

Functions for tournament logic.
'''

from Models import Player, Team, Tournament, Server, Match
from DataLayer import DataLayerAPI
from uuid import uuid4
from datetime import date, time, timedelta, datetime

class TournamentLL:
    def __init__(self):
        self._data_api = DataLayerAPI

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

        self._data_api.store_tournament(new_tournament)

    def add_team(self, tournament_name: str, team_name: str) -> None:
        '''
        Takes in a tournament and team name.

        Adds the teams UUID to the teams_playing list in the tournament.
        '''
        tournaments: list[Tournament] = self._data_api.load_tournaments()
        tournament: Tournament | None = next((t for t in tournaments if t.name == tournament_name), None)
        
        teams: list[Team] = self._data_api.load_teams()
        team: Team | None = next((t for t in teams if t.name == team_name), None)

        if tournament is None:
            raise Exception(f'No tournament found named: {tournament_name}')

        if team is None:
            raise Exception(f'No team found named: {team_name}')
        
        if team.uuid in tournament.teams_playing:
            raise Exception(f'The team \'{team_name}\' is already in the tournament \'{tournament_name}\'!')
        
        tournament.teams_playing.append(team.uuid)
        self._data_api.update_tournament(tournament.uuid, tournament)

    def remove_team(self, tournament_name: str, team_name: str) -> None:
        '''
        Takes in a tournament and team name.

        Removes the teams UUID from the teams_playing list in the tournament.
        '''
        tournaments: list[Tournament] = self._data_api.load_tournaments()
        tournament: Tournament | None = next((t for t in tournaments if t.name == tournament_name), None)
        
        teams: list[Team] = self._data_api.load_teams()
        team: Team | None = next((t for t in teams if t.name == team_name), None)

        if tournament is None:
            raise Exception(f'No tournament found named: {tournament_name}')

        if team is None:
            raise Exception(f'No team found named: {team_name}')
        
        if team.uuid in tournament.teams_playing:
            tournament.teams_playing.remove(team.uuid)

        self._data_api.update_tournament(tournament.uuid, tournament)

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
        
        tournaments: list[Tournament] = self._data_api.load_tournaments()
        tournament: Tournament | None = next((t for t in tournaments if t.name == name), None)

        if tournament is None:
            raise Exception(f'No tournament found named: {name}')

        for attr, value in params.items():
            if value == '':
                continue
        
            setattr(tournament, attr, value)

        self._data_api.update_tournament(tournament.uuid, tournament)
    
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
        
        tournaments: list[Tournament] = self._data_api.load_tournaments()
        tournament: Tournament | None = next((t for t in tournaments if t.name == name), None)

        if tournament is None:
            raise Exception(f'No tournament found named: {name}')

        if tournament.status == Tournament.StatusType.active:
            raise Exception('You can\'t change the time of an active tournament!')

        for attr, value in params.items():
            setattr(tournament, attr, value)

        self._data_api.update_tournament(tournament.uuid, tournament)

    def list_tournaments(self) -> list[Tournament]:
        tournaments: list[Tournament] = self._data_api.load_tournaments()
        return tournaments

    def publish(self, uuid: str) -> None:
        tournaments: list[Tournament] = DataLayerAPI.load_tournaments()

        for item in tournaments:
            if item.uuid == uuid:
                tournament: Tournament = item
                break
        else:
            # TODO Add a real assert
            assert(False)

        tournament.status = Tournament.StatusType.active

        for idx, _ in enumerate(tournament.list_servers):
            # TODO Maybe move to ServerLL
            new_server = Server(str(uuid4()), "NoMatch")
            tournament.list_servers[idx] = new_server.uuid

        number_of_players: int = len(tournament.teams_playing)
        matches_per_round: list[int] = []

        while 1 < number_of_players:
            matches_per_round.append(number_of_players // 2)
            number_of_players -= matches_per_round[-1]

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

        # TODO add real assert
        if times_used[-1] >= datetime.combine(date = tournament.end_date, time = tournament.time_frame_end):
            assert(False)

        for x in times_used:
            print(x)
