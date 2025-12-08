'''
Author: Kristjan Hagalin <kristjanhj24@ru.is>
Date: 2025-12-05

Functions for tournament logic.
'''

from Models import Player, Team, Tournament
from DataLayer import DataLayerAPI
from uuid import uuid4
from datetime import date, time

class TournamentLL:
    def __init__(self, data_api: DataLayerAPI):
        self._data_api: DataLayerAPI = data_api

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

        self._data_api.store_tournament(new_tournament)

    # TODO: Only changes the tournaments status at the moment.
    def publish(self, tournament_name: str) -> None:
        tournaments: list[Tournament] = self._data_api.load_tournaments()
        tournament: Tournament | None = next((t for t in tournaments if t.name == tournament_name), None)
        
        if tournament is None:
            raise Exception(f'No tournament found named: {tournament_name}')

        tournament.status = Tournament.StatusType.active
        self._data_api.store_tournament(tournament)

    def add_team(self, tournament_name: str, team_name: str) -> None:
        tournaments: list[Tournament] = self._data_api.load_tournaments()
        tournament: Tournament | None = next((t for t in tournaments if t.name == tournament_name), None)
        
        teams: list[Team] = self._data_api.load_teams()
        team: Team | None = next((t for t in teams if t.name == team_name), None)

        if tournament is None:
            raise Exception(f'No tournament found named: {tournament_name}')

        if team is None:
            raise Exception(f'No team found named: {team_name}')
        
        tournament.teams_playing.append(team.uuid)
        self._data_api.store_tournament(tournament)

    def remove_team(self, tournament_name: str, team_name: str) -> None:
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

        self._data_api.store_tournament(tournament)

    def update_info(
        self,
        name: str,
        venue: str, # ma breyta venue ef published?
        email: str,
        phone_number: str
    ) -> None:
        
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
    
    # TODO: Implement.
    def update_tournament_datetime(
        self,
        name: str,
        start_date: date,
        end_date: date,
        time_frame_start: time,
        time_frame_end: time
    ) -> None:
        
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