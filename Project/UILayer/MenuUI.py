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

            print("Not a valid option try again")

    def __input_info(self, message: str) -> str:
        """
        A helper function for inputted string that checks for too long strings

        Args:
            message (str): The input message to the user

        Returns:
            str: The input from the user
        """
        while True:
            choice: str = input(message)
            if len(choice) >= 3 and len(choice) <= 40:
                return choice.strip()
            print("Not a valid length")

    def show_start_screen(self) -> MenuOptions:
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

    def show_login_screen(self) -> MenuOptions:
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
        choice: str = self.__input_info("Input Your Handle: ")
        if choice == "admin":
            return MenuOptions.admin_page
        
        # TODO: check if handle exists from LL API
        # if choice in Player_list:
        #     return MenuOption.player_page

        return MenuOptions.quit

    def show_register_screen(self) -> MenuOptions:
        """ Register screen, choices: fill info with input

        Returns:
            MenuOptions: The next menu to navigate to 
        """
        #TODO: add fill in option
        print("This is the register page")
        return MenuOptions.main_menu


    def show_admin_screen(self) -> MenuOptions:
        """ Admin screen, choices: 1,2,3 and b

        Returns:
            MenuOptions: The next menu to navigate to 
        """
        print(
            r"""
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
        choice: str = self.__prompt_choice(["1", "2", "3", "b"])
        match choice:
            case "1":
                return MenuOptions.create_tournament
            case "2":
                return MenuOptions.manage_tournament
            case "3":
                return MenuOptions.create_club
            case "b":
                return MenuOptions.main_menu
        return MenuOptions.main_menu

    def show_create_tournament(self) -> MenuOptions:
        """ Create tournament screen, choices: fill info with input

        Returns:
            MenuOptions: The next menu to navigate to 
        """

        print("This is the create tournament page")
        #TODO: add fill in options
        return MenuOptions.admin_page

    
    def show_manage_tournaments(self) -> MenuOptions:
        """ Manage tournaments screen, choices: choose with input

        Returns:
            MenuOptions: The next menu to navigate to 
        """

        print("This is the manage tournaments screen")
        print("HERE a list of all the tournaments shows")

        #TODO: add input for tournament to manage
        #TODO: if active the go to active screen else inactive screen
        return MenuOptions.admin_page

    
    def manage_active_tournament(self) -> MenuOptions:
        """ Active tournament screen, choices: 1,2,3(c requirement) and b

        Returns:
            MenuOptions: The next menu to navigate to 
        """

        print("This is the active tournaments screen")
        choice: str = self.__prompt_choice(["1", "2", "3", "b"])
        match choice:
            case "1":
                return MenuOptions.select_match
            # case "2": 
            #     return MenuOptions.cancel_tournament  #TODO: Optional C requirement
            case "b":
                return MenuOptions.back
        return MenuOptions.manage_tournament
    
    def matches(self) -> MenuOptions:
        """ Matches screen, choices: input to select match

        Returns:
            MenuOptions: The next menu to navigate to 
        """
        print("HERE COMES A LIST OF MATCHES")
        #TODO: function for user to input to select match to manage
        return MenuOptions.manage_tournament
    
    def match_results(self) -> MenuOptions:
        """ Match results screen, choices: input a match that won

        Returns:
            MenuOptions: The next menu to navigate to 
        """

        print("This is where you choose match results")
        #TODO: function to choose a team that won update the team and match
        return MenuOptions.manage_active_tournament
    
    def manage_inactive_tournament(self) -> MenuOptions:
        """ Inactive tournament screen, choices: 1,2,3 and b

        Returns:
            MenuOptions: The next menu to navigate to 
        """
        print("This is an inactive tournament")
        choice: str = self.__prompt_choice(["1", "2", "3", "b"])
        match choice:
            case "1":
                return MenuOptions.manage_teams
            case "2":
                return MenuOptions.publish
            case "3":
                return MenuOptions.edit_tournament
            case "b":
                return MenuOptions.manage_tournament
        return MenuOptions.manage_tournament
    
    def manage_teams(self) -> MenuOptions:
        """ Manage teams screen, choices: 1,2 and b

        Returns:
            MenuOptions: The next menu to navigate to 
        """
        choice: str = self.__prompt_choice(["1", "2", "b"])
        match choice:
            case "1":
                return MenuOptions.add_team
            case "2":
                return MenuOptions.remove_team
            case "b":
                return MenuOptions.manage_inactive_tournament
        return MenuOptions.manage_inactive_tournament
    
    def add_team(self) -> MenuOptions:
        """ Add team screen, choices: input a team to add or l to list all team

        Returns:
            MenuOptions: The next menu to navigate to 
        """
        print("This is the add team screen")

        #TODO: Add function to list teams and to choose a team by the name
        
        return MenuOptions.manage_teams
    
    def remove_team(self) -> MenuOptions:
        """ Remove team screen, choices: input a team to add or l to list all team

        Returns:
            MenuOptions: The next menu to navigate to 
        """
        print("This is the remove team screen")
        # TODO: same as add team but not remove
        return MenuOptions.manage_teams