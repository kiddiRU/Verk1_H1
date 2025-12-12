"""
Author: Ísak Elí Hauksson <isak25@ru.is>
Date: 2025-12-03

Collaborator: Sindri Freysson <Sindrif25@ru.is>

File that holds the main state machine.
"""

from UILayer.UtilityUI import UtilityUI
from UILayer.AdminUI import AdminUI
from UILayer.PlayerUI import PlayerUI
from UILayer.SpectateUI import SpectateUI
from UILayer.MenuOptions import MenuOptions


class MainUI:
    """Main UI state machine controlling all screen transitions."""

    def __init__(self) -> None:
        """
        Initializes the UI controller.

        Sets up references to all UI classes and creates a mapping from
        MenuOptions to the corresponding screen-handling functions.
        """
        self.player_username: str | None = None
        self.team_name: str | None = None
        self._utility_ui: UtilityUI = UtilityUI()
        self._admin_ui: AdminUI = AdminUI()
        self._player_ui: PlayerUI = PlayerUI()
        self._spectate_ui: SpectateUI = SpectateUI()
        self.current_screen: MenuOptions = MenuOptions.START_SCREEN

        # Holds a map of corresponding screens
        self.screens = {
            MenuOptions.START_SCREEN: self._player_ui.start_screen,
            MenuOptions.LOGIN: self._player_ui.login_screen,
            MenuOptions.REGISTER: self._player_ui.register_screen,
            MenuOptions.SPECTATE_SCREEN: self._spectate_ui.spectate_screen,
            MenuOptions.ONION: self._player_ui.onion,
            MenuOptions.MASTERPIECE: self._player_ui.masterpiece,
            MenuOptions.SINDRI_FC: self._player_ui.sindri_fc,
            # ------------------ Admin Paths ------------------
            MenuOptions.ADMIN_SCREEN: self._admin_ui.admin_screen,
            MenuOptions.CREATE_TOURNAMENT: self._admin_ui.create_tournament,
            MenuOptions.MANAGE_TOURNAMENT: self._admin_ui.manage_tournaments,
            MenuOptions.CREATE_CLUB: self._admin_ui.create_club,
            MenuOptions.MANAGE_INACTIVE_TOURNAMENT: (
                self._admin_ui.manage_inactive_tournament
            ),
            MenuOptions.MANAGE_ACTIVE_TOURNAMENT: (
                self._admin_ui.manage_active_tournament
            ),
            MenuOptions.SELECT_MATCH: self._admin_ui.matches,
            MenuOptions.INPUT_RESULTS: self._admin_ui.match_results,
            MenuOptions.MANAGE_TEAMS: self._admin_ui.manage_teams,
            MenuOptions.ADD_TEAM: self._admin_ui.add_team,
            MenuOptions.REMOVE_TEAM: self._admin_ui.remove_team,
            MenuOptions.PUBLISH: self._admin_ui.publish,
            # ------------------ Player Paths ------------------
            MenuOptions.PLAYER_SCREEN: self._player_ui.player_screen,
            MenuOptions.EDIT_PLAYER_INFO: self._player_ui.edit_player_info,
            MenuOptions.MY_TEAM_EMPTY: self._player_ui.my_team_empty,
            MenuOptions.MY_TEAM_NOT_EMPTY: self._player_ui.my_team_not_empty,
            MenuOptions.CREATE_TEAM: self._player_ui.create_team,
            MenuOptions.EDIT_TEAM: self._player_ui.edit_team,
            MenuOptions.ADD_PLAYER: self._player_ui.add_player,
            MenuOptions.REMOVE_PLAYER: self._player_ui.remove_player,
            MenuOptions.LEAVE_TEAM: self._player_ui.leave_team,
            MenuOptions.CREATE_TEAM_IN_TEAM: (
                self._player_ui.create_team_in_team
            ),
            # ------------------ Spectate Paths ------------------
            MenuOptions.SPECTATE_PLAYERS: self._spectate_ui.spectate_players,
            MenuOptions.VIEW_PLAYER_STATS: self._spectate_ui.view_player_stats,
            MenuOptions.SPECTATE_CLUBS: self._spectate_ui.spectate_clubs,
            MenuOptions.VIEW_CLUB_STATS: self._spectate_ui.view_club_stats,
            MenuOptions.SPECTATE_TEAMS: self._spectate_ui.spectate_teams,
            MenuOptions.VIEW_TEAM_STATS: self._spectate_ui.view_team_stats,
            MenuOptions.SPECTATE_TOURNAMENTS: (
                self._spectate_ui.spectate_tournaments
            ),
            MenuOptions.ACTIVE_TOURNAMENT: self._spectate_ui.active_tournament,
            MenuOptions.ARCHIVED_TOURNAMENT: (
                self._spectate_ui.archived_tournament
            ),
            MenuOptions.GAME_SCHEDULE: self._spectate_ui.game_schedule,
            MenuOptions.TEAMS_IN_TOURNAMENT: (
                self._spectate_ui.teams_in_tournament
            ),
            MenuOptions.TEAM_TOURNAMENT_STATS: (
                self._spectate_ui.team_tournament_stats
            ),
            # ------------------ Misc Paths ------------------
            MenuOptions.LOGOUT: self._player_ui.start_screen,
        }

    def screen_not_exist_error(self) -> MenuOptions:
        """
        A screen that shows up if the
        main ui state machine cant find any screen
        (NOTE: Should never happen)

        :return: The next screen to go to
        :rtype: MenuOptions
        """

        print("Screen doesn't exist")
        input("Input anything to go back to start: ")
        return MenuOptions.START_SCREEN

    def run(self) -> None:
        """
        Main application loop.

        Handles user input and transitions to the appropriate screen.
        """

        while True:
            if self.screens.get(self.current_screen) is not None:
                self.current_screen = self.screens[self.current_screen]()

            # ------------------ Misc Paths ------------------
            # stop when quit
            elif self.current_screen == MenuOptions.QUIT:
                print("Quitting Program")
                exit()

            else:
                self.current_screen = self.screen_not_exist_error()
