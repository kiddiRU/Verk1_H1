""" 
Author: Elmar Sigmarsson > elmars25@ru.is <
Date: 2025/12/02

Server model class
"""

class Server():
    """ Server model class """

    def __init__(
            self,
            server_uuid: str,
            match_in_server: str
            ) -> None:
        
        """
         Initializer for Match model class
        
         Args:
         server_uuid (str): unique id for server
         match_in_server (str): the match uuid that is using that server 
        """
        
        self.server_uuid = server_uuid
        self.match_in_server = match_in_server

        