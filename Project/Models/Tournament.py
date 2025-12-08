"""
Author: Ísak Elí Hauksson <isak25@ru.is>
Date: 2025-12-02

Tournament Model Class

Contributer:
    Kristinn Hrafn <kristinnd25@ru.is>
"""

from enum import StrEnum
from datetime import date, time


class Tournament:
    """Tournament Model Class"""

    class StatusType(StrEnum):
        active = "ACTIVE"
        inactive = "INACTIVE"
        archived = "ARCHIVED"

    def __init__(
        self,
        uuid: str,
        name: str,
        start_date: date,
        end_date: date,
        venue: str,
        email: str,
        phone_number: str,
        time_frame_start: time = time(hour=8,minute=0),
        time_frame_end: time = time(hour=16,minute=0),
        status: StatusType = StatusType.inactive,
        number_of_servers: int = 1,
        list_servers: list[str] = [],
        teams_playing: list[str] = [],
    ) -> None:
        """
        The initialization function of the Tournament model class

        Args:
            uuid (str): unique identifier
            name (str): Unique name for the tournament
            start_date (date): Start date of the tournament (YYYY-MM-DD)
            end_date (date): End date of the tournament (YYYY-MM-DD)
            venue (str): Location of the tournament
            email (str): Tournament email (length <= 64)
            phone_number (str): Tournament phone number 
                        (length of 8  = 000-0000)
            time_frame_start (time, optional): Start of the event per day. 
                        Defaults to time(hour=8,minute=0).
            time_frame_end (time, optional): End of the event per day. 
                        Defaults to time(hour=16,minute=0).
            status (StatusType, optional): Tournament status.
                        Defaults to StatusType.inactive.
            number_of_servers: (list[str]):
                        Defaults to 1. Don't pass if passing list_servers.
            list_servers (list[str], optional): 
                        List containing uuid's of servers. Defaults to [].
                        Don't pass if passing number_of_servers.
            teams_playing (list[str], optional): 
                        List containing uuid's of teams. Defaults to [].
        """
        
        self.uuid = uuid
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.time_frame_start = time_frame_start
        self.time_frame_end = time_frame_end
        self.venue = venue
        self.email = email
        self.phone_number = phone_number
        self.status = status

        if list_servers == []:
            self.list_servers: list[str] = [
                "NoServer" for _ in range(number_of_servers)
            ]
        else: self.list_servers = list_servers
        
        self.teams_playing = teams_playing

    def __str__(self) -> str:
        # TODO: NOT IMPLEMENTED
        return f""
    
