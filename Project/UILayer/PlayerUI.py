"""
Author: Ísak Elí Hauksson <isak25@ru.is>
Date: 2025-12-04

File that holds all the menus that the player can access
"""

from UILayer.MenuOptions import MenuOptions
from UILayer.UtilityUI import UtilityUI


class PlayerUI:
    """Every player menu option"""

    def __init__(self) -> None:
        self.utility = UtilityUI()

    def start_screen(self) -> MenuOptions:
        """Start screen with choices: 1, 2, 3 and q

        Returns:
            MenuOptions: The next menu to navigate to
        """
        print(
            r"""
————————————————————————————————————————————————————————————————————————————————
             _____                  __ 
  ___       / ___/____  ____  _____/ /_
 / _ \______\__ \/ __ \/ __ \/ ___/ __/
/  __/_____/__/ / /_/ / /_/ / /  / /_  
\___/     /____/ .___/\____/_/   \__/  
            /_/                      
    ______     __                                                      
   / ____/  __/ /__________ __   ______ _____ _____ _____  ____  ____ _
  / __/ | |/_/ __/ ___/ __ `/ | / / __ `/ __ `/ __ `/ __ \/_  / / __ `/
 / /____>  </ /_/ /  / /_/ /| |/ / /_/ / /_/ / /_/ / / / / / /_/ /_/ / 
/_____/_/|_|\__/_/   \__,_/ |___/\__,_/\__, /\__,_/_/ /_/ /___/\__,_/  
                                    /____/          
————————————————————————————————————————————————————————————————————————————————
StartPage
————————————————————————————————————————————————————————————————————————————————
                                 Start Page
————————————————————————————————————————————————————————————————————————————————
1 Login
2 Register 
3 Spectate
q Quit
————————————————————————————————————————————————————————————————————————————————
"""
        )
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
        print(
            r"""
* User Path *
StartPage -> Login
————————————————————————————————————————————————————————————————————————————————
                                    Login
————————————————————————————————————————————————————————————————————————————————
"""
        )
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
        print("This is the register page")
        return MenuOptions.main_menu
