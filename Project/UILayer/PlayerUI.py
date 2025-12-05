"""
Author: Ísak Elí Hauksson <isak25@ru.is>
Date: 2025-12-04
Co-author: Andri Már Kristjánsson <andrik25@ru.is>

File that holds all the menus that the player can access
"""

from UILayer.MenuOptions import MenuOptions
from UILayer.UtilityUI import UtilityUI
from UILayer.Drawer import Drawer


class PlayerUI:
    """Every player menu option"""

    def __init__(self) -> None:
        self.utility = UtilityUI()

    def start_screen(self) -> MenuOptions:
        """Start screen with choices: 1, 2, 3 and q

        Returns:
            MenuOptions: The next menu to navigate to
        """
        menu = "Start Page"
        user_path = ["StartPage"]
        options = ["1 Log In", "2 Register", "3 Spectate", "q Quit"]

        tui = Drawer()
        print(tui.table(menu, user_path, options))


        choice: str = self.utility._prompt_choice(["1", "2", "3", "q"])
        match choice:
            case "1":
                return MenuOptions.login
            case "2":
                return MenuOptions.register
            case "3":
                return MenuOptions.spectate_page
            case "q":
                return MenuOptions.quit

        return MenuOptions.back

    def login_screen(self) -> MenuOptions:
        """Login screen, choices: fill info with input

        Returns:
            MenuOptions: The next menu to navigate to
        """

        menu = "Login"
        user_path = ["StartPage", "Login"]

        tui = Drawer()
        print(tui.table(menu, user_path))        


        choice: str = self.utility._input_info("Input Your Handle: ")
        if choice == "admin":
            return MenuOptions.admin_page

        # TODO: check if handle exists from LL API
        # if choice in Player_list:
        #     return MenuOption.player_page

        return MenuOptions.quit

    def register_screen(self) -> MenuOptions:
        """Register screen, choices: fill info with input

        Returns:
            MenuOptions: The next menu to navigate to
        """
        # TODO: add fill in option
        
        
        menu = "Register"
        user_path = ["StartPage", "Register"]

        tui = Drawer()
        print(tui.table(menu, user_path))   
        choice = input()
        

        return MenuOptions.main_menu
