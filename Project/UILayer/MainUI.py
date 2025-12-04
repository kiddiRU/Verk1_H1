"""
Author: Ísak Elí Hauksson <isak25@ru.is>
Date: 2025-12-03

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
            self.__clear()
            # main menu
            if self.current_screen == MenuOptions.main_menu:
                self.current_screen = self._player_ui.start_screen()

            # login
            elif self.current_screen == MenuOptions.login:
                self.current_screen = self._player_ui.login_screen()

            # admin page
            elif self.current_screen == MenuOptions.admin_page:
                self.current_screen = self._admin_ui.admin_screen()

            # go to main menu if logout
            elif self.current_screen == MenuOptions.logout:
                self.current_screen = MenuOptions.main_menu

            # back function
            elif self.current_screen == MenuOptions.back:
                # TODO: need to add a way to keep track of paths traveled
                pass

            # stop when quit
            elif self.current_screen == MenuOptions.quit:
                print("Quitting program")
                exit()

            else:
                self.current_screen = self._utility_ui.screen_exist_error()
