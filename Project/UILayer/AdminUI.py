"""
Author: Ísak Elí Hauksson <isak25@ru.is>
Date: 2025-12-04

File that holds all the menus that the admin can access
"""

from Models.Tournament import Tournament

from UILayer.MenuOptions import MenuOptions
from UILayer.UtilityUI import UtilityUI
from UILayer.Drawer import Drawer
from LogicLayer import LogicLayerAPI


class AdminUI:
    """Every admin menu option"""

    def __init__(self) -> None:
        self.utility = UtilityUI()
        self.tui = Drawer()
        self.message_color = "\033[36m"
        self.reset: str = "\033[0m"
        self.underscore = "\033[4m"

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
        options: dict[str, str] = {"c": "Continue"}
        message: str = "You have Created A Tournament!"

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path))
        tournament_name: str = self.utility._input_info(
            "Enter Tournament Name: \n", "handle", "TOURNAMENT"
        )
        self.tui.save_input("Tournament Name: " + tournament_name)

        print(self.tui.table(menu, user_path, info))
        tournament_date: str = self.utility._input_info(
            "Enter Start And End Date: (yyyy-mm-dd yyyy-mm-dd) \n",
            "date",
            "TOURNAMENT",
        )
        self.tui.save_input("Start And End Dates: " + str(tournament_date))

        print(self.tui.table(menu, user_path, info))
        tournament_addr: str = self.utility._input_info(
            "Enter Venue Address: (Streetname 00 Cityname)\n",
            "address",
            "Tournament",
        )
        self.tui.save_input("Venue Address: " + tournament_addr)

        print(self.tui.table(menu, user_path, info))
        tournament_email: str = self.utility._input_info(
            "Enter Contact Email: \n", "email", "PLAYER"
        )
        self.tui.save_input("Email: " + tournament_email)

        print(self.tui.table(menu, user_path, info))
        tournament_phnum: str = self.utility._input_info(
            "Enter Contact Phone Number: 123-4567 \n", "phone_number", "PLAYER"
        )
        self.tui.save_input("Phone Number: " + tournament_phnum)

        LogicLayerAPI.save_player(tournament_name)
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
        info: list[str] = self.utility.show_tournaments_except_status(
            Tournament.StatusType.archived
        )
        options: dict[str, str] = {"t": "Try Again", "b": "Back"}
        message: str = "Tournament Not Found!"

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info))

        find_name: str = input(
            self.message_color + "Input Team Name: " + self.reset
        )
        if find_name.lower() == "lo":
            return MenuOptions.logout

        # Check tournaments that are not archived
        if find_name in self.utility.except_status_tournaments(
            Tournament.StatusType.archived
        ):

            LogicLayerAPI.save_player(find_name)

            # check status to redirect correctly
            tournament = self.utility.get_tournament_object(find_name)
            if tournament == None: 
                return MenuOptions.manage_tournament
            if tournament.status == Tournament.StatusType.active:
                return MenuOptions.manage_active_tournament
            if tournament.status == Tournament.StatusType.inactive:
                return MenuOptions.manage_inactive_tournament

        print(self.tui.table(menu, user_path, info, options, message))

        choice: str = self.utility._prompt_choice(["t", "b"])
        match choice:
            case "t":
                return MenuOptions.manage_tournament

        return MenuOptions.admin_screen

    def manage_active_tournament(self) -> MenuOptions:
        """Active tournament screen, choices: 1,2(c requirement) and b
        1: Select match
        2: (OPTIONAL C Requirement) cancel active tournament
        b: Go back to manage tournaments

        Returns:
            MenuOptions: The next menu to navigate to
        """
        # Get tournament name
        tournament_name: str | None = LogicLayerAPI.save_player()

        menu: str = "Active Tournament"
        user_path: list[str] = [
            MenuOptions.admin_screen,
            MenuOptions.manage_tournament,
            MenuOptions.manage_active_tournament,
        ]
        info: list = [f"- - - - {str(tournament_name)} - - - -"]
        options: dict[str, str] = {
            "1": "Input Results Of A Match",
            "b": "Back",
            "lo": "Log Out",
        }
        message: str = ""

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options))

        choice: str = self.utility._prompt_choice(["1", "b", "lo"])

        match choice:
            case "1":
                return MenuOptions.select_match
            # case "2":
            #     return MenuOptions.cancel_tournament  #TODO: Optional C requirement
            case "b":
                return MenuOptions.manage_tournament

            case "lo":
                MenuOptions.start_screen

        return MenuOptions.manage_tournament

    def matches(self) -> MenuOptions:
        """Matches screen, choices: input to select match

        Returns:
            MenuOptions: The next menu to navigate to
        """

        menu: str = "Matches"
        user_path: list[str] = [
            MenuOptions.admin_screen,
            MenuOptions.manage_tournament,
            MenuOptions.manage_active_tournament,
            MenuOptions.select_match,
        ]
        info: list = ["- - - - List Of Matches - - - -"]
        self.options: dict[str, str] = {}
        choice_list = []
        message: str = ""

        matches_list = [
            "Team 1 vs Team 3",
            "Team 2 vs Team 4",
            "Team 5 vs Team 7",
            "Team 6 vs Team 8",
        ]

        x = 0
        for match in matches_list:
            x += 1
            choice_list.append(str(x))
            self.options[str(x)] = f"Input Results for {match}"
            info.append(match)
        choice_list.append("b")
        self.options["b"] = "Back"

        ## GET NEXT TIME-SLOT
        ## UPDATE MATCH

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, self.options, message))
        self.choice: str = self.utility._prompt_choice(choice_list)

        match self.choice:
            case "b":
                return MenuOptions.manage_active_tournament

        return MenuOptions.input_results

    def match_results(self) -> MenuOptions:
        """Match results screen, choices: input a match that won

        Returns:
            MenuOptions: The next menu to navigate to
        """

        menu: str = "Matches"
        user_path: list[str] = [
            MenuOptions.manage_tournament,
            MenuOptions.manage_active_tournament,
            MenuOptions.select_match,
            MenuOptions.input_results,
        ]
        teamname1, teamname2 = self.options[self.choice].split(" vs ")
        teamname1 = teamname1[18:]
        info: list = ["- - - - List Of Matches - - - -"]
        options: dict[str, str] = {
            "1": f"Select {teamname1} for victory",
            "2": f"Select {teamname2} for victory",
            "b": "Back",
        }

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options))
        choice: str = self.utility._prompt_choice(["1", "2", "b"])

        winner = None

        match choice:
            case "b":
                return MenuOptions.select_match
            case "1":
                winner = teamname1
            case "2":
                winner = teamname2

        options = {"b": "Back"}
        message = f"{winner} Has Won The Round!"

        print(self.tui.table(menu, user_path, info, options, message))
        choice: str = self.utility._prompt_choice(["b"])

        # TODO: function to choose a team that won update the team and match
        return MenuOptions.manage_active_tournament

    def manage_inactive_tournament(self) -> MenuOptions:
        """Inactive tournament screen, choices: 1,2,3 and b

        Returns:
            MenuOptions: The next menu to navigate to
        """
        tournament_name: str | None = LogicLayerAPI.save_player()

        menu: str = "Inactive Tournament"
        user_path: list[str] = [
            MenuOptions.admin_screen,
            MenuOptions.manage_tournament,
            MenuOptions.manage_inactive_tournament,
        ]
        info: list = [f"- - - - {str(tournament_name)} - - - -"]
        options: dict[str, str] = {
            "1": "Manage Teams",
            "2": "Publish",
            "3": "Edit Tournament",
            "b": "Back",
        }
        message = ""

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options))

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

        menu: str = "Inactive Tournament"
        user_path: list[str] = [
            MenuOptions.admin_screen,
            MenuOptions.manage_tournament,
            MenuOptions.manage_inactive_tournament,
            MenuOptions.manage_teams,
        ]
        info: list = ["- - - - List Of Teams In Tournament - - - -"]
        options: dict[str, str] = {
            "1": "Add Team",
            "2": "Remove Team",
            "b": "Back",
        }
        message = ""

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options))

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

        menu: str = "Inactive Tournament"
        user_path: list[str] = [
            MenuOptions.manage_tournament,
            MenuOptions.manage_inactive_tournament,
            MenuOptions.manage_teams,
            MenuOptions.add_team,
        ]
        info: list = []
        options_1: dict[str, str] = {"a": "Add Another Team", "b": "Back"}
        options_2: dict[str, str] = {"t": "Try Again", "b": "Back"}

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info))

        team_to_add: str = input("Enter Team Name or 'l' to list all: \n")

        # if ...: # If Team Found
        #     message = f"You Have Added {team_to_add} To The Tournament"
        #     print(self.tui.table(menu, user_path, info, options_1, message))
        #     choice: str = self.utility._prompt_choice(["a", "b"])

        #     match choice:
        #         case "a":
        #             return MenuOptions.add_team

        #     return MenuOptions.manage_teams

        if ...:  # Team not found
            message = f"{team_to_add} Was Not Found"
            print(self.tui.table(menu, user_path, info, options_2, message))
            choice: str = self.utility._prompt_choice(["t", "b"])

            match choice:
                case "t":
                    return MenuOptions.add_team

            return MenuOptions.manage_teams

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
        choice: str = input("Input tournament to publish: ")
        # TODO: Check for tournament then publish it

        return MenuOptions.manage_inactive_tournament

    def edit_tournament(self) -> MenuOptions:
        """Edit inactive tournament screen,
        choices: input a tournament to edit, then choose to edit time or info

        Returns:
            MenuOptions: The next menu to navigate to
        """
        print("list of inactive tournaments")
        tournament_name: str = input("Choose tournament to edit")

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

        choice = "a"
        while choice.lower() != "y" or choice.lower() != "n":
            choice: str = input("DO YOU WANT TO CONTINUE? Y/N")
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
