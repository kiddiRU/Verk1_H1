"""
Author: Ísak Elí Hauksson <isak25@ru.is>
Date: 2025-12-04
Co-author: Andri Már Kristjá.nsson <andrik25@ru.is>

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
        1: go to login screen
        2: go to register screen
        3: go to spectating page
        1: quit program

        Returns:
            MenuOptions: The next menu to navigate to
        """
        menu: list = "Start Page"
        user_path: list = ["StartPage"]
        info: list = []
        options: dict = {1: "Log in", 2: "Register", 3: "Spectate", "q": "Quit program"}
        message: str = ""

        tui = Drawer()
        print(tui.table(menu, user_path, info, options, message))  


        choice: str = self.utility._prompt_choice(["1", "2", "3", "q"])
        match choice:
            case "1":
                return MenuOptions.login
            case "2":
                return MenuOptions.register
            case "3":
                return MenuOptions.spectate_screen
            case "q":
                return MenuOptions.quit

        return MenuOptions.main_menu

    def login_screen(self) -> MenuOptions:
        """Login screen, choices: fill info with input

        Returns:
            MenuOptions: The next menu to navigate to
        """

        menu: list = "Login"
        user_path: list = ["StartPage", "Login"]
        info: list = []
        options: dict = {}
        message: str = ""

        tui = Drawer()
        print(tui.table(menu, user_path, info, options, message))        

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
        
        menu: list = "Register"
        user_path: list = ["StartPage", "Login", "Register"]
        info: list = []
        options: dict = {"c": "Continue"}
        message: str = "You Have Created A User"

        tui = Drawer()
        print(tui.table(menu, user_path, info))  
        choice_name: str = input("Enter Name: \n")
        tui.save_input("Name: " + choice_name)
        print(tui.table(menu, user_path, info, options, message))  

        print(tui.table(menu, user_path, info)) 
        choice_dob: str = input("Enter Date Of Birth: \n")
        tui.save_input("Date Of Birth: " + choice_dob)
        print(tui.table(menu, user_path, info, options, message))  

        print(tui.table(menu, user_path, info)) 
        choice_addr: str = input("Enter Home Adderess: \n")
        tui.save_input("Home Address: " + choice_addr)
        print(tui.table(menu, user_path, info, options, message))  

        print(tui.table(menu, user_path, info))
        choice_email: str = input("Enter Email: \n")
        tui.save_input("Email: " + choice_email)
        print(tui.table(menu, user_path, info, options, message))  

        print(tui.table(menu, user_path, info))   
        choice_pnum: str = input("Enter Phone Number: \n")
        tui.save_input("Phone Number: " + choice_pnum)
        print(tui.table(menu, user_path, info, options, message))  

        print(tui.table(menu, user_path, info))   
        choice_handle: str = input("Enter Handle: \n")
        tui.save_input("Handle: " + choice_handle)
        print(tui.table(menu, user_path, info, options, message))  

        
        #if register
        return MenuOptions.player_page
        #if cancel: return MenuOptions.main_menu

    def player_page(self) -> MenuOptions:
        """Player page, choices: 1,2,3 and b
        1: Edit info
        2: See team
        3: Create a team
        b: back to main menu

        Returns:
            MenuOptions: The next menu to navigate to
        """
        

        menu: list = "Player Page"
        user_path: list = ["StartPage", "PlayerPage"]
        info: list = []
        options: dict = {"c": "Continue"}
        message: str = "You Have Created A User"



        choice: str = self.utility._prompt_choice(["1", "2", "3", "q"])
        match choice:
            case "1":
                return MenuOptions.edit_player_info
            case "2":
                if ...:  # TODO: check if team is empty aka if player not in a team
                    return MenuOptions.my_team_not_empty
                else:
                    return MenuOptions.my_team_empty
            case "3":
                if ...:  # TODO: check if player is already in a team
                    print("You are already in a team")
                    return MenuOptions.player_page
                return MenuOptions.create_team
            case "q":
                return MenuOptions.quit


        return MenuOptions.main_menu
    
    def create_team(self) -> MenuOptions:
        """Create team screen, choices: fill info with input

        Returns:
            MenuOptions: The next menu to navigate to
        """
        print("This is the create team page")
        return MenuOptions.player_page

    def edit_player_info(self) -> MenuOptions:
        """Edit player info screen, choices: fill info with input

        Returns:
            MenuOptions: The next menu to navigate to
        """
        print("This is the edit player info page")
        return MenuOptions.player_page
    
    def my_team_empty(self) -> MenuOptions:
        """My team screen when team is empty, choices: b to go back

        Returns:
            MenuOptions: The next menu to navigate to
        """
        print("You are not in a team")
        choice: str = self.utility._prompt_choice(["b"])
        match choice:
            case "b":
                return MenuOptions.player_page
        return MenuOptions.player_page
    
    def my_team_not_empty(self) -> MenuOptions:
        """My team screen when team is not empty, choices: 1,2 and b
        1: edit team
        2: leave team
        b: back to player page

        Returns:
            MenuOptions: The next menu to navigate to
        """
        print("This is your team page")
        choice: str = self.utility._prompt_choice(["1", "2", "b"])
        match choice:
            case "1":
                return MenuOptions.edit_team
            case "2":
                if ...:  # TODO: check if player is captain
                    return MenuOptions.leave_team
            case "b":
                return MenuOptions.my_team_not_empty
        return MenuOptions.player_page
    
    def edit_team(self) -> MenuOptions:
        """Edit team screen, choices: 1,2 and b
        1: Add player to team
        2: Remove player from team
        b: back to My Team

        Returns:
            MenuOptions: The next menu to navigate to
        """
        print("This is the edit team page")
        return MenuOptions.my_team_not_empty
    
    def add_player(self) -> MenuOptions:
        """Add player to team screen, choices: input player handle to add

        Returns:
            MenuOptions: The next menu to navigate to
        """
        print("This is the add player to team page")
        return MenuOptions.edit_team
    
    def remove_player(self) -> MenuOptions:
        """Remove player from team screen, choices: input player handle to remove

        Returns:
            MenuOptions: The next menu to navigate to
        """
        print("This is the remove player from team page")
        return MenuOptions.edit_team
    
    def leave_team(self) -> MenuOptions:
        """Leave team screen, choices: confirm leaving team with y or n and if captain then choose new captain

        Returns:
            MenuOptions: The next menu to navigate to
        """
        print("This is the leave team page")
        if ...:  # TODO: check if player is captain
            print("You are the captain, please choose a new captain before leaving")

        return MenuOptions.player_page