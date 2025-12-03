"""
Author: Ísak Elí Hauksson <isak25@ru.is>
Date: 2025-12-03

File that holds the SpectatorUI class
which controls the options for the spectator
"""

from UtilityUI import UtilityUI


class SpectatorUI:

    def __init__(self) -> None:
        self.utility = UtilityUI()

    def show_tournaments(self):
        # shows all tournaments in a list
        self.utility.show_tournaments()

    def show_specific_tournament(self):
        # show a specific tournament
        self.utility.show_specific_tournament(...)

    def show_schedule(self):
        # show schedule
        self.utility.show_schedule()

    def show_clubs(self):
        # show all clubs
        self.utility.show_clubs()

    def show_teams(self):
        # show all teams
        self.utility.show_teams()

    def show_players(self):
        # show all players
        self.show_players()

    def show_specific_team(self):
        # take input from user and show that team
        self.show_specific_team()

    def logout(self):
        # go to the StartUI
        pass
