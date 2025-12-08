'''
Author: Kristjan Hagalin <kristjanhj24@ru.is>
Date: 2025-12-05

Functions for tournament logic.
'''

from Models import Player, Team, Tournament
from DataLayer import DataLayerAPI
from uuid import uuid4

class TournamentLL:
    def __init__(self, data_api: DataLayerAPI):
        self._data_api: DataLayerAPI = data_api

    def create_tournament(self,
        name,
        start_date: str,
        end_date: str,
        time_frame_start,
        time_frame_end, 
        venue: str,
        email: str,
        phone_number: str,
        amount_of_servers: int
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
            number_of_servers = amount_of_servers
        )

        self._data_api.store_tournament(new_tournament)