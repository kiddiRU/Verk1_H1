"""
Author: Ísak Elí Hauksson <isak25@ru.is>
Date: 2025-12-03

Collaborator: Sindri Freysson <Sindrif25@ru.is>

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
        self.player_username: str|None = None
        self.team_name: str|None = None
        self._utility_ui: UtilityUI = UtilityUI()
        self._admin_ui: AdminUI = AdminUI()
        self._player_ui: PlayerUI = PlayerUI()
        self._spectate_ui: SpectateUI = SpectateUI()
        self.current_screen: MenuOptions = MenuOptions.start_screen

        self.screens = {
            MenuOptions.start_screen: self._player_ui.start_screen,
            MenuOptions.login: self._player_ui.login_screen,
            MenuOptions.register: self._player_ui.register_screen,
            MenuOptions.spectate_screen: self._spectate_ui.spectate_screen,
            # ------------------ Admin Paths ------------------
            MenuOptions.admin_screen: self._admin_ui.admin_screen,
            MenuOptions.create_tournament: self._admin_ui.create_tournament,
            MenuOptions.manage_tournament: self._admin_ui.manage_tournaments,
            MenuOptions.create_club: self._admin_ui.create_club,
            MenuOptions.manage_inactive_tournament: self._admin_ui.manage_inactive_tournament,
            MenuOptions.manage_active_tournament: self._admin_ui.manage_active_tournament,
            MenuOptions.select_match: self._admin_ui.matches,
            MenuOptions.input_results: self._admin_ui.match_results,
            MenuOptions.manage_teams: self._admin_ui.manage_teams,
            MenuOptions.add_team: self._admin_ui.add_team,
            MenuOptions.remove_team: self._admin_ui.remove_team,
            MenuOptions.publish: self._admin_ui.publish,
            MenuOptions.edit_tournament: self._admin_ui.edit_tournament,
            MenuOptions.edit_tournament_time: self._admin_ui.edit_tournament_time,
            MenuOptions.edit_tournament_info: self._admin_ui.edit_tournament_info,
            # ------------------ Player Paths ------------------
            MenuOptions.player_screen: self._player_ui.player_screen,
            MenuOptions.edit_player_info: self._player_ui.edit_player_info,
            MenuOptions.my_team_empty: self._player_ui.my_team_empty,
            MenuOptions.my_team_not_empty:  self._player_ui.my_team_not_empty,
            MenuOptions.create_team: self._player_ui.create_team,
            MenuOptions.edit_team: self._player_ui.edit_team,
            MenuOptions.add_player: self._player_ui.add_player,
            MenuOptions.remove_player: self._player_ui.remove_player,
            MenuOptions.leave_team: self._player_ui.leave_team,
            # ------------------ Spectate Paths ------------------
            MenuOptions.spectate_players: self._spectate_ui.spectate_players,
            MenuOptions.view_player_stats: self._spectate_ui.view_player_stats,
            MenuOptions.spectate_clubs: self._spectate_ui.spectate_clubs,
            MenuOptions.view_club_stats: self._spectate_ui.view_club_stats,
            MenuOptions.spectate_teams: self._spectate_ui.spectate_teams,
            MenuOptions.view_team_stats: self._spectate_ui.view_team_stats,
            MenuOptions.spectate_tournaments: self._spectate_ui.spectate_tournaments,
            MenuOptions.active_tournament: self._spectate_ui.active_tournament,
            MenuOptions.archived_tournament:  self._spectate_ui.archived_tournament,
            MenuOptions.game_schedule: self._spectate_ui.game_schedule,
            MenuOptions.view_bracket: self._spectate_ui.view_bracket,
            MenuOptions.teams_in_tournament: self._spectate_ui.teams_in_tournament,
            MenuOptions.team_tournament_stats: self._spectate_ui.team_tournament_stats,
            # ------------------ Misc Paths ------------------
            MenuOptions.logout: self._player_ui.start_screen
        }

    def __clear(self):
        """Helper function that clears the screen"""

        os.system('cls' if os.name == 'nt' else 'clear')

    def run(self) -> None:
        """Main navigation loop"""

        while True:
            if self.screens.get(self.current_screen) is not None:
                self.current_screen = self.screens[self.current_screen]()
            
             # ------------------ Misc Paths ------------------
             # stop when quit
            elif self.current_screen == MenuOptions.quit:
                print("Quitting program")
                exit()

            else:
                self.current_screen = self._utility_ui.screen_not_exist_error()
