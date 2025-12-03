"""
Author: Ísak Elí Hauksson <isak25@ru.is>
Date: 2025-12-03

File that holds the PlayerUI class
which controls what options the player gets
"""

from UtilityUI import UtilityUI
from Models.Team import Team


class PlayerUI:

    def __init__(self, team_name: Team) -> None:
        self.team_name = team_name.name
        self.utility = UtilityUI()

    def show_team(self):
        self.utility.show_specific_team(self.team_name)

    def edit_player_info(self):
        pass

    def add_team(self):
        pass

    def add_player_to_team(self):
        # possible if Team.team_captain_uuid == Player.uuid
        # or comparing the handles
        pass

    def remove_player_from_team(self):
        # possible if Team.team_captain_uuid == Player.uuid
        # or comparing the handles
        pass

    def edit_team_info(self):
        # possible if Team.team_captain_uuid == Player.uuid
        # or comparing the handles
        pass

    def logout(self):
        pass
