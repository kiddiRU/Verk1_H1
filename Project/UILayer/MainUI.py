"""
Author: Ísak Elí Hauksson <isak25@ru.is>
Date: 2025-12-03

File that holds the main state machine.
"""

from LogicLayer.LogicLayerAPI import LogicAPI
from UILayer.MenuUI import MenuUI


class MainUI:
    """Main UI State Machine"""

    def __init__(self) -> None:
        logic_api = LogicAPI()
        self._menu_ui = MenuUI(logic_api)
        self.current_screen = "MAIN_MENU"

    def run(self) -> None:
        """Main navigation loop"""

        while True:
            if self.current_screen == "MAIN_MENU":
                self._menu_ui.show_start_screen()
