"""
Author: Ísak Elí Hauksson <isak25@ru.is>
Date: 2025-12-02

Tournament Model Class

Contributor:
    Kristinn Hrafn <kristinnd25@ru.is>
    Ísak Elí Hauksson <isak25@ru.is>
"""

from enum import StrEnum
from datetime import date, time


class Tournament:
    """
    Represents a tournament including its schedule, venue, servers, and teams.

    Each tournament has a unique identifier and name. Tracks start/end dates,
    daily timeframes, contact info, status, list of servers,
    and participating teams.

    :param uuid: Unique identifier for the tournament
    :type uuid: str
    :param name: Unique tournament name
    :type name: str
    :param start_date: Tournament start date (YYYY-MM-DD)
    :type start_date: date
    :param end_date: Tournament end date (YYYY-MM-DD)
    :type end_date: date
    :param venue: Location of the tournament
    :type venue: str
    :param email: Tournament email (max 39 characters)
    :type email: str
    :param phone_number: Tournament phone number (format: 000-0000)
    :type phone_number: str
    :param time_frame_start: Daily start time of tournament, defaults to 08:00
    :type time_frame_start: time, optional
    :param time_frame_end: Daily end time of tournament, defaults to 16:00
    :type time_frame_end: time, optional
    :param status: Tournament status (active, inactive, archived),
    defaults to inactive
    :type status: Tournament.StatusType, optional
    :param number_of_servers: Number of servers to assign if list_servers
    is not provided
    :type number_of_servers: int, optional
    :param list_servers: List of server UUIDs, defaults to empty list
    :type list_servers: list[str], optional
    :param teams_playing: List of team UUIDs participating in
    tournament, defaults to empty list
    :type teams_playing: list[str], optional
    :rtype: None
    """

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
        time_frame_start: time = time(hour=8, minute=0),
        time_frame_end: time = time(hour=16, minute=0),
        status: StatusType = StatusType.inactive,
        number_of_servers: int = 1,
        list_servers: list[str] = [],
        teams_playing: list[str] = [],
    ) -> None:
        """
        Initialize a Tournament instance.

        Sets up tournament properties including schedule,
        servers, teams, and contact info.

        :param uuid: Unique identifier for the tournament
        :param name: Unique tournament name
        :param start_date: Tournament start date (YYYY-MM-DD)
        :param end_date: Tournament end date (YYYY-MM-DD)
        :param venue: Location of the tournament
        :param email: Tournament email (max 39 characters)
        :param phone_number: Tournament phone number (format: 000-0000)
        :param time_frame_start: Daily start time of tournament,
        defaults to 08:00
        :param time_frame_end: Daily end time of tournament, defaults to 16:00
        :param status: Tournament status (active, inactive, archived),
        defaults to inactive
        :param number_of_servers: Number of servers to assign if
        list_servers is not provided
        :param list_servers: List of server UUIDs, defaults to empty list
        :param teams_playing: List of team UUIDs participating in tournament,
        defaults to empty list
        :rtype: None
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
        else:
            self.list_servers = list_servers

        self.teams_playing = teams_playing
