"""
Author: Ísak Elí Hauksson <isak25@ru.is>
Date: 2025-12-04

File that holds all the menus that the admin can access
"""

from UILayer.MenuOptions import MenuOptions
from UILayer.UtilityUI import UtilityUI
from UILayer.Drawer import Drawer


class AdminUI:
    """Every admin menu option"""

    def __init__(self) -> None:
        self.utility = UtilityUI()
        self.tui = Drawer()

    def admin_screen(self) -> MenuOptions:
        """Admin screen, choices: 1,2,3 and lo
        1: Go to create tournament screen
        2: Go to manage tournaments screen
        3: Go to create club screen
        lo: Log out of admin and go back to start screen

        Returns:
            MenuOptions: The next menu to navigate to
        """

        menu: str = "Admin Screen"
        user_path: list[str] = [MenuOptions.admin_screen]
        info: list[str] = []
        options: dict[str, str] = {
            "1": "Create Tournament",
            "2": "Manage Tournaments",
            "3": "Create Club",
            "lo": "Log Out",
        }
        message = ""

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options, message))


        choice: str = self.utility._prompt_choice(["1", "2", "3", "lo"])
        match choice:
            case "1":
                return MenuOptions.create_tournament
            case "2":
                return MenuOptions.manage_tournament
            case "3":
                return MenuOptions.create_club
            case "lo":
                return MenuOptions.logout
        return MenuOptions.logout

    def create_tournament(self) -> MenuOptions:
        """Create tournament screen, choices: fill info with input

        Returns:
            MenuOptions: The next menu to navigate to
        """

        menu: str = "Create Tournament"
        user_path: list = [
            MenuOptions.admin_screen,
            MenuOptions.create_tournament,
        ]
        info: list[str] = []
        options: dict[str, str] = {}
        message: str = ""

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options, message))

        tournament_create = Drawer()
        print(tournament_create.table(menu))

        # TODO: add fill in options
        option = input("THIS IS A STOPPER IN CREATE TOURNAMENT")
        return MenuOptions.manage_inactive_tournament

    def manage_tournaments(self) -> MenuOptions:
        """Manage tournaments screen, choices: choose with input

        Returns:
            MenuOptions: The next menu to navigate to
        """
        menu: str = "Manage Tournaments"
        user_path: list[str] = [
            MenuOptions.admin_screen,
            MenuOptions.manage_tournament,
        ]
        info: list[str] = []
        options: dict[str, str] = {"Choose a tournament to manage": ""}
        message: str = ""

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options, message))

        tournament = self.utility._input_info("Input tournament to manage")
        if tournament.lower() == "lo":
            return MenuOptions.logout

        # TODO: add input for tournament to manage
        # TODO: if active the go to active screen else inactive screen
        return MenuOptions.admin_screen

    def manage_active_tournament(self) -> MenuOptions:
        """Active tournament screen, choices: 1,2(c requirement) and b
        1: Select match
        2: (OPTIONAL C Requirement) cancel active tournament
        b: Go back to manage tournaments

        Returns:
            MenuOptions: The next menu to navigate to
        """

        print("This is the active tournaments screen")
        menu: str = "Tournaments"
        user_path: list[str] = [
            MenuOptions.admin_screen,
            MenuOptions.manage_tournament,
            MenuOptions.manage_active_tournament,
        ]
        info: list = []
        options: dict[str, str] = {
            "Enter A Tournaments Name Or The First Letter(s) To Search:": ""
        }
        message: str = ""

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options, message))

        choice: str = self.utility._prompt_choice(["1", "b"])
        match choice:
            case "1":
                return MenuOptions.select_match
            # case "2":
            #     return MenuOptions.cancel_tournament  #TODO: Optional C requirement
            case "b":
                return MenuOptions.manage_tournament
        return MenuOptions.manage_tournament

    def matches(self) -> MenuOptions:
        """Matches screen, choices: input to select match

        Returns:
            MenuOptions: The next menu to navigate to
        """
        print("HERE COMES A LIST OF MATCHES")
        # TODO: function for user to input to select match to manage
        return MenuOptions.manage_tournament

    def match_results(self) -> MenuOptions:
        """Match results screen, choices: input a match that won

        Returns:
            MenuOptions: The next menu to navigate to
        """

        print("This is where you choose match results")
        # TODO: function to choose a team that won update the team and match
        return MenuOptions.manage_active_tournament

    def manage_inactive_tournament(self) -> MenuOptions:
        """Inactive tournament screen, choices: 1,2,3 and b

        Returns:
            MenuOptions: The next menu to navigate to
        """
        print("This is an inactive tournament")
        choice: str = self.utility._prompt_choice(["1", "2", "3", "b"])
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
        """Manage teams screen, choices: 1,2 and b

        Returns:
            MenuOptions: The next menu to navigate to
        """
        choice: str = self.utility._prompt_choice(["1", "2", "b"])
        match choice:
            case "1":
                return MenuOptions.add_team
            case "2":
                return MenuOptions.remove_team
            case "b":
                return MenuOptions.manage_inactive_tournament
        return MenuOptions.manage_inactive_tournament

    def add_team(self) -> MenuOptions:
        """Add team screen, choices: input a team to add or l to list all team

        Returns:
            MenuOptions: The next menu to navigate to
        """
        print("This is the add team screen")

        # TODO: Add function to list teams and to choose a team by the name

        return MenuOptions.manage_teams

    def remove_team(self) -> MenuOptions:
        """Remove team screen, choices: input a team to add or l to list all team

        Returns:
            MenuOptions: The next menu to navigate to
        """
        print("This is the remove team screen")
        # TODO: same as add team but not remove
        return MenuOptions.manage_teams

    def publish(self) -> MenuOptions:
        """Publish tournament screen, choices: input a tournament to publish

        Returns:
            MenuOptions: The next menu to navigate to
        """

        print("PUBLISH TOURNAMENT")
        print("<list of tournaments>")
        choice: str = self.utility._input_info("Input tournament to publish: ")
        # TODO: Check for tournament then publish it

        return MenuOptions.manage_active_tournament

    def edit_tournament(self) -> MenuOptions:
        """Edit inactive tournament screen,
        choices: input a tournament to edit, then choose to edit time or info

        Returns:
            MenuOptions: The next menu to navigate to
        """
        print("list of inactive tournaments")
        tournament_name: str = self.utility._input_info(
            "Choose tournament to edit"
        )

        # TODO: Check for tournament

        print("1. Edit time/date")
        print("2. Edit Info")

        choice: str = self.utility._prompt_choice(["1", "2", "b"])
        match choice:
            case "1":
                return MenuOptions.edit_tournament_time
            case "2":
                return MenuOptions.edit_tournament_info
            case "b":
                return MenuOptions.manage_inactive_tournament
        return MenuOptions.manage_inactive_tournament

    def edit_tournament_time(self) -> MenuOptions:
        """Edit tournament time screen, choices: input a start and end date

        Returns:
            MenuOptions: The next menu to navigate to
        """
        print("THIS is edit tournament time")

        choice: str = self.utility._input_info("DO YOU WANT TO CONTINUE? Y/N")
        match choice:
            case "Y":
                print("YOU CHANGED IT")
                return MenuOptions.edit_tournament
            case "N":
                print("CANCELING")
                return MenuOptions.edit_tournament
        return MenuOptions.edit_tournament

    def edit_tournament_info(self) -> MenuOptions:
        """Edit tournament info screen, choices: input new name, venue,
        email and/or phone number

        Returns:
            MenuOptions: The next menu to navigate to
        """

        print("THIS IS EDIT TOURNAMENT INFO WINDOW")
        return MenuOptions.edit_tournament

    def create_club(self) -> MenuOptions:
        """Create club screen, choices: fill info with input (name and color)

        Returns:
            MenuOptions: The next menu to navigate to
        """

        print("This is the create club screen")
        return MenuOptions.admin_screen
