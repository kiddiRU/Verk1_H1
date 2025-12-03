"""
Author: Ísak Elí Hauksson <isak25@ru.is>
Date: 2025-12-03

File that holds the OrganizerUI class which controls
what the organizer can see
"""
from UtilityUI import UtilityUI

class OrganizerUi:

    def __init__(self) -> None:
        self.utility = UtilityUI()

    def manage_tournament(self):
        pass

    def create_tournament(self):
        pass

    def edit_tournament(self):
        pass

    def enter_match_results(self):
        pass

    def create_club(self):
        pass

    def show_club(self):
        self.utility.show_clubs()

    def show_tournaments(self):
        self.utility.show_tournaments()

    def show_teams(self):
        pass

    def show_specific_team(self):
        pass

    def players(self):
        pass

    def show_specific_players(self):
        pass

    def show_schedule(self):
        pass

    def logout(self):
        pass