"""
Author: Ísak Elí Hauksson <isak25@ru.is>
Date: 2025-12-03
Co-author: Andri Már Kristjánsson <andrik25@ru.is>

File that holds the main state machine.
"""

import os
from UILayer.UtilityUI import UtilityUI
from UILayer.AdminUI import AdminUI
from UILayer.PlayerUI import PlayerUI
from UILayer.SpectateUI import SpectateUI
from UILayer.MenuOptions import MenuOptions


class MainUI:
    """Main UI State Machine"""

    def __init__(self) -> None:
        """Initializes the class"""
        self._utility_ui: UtilityUI = UtilityUI()
        self._admin_ui: AdminUI = AdminUI()
        self._player_ui: PlayerUI = PlayerUI()
        self._spectate_ui: SpectateUI = SpectateUI()
        self.current_screen: MenuOptions = MenuOptions.main_menu

    def __clear(self):
        """Helper function that clears the screen"""

        os.system('cls' if os.name == 'nt' else 'clear')

    def run(self) -> None:
        """Main navigation loop"""

        while True:
            
            # main menu
            if self.current_screen == MenuOptions.main_menu:
                self.current_screen = self._player_ui.start_screen()

            # login
            elif self.current_screen == MenuOptions.login:
                self.current_screen = self._player_ui.login_screen()

            # register
            elif self.current_screen == MenuOptions.register:
                self.current_screen = self._player_ui.register_screen()

            # spectate
            elif self.current_screen == MenuOptions.spectate_screen:
                self.current_screen = self._spectate_ui.spectate_screen()

            # ------------------ Admin Paths ------------------
            # admin page
            elif self.current_screen == MenuOptions.admin_page:
                self.current_screen = self._admin_ui.admin_screen()

            # create tournament
            elif self.current_screen == MenuOptions.create_tournament:
                self.current_screen = self._admin_ui.create_tournament()

            # manage tournament
            elif self.current_screen == MenuOptions.manage_tournament:
                self.current_screen = self._admin_ui.manage_tournaments()

            # create club
            elif self.current_screen == MenuOptions.create_club:
                self.current_screen = self._admin_ui.create_club()

            # manage tournaments
            elif self.current_screen == MenuOptions.manage_tournament:
                self.current_screen = self._admin_ui.manage_tournaments()

            # manage active tournament
            elif self.current_screen == MenuOptions.manage_active_tournament:
                self.current_screen = self._admin_ui.manage_active_tournament()

            # manage inactive tournament
            elif self.current_screen == MenuOptions.manage_inactive_tournament:
                self.current_screen = (
                    self._admin_ui.manage_inactive_tournament()
                )

            # select match
            elif self.current_screen == MenuOptions.select_match:
                self.current_screen = self._admin_ui.matches()

            # input match results
            elif self.current_screen == MenuOptions.input_results:
                self.current_screen = self._admin_ui.match_results()

            # manage teams in tournament
            elif self.current_screen == MenuOptions.manage_teams:
                self.current_screen = self._admin_ui.manage_teams()

            # add team to tournament
            elif self.current_screen == MenuOptions.add_team:
                self.current_screen = self._admin_ui.add_team()

            # remove team from tournament
            elif self.current_screen == MenuOptions.remove_team:
                self.current_screen = self._admin_ui.remove_team()

            # publish tournament
            elif self.current_screen == MenuOptions.publish:
                self.current_screen = self._admin_ui.publish()

            # edit tournament menu
            elif self.current_screen == MenuOptions.edit_tournament:
                self.current_screen = self._admin_ui.edit_tournament()

            # edit tournament time
            elif self.current_screen == MenuOptions.edit_tournament_time:
                self.current_screen = self._admin_ui.edit_tournament_time()

            # edit tournament info
            elif self.current_screen == MenuOptions.edit_tournament_info:
                self.current_screen = self._admin_ui.edit_tournament_info()

            # ------------------ Player Paths ------------------

            # player page
            elif self.current_screen == MenuOptions.player_page:
                self.current_screen = self._player_ui.player_page()

            # edit player information
            elif self.current_screen == MenuOptions.edit_player_info:
                self.current_screen = self._player_ui.edit_player_info()

            # check team if empty
            elif self.current_screen == MenuOptions.my_team_empty:
                self.current_screen = self._player_ui.my_team_empty()
            
            # check team if not empty
            elif self.current_screen == MenuOptions.my_team_not_empty:
                self.current_screen = self._player_ui.my_team_not_empty()

            # create a team
            elif self.current_screen == MenuOptions.create_team:
                self.current_screen = self._player_ui.create_team()

            # edit your team
            elif self.current_screen == MenuOptions.edit_team:
                self.current_screen = self._player_ui.edit_team()

            # add player to team
            elif self.current_screen == MenuOptions.add_player:
                self.current_screen = self._player_ui.add_player()

            # remove player from team
            elif self.current_screen == MenuOptions.remove_player:
                self.current_screen = self._player_ui.remove_player()

            # leave team
            elif self.current_screen == MenuOptions.leave_team:
                self.current_screen = self._player_ui.leave_team()

            # ------------------ Spectate Paths ------------------

            # spectate players
            elif self.current_screen == MenuOptions.spectate_players:
                self.current_screen = self._spectate_ui.spectate_players()
            
            # view specific player stats
            elif self.current_screen == MenuOptions.view_player_stats:
                self.current_screen = self._spectate_ui.view_player_stats()
            
            # spectate clubs
            elif self.current_screen == MenuOptions.spectate_clubs:
                self.current_screen = self._spectate_ui.spectate_clubs()

            # view specific clubs stats
            elif self.current_screen == MenuOptions.view_club_stats:
                self.current_screen = self._spectate_ui.view_club_stats()
            
            # spectate teams
            elif self.current_screen == MenuOptions.spectate_teams:
                self.current_screen = self._spectate_ui.spectate_teams()
            
            # view specific player stats
            elif self.current_screen == MenuOptions.view_team_stats:
                self.current_screen = self._spectate_ui.view_team_stats()

            # get a list of tournaments (shows which is active and inactive)
            elif self.current_screen == MenuOptions.spectate_tournaments:
                self.current_screen = self._spectate_ui.spectate_tournaments()

            # options for active tournament
            elif self.current_screen == MenuOptions.active_tournament:
                self.current_screen = self._spectate_ui.active_tournament()
            
            # options for archived tournaments 
            elif self.current_screen == MenuOptions.archived_tournament:
                self.current_screen = self._spectate_ui.archived_tournament()

            # see specific tournament schedule
            elif self.current_screen == MenuOptions.game_schedule:
                self.current_screen = self._spectate_ui.game_schedule()

            # view specific tournaments brackets
            elif self.current_screen == MenuOptions.view_bracket:
                self.current_screen = self._spectate_ui.view_bracket()
            
            # see all teams in a tournament
            elif self.current_screen == MenuOptions.teams_in_tournament:
                self.current_screen = self._spectate_ui.teams_in_tournament()

            # select specific team to see stats
            elif self.current_screen == MenuOptions.team_tournament_stats:
                self.current_screen = self._spectate_ui.team_tournament_stats()

            # ------------------ Misc Paths ------------------

            # go to main menu if logout
            elif self.current_screen == MenuOptions.logout:
                self.current_screen = MenuOptions.main_menu

            # stop when quit
            elif self.current_screen == MenuOptions.quit:
                print("Quitting program")
                exit()

            else:
                self.current_screen = self._utility_ui.screen_not_exist_error()
