"""
Author: Ísak Elí Hauksson <isak25@ru.is>
Date: 2025-12-03

File that holds all the menus
"""

from UILayer.MenuOptions import MenuOptions


class MenuUI:
    """Every menu option with choices"""

    def __prompt_choice(self, valid_choices: list[str]) -> str:
        """
        Helper function for allowed choices for the user

        Args:
            valid_choices (list[str]): A list of valid choices for the user to input

        Returns:
            str: _description_
        """
        valid_choices_lower: list[str] = [x.lower() for x in valid_choices]

        while True:
            choice: str = input("> ").strip().lower()
            if choice in valid_choices_lower:
                return choice

            print("not a valid option try again")

    def __input_info(self, message: str) -> str:
        """
        A helper function for inputted string

        Args:
            message (str): The input message to the user

        Returns:
            str: The input from the user
        """
        choice: str = input(message)
        return choice.strip()

    def show_start_screen(self) -> str:
        """ Start screen with choices: 1, 2, 3 and q """
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
""")
        choice: str = self.__prompt_choice(["1", "2", "3", "q"])
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

    def show_login_screen(self) -> str:
        """ Login screen which asks for a player handle"""

        print(r"""
* User Path *
StartPage -> Login
————————————————————————————————————————————————————————————————————————————————
                                    Login
————————————————————————————————————————————————————————————————————————————————
""")
        choice: str = self.__input_info("Input Your Handle: ")
        if choice == "admin":
            return MenuOptions.admin_page
        
        # LogicLayerAPI.validate_unique_name(choice)
        
        # if choice in Player_list:
        #     return "PLAYER_SCREEN"
        return MenuOptions.quit


    def show_register_screen(self) -> str:
        choice: str = self.__prompt_choice(["1"])
        print("THIS IS REGISTER")
        return MenuOptions.main_menu

    def show_admin_page(self) -> str:
        print(r"""
* User Path *
StartPage -> AdminPage
————————————————————————————————————————————————————————————————————————————————
                                Admin Page
————————————————————————————————————————————————————————————————————————————————
1 Create Tournament
2 Manage Tournaments
3 Create Club
b Back
————————————————————————————————————————————————————————————————————————————————
Choose Action:
————————————————————————————————————————————————————————————————————————————————
"""
        )
        input("INOUT AS ADMIN")
        return MenuOptions.main_menu