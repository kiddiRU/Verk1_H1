"""
Author: Elmar Sigmarsson > elmars25@ru.is <
Date: 2025-12-02

Server model class

Contributor:
    Ísak Elí Hauksson <isak25@ru.is>
"""


class Server:
    """
    Represents a server used to host a match in the system.

    Each server has a unique identifier and keeps track of the match
    currently assigned to it.

    :param uuid: Unique identifier for the server
    :type uuid: str
    :param match_in_server: UUID of the match currently assigned to this server
    :type match_in_server: str
    :rtype: None
    """

    def __init__(self, uuid: str, match_in_server: str) -> None:
        """
        Initialize a Server instance.

        Sets the server's unique identifier and the match it is hosting.

        :param uuid: Unique identifier for the server
        :param match_in_server: UUID of the match
        currently assigned to this server
        :rtype: None
        """

        self.uuid = uuid
        self.match_in_server = match_in_server
