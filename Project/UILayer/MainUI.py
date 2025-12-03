"""
Author: Ísak Elí Hauksson <isak25@ru.is>
Date: 2025-12-03

File that holds the main state machine.
"""


from UILayer.MenuUI import MenuUI
from UILayer.MenuOptions import MenuOptions


class MainUI:
    """Main UI State Machine"""

    def __init__(self) -> None:
        self._menu_ui = MenuUI()
        self.current_screen = MenuOptions.main_menu

    def run(self) -> None:
        """Main navigation loop"""

        while True:
            if self.current_screen == MenuOptions.main_menu:
                self.current_screen = self._menu_ui.show_start_screen()

            if self.current_screen == MenuOptions.login:
                self.current_screen = self._menu_ui.show_login_screen()

            if self.current_screen == "ADMIN":
                print("you are admin")

            if self.current_screen == "LOGOUT":
                self.current_screen = MenuOptions.main_menu

            if self.current_screen == "QUIT":
                exit()

            self.current_screen = MenuOptions.main_menu