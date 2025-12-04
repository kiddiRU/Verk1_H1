"""
Author: Ísak Elí Hauksson <isak25@ru.is>
Date: 2025-12-03

File that holds the main state machine.
"""

from UILayer.MenuUI import MenuUI
from UILayer.MenuOptions import MenuOptions
import os


class MainUI:
    """Main UI State Machine"""

    def __init__(self) -> None:
        """Initializes the class"""

        self._menu_ui = MenuUI()
        self.current_screen = MenuOptions.main_menu

    def __clear(self):
        """Helper function that clears the screen"""

        os.system('cls' if os.name == 'nt' else 'clear')

    def run(self) -> None:
        """Main navigation loop"""

        while True:

            # main menu
            if self.current_screen == MenuOptions.main_menu:
                self.__clear()
                self.current_screen = self._menu_ui.show_start_screen()

            # login
            if self.current_screen == MenuOptions.login:
                self.__clear()
                self.current_screen = self._menu_ui.show_login_screen()

            # admin page
            if self.current_screen == MenuOptions.admin_page:
                self.__clear()
                self.current_screen = self._menu_ui.show_admin_page()

            # go to main menu if logout
            if self.current_screen == MenuOptions.logout:
                self.__clear()
                self.current_screen = MenuOptions.main_menu

            # back function
            if self.current_screen == MenuOptions.back:
                # TODO: need to add a way to keep track of paths traveled
                pass

            # stop when quit
            if self.current_screen == MenuOptions.quit:
                print("Quitting program")
                exit()

            # if nothing works then go to the main menu
            self.current_screen = MenuOptions.main_menu
