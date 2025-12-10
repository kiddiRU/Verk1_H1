"""
Author: Ísak Elí Hauksson <isak25@ru.is>
Date: 2025-12-04

File that holds all the menus that the admin can access
"""

from Models.Exceptions import ValidationError
from Models.Tournament import Tournament
from Models.Team import Team
from Models.Match import Match

from UILayer.MenuOptions import MenuOptions
from UILayer.UtilityUI import UtilityUI
from UILayer.Drawer import Drawer
from LogicLayer import LogicLayerAPI

from datetime import date, time


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
        user_path: list[MenuOptions] = [MenuOptions.admin_screen]
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
        # Main info of table
        menu: str = "Create Tournament"
        user_path: list[MenuOptions] = [
            MenuOptions.admin_screen,
            MenuOptions.create_tournament,
        ]
        info: list[str] = []
        options: dict[str, str] = {"c": "Continue", "b": "Back"}
        message: str = "You have Created A Tournament!"

        tournament_name: str = ""
        tournament_date: str = ""
        tournament_time: str = ""
        tournament_addr: str = ""
        tournament_email: str = ""
        tournament_phnum: str = ""

        self.tui.clear_saved_data()

        con = "b"
        while con.lower() == "b":
            print(self.tui.table(menu, user_path, info))
            tournament_name: str = self.utility._input_info(
                "Enter Tournament Name or 'q' to cancel: \n",
                "handle",
                "TOURNAMENT",
            )
            if not tournament_name:
                return MenuOptions.admin_screen

            self.tui.save_input("Name: " + tournament_name)
            print(self.tui.table(menu, user_path, info, options))
            con: str = self.utility._prompt_choice(["c", "b"])
            if con.lower() == "b":
                self.tui.discard_last_input()

        con = "b"
        while con.lower() == "b":
            print(self.tui.table(menu, user_path, info))
            tournament_date: str = self.utility._input_info(
                "Enter Start And End Date or 'q' to cancel: (yyyy-mm-dd yyyy-mm-dd) \n",
                "tournament_date",
                "TOURNAMENT",
            )
            if not tournament_date:
                return MenuOptions.admin_screen

            self.tui.save_input("Start And End Dates: " + tournament_date)
            print(self.tui.table(menu, user_path, info, options))
            con: str = self.utility._prompt_choice(["c", "b"])
            if con.lower() == "b":
                self.tui.discard_last_input()

        con = "b"
        while con.lower() == "b":
            print(self.tui.table(menu, user_path, info))
            tournament_time: str = self.utility._input_info(
                "Enter Start And End Time or 'q' to cancel: (hh:mm hh:mm) \n",
                "tournament_time",
                "TOURNAMENT",
            )
            if not tournament_time:
                return MenuOptions.admin_screen

            self.tui.save_input("Start And End Time: " + tournament_time)
            print(self.tui.table(menu, user_path, info, options))
            con: str = self.utility._prompt_choice(["c", "b"])
            if con.lower() == "b":
                self.tui.discard_last_input()

        con = "b"
        while con.lower() == "b":
            print(self.tui.table(menu, user_path, info))
            tournament_addr: str = self.utility._input_info(
                "Enter Venue Address or 'q' to cancel: (Streetname 00 Cityname)\n",
                "home_address",
                "TOURNAMENT",
            )
            if not tournament_addr:
                return MenuOptions.admin_screen

            self.tui.save_input("Venue Address: " + tournament_addr)
            print(self.tui.table(menu, user_path, info, options))
            con: str = self.utility._prompt_choice(["c", "b"])
            if con.lower() == "b":
                self.tui.discard_last_input()

        con = "b"
        while con.lower() == "b":
            print(self.tui.table(menu, user_path, info))
            tournament_email: str = self.utility._input_info(
                "Enter Contact Email or 'q' to cancel: \n", "email", "PLAYER"
            )
            if not tournament_email:
                return MenuOptions.admin_screen

            self.tui.save_input("Email: " + tournament_email)
            print(self.tui.table(menu, user_path, info, options))
            con: str = self.utility._prompt_choice(["c", "b"])
            if con.lower() == "b":
                self.tui.discard_last_input()

        con = "b"
        while con.lower() == "b":
            print(self.tui.table(menu, user_path, info))
            tournament_phnum: str = self.utility._input_info(
                "Enter Contact Phone Number or 'q' to cancel: 123-4567 \n",
                "phone_number",
                "PLAYER",
            )
            if not tournament_phnum:
                return MenuOptions.admin_screen

            self.tui.save_input("Phone Number: " + tournament_phnum)
            print(self.tui.table(menu, user_path, info, options))
            con: str = self.utility._prompt_choice(["c", "b"])
            if con.lower() == "b":
                self.tui.discard_last_input()

        options: dict[str, str] = {
            "c": "Save Info And Continue",
            "b": "Discard Info And Go Back",
        }
        print(self.tui.table(menu, user_path, info, options, message))
        con: str = self.utility._prompt_choice(["c", "b"])

        if con.lower() == "b":
            return MenuOptions.admin_screen

        date_start, date_end = tournament_date.split()
        time_start, time_end = tournament_time.split()

        start_date: date = LogicLayerAPI.to_date(date_start)
        end_date: date = LogicLayerAPI.to_date(date_end)
        time_frame_start: time = LogicLayerAPI.to_time(time_start)
        time_frame_end: time = LogicLayerAPI.to_time(time_end)

        LogicLayerAPI.create_tournament(
            tournament_name,
            start_date,
            end_date,
            time_frame_start,
            time_frame_end,
            tournament_addr,
            tournament_email,
            tournament_phnum,
        )

        LogicLayerAPI.save_player(tournament_name)

        return MenuOptions.manage_inactive_tournament

    def manage_tournaments(self) -> MenuOptions:
        """Manage tournaments screen, choices: choose with input

        Returns:
            MenuOptions: The next menu to navigate to
        """

        menu: str = "Manage Tournaments"
        user_path: list[MenuOptions] = [
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
            self.message_color + "Input Tournament Name or 'q' to go back: \n" + self.reset
        )
        if find_name.lower() == "q":
            return user_path[-2]
        if find_name.lower() == "lo":
            return MenuOptions.logout

        # Check tournaments that are not archived
        if find_name in self.utility.except_status_tournaments(
            Tournament.StatusType.archived
        ):

            LogicLayerAPI.save_player(find_name)

            tournament_object: Tournament | None = (
                LogicLayerAPI.get_tournament_by_name(find_name)
            )

            # check status to redirect correctly
            tournament = tournament_object
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
        if tournament_name is None:  # For type hinting
            return MenuOptions.start_screen

        # Get tournament object
        tournament_object: Tournament | None = (
            LogicLayerAPI.get_tournament_by_name(tournament_name)
        )
        if tournament_object is None:  # Check if None goes through
            return MenuOptions.start_screen

        # Get tournament uuid
        tournament_uuid: str = tournament_object.uuid

        menu: str = "Active Tournament"
        user_path: list[MenuOptions] = [
            MenuOptions.admin_screen,
            MenuOptions.manage_tournament,
            MenuOptions.manage_active_tournament,
        ]
        info: list[str] = [f"{f"- - - - {str(tournament_name)} - - - -": <79}" + "|"]
        options: dict[str, str] = {
            "1": "Input Results Of A Match",
            "b": "Back",
            "lo": "Log Out",
        }

        matches = self.utility.list_matches(tournament_uuid, True)

        ammount_of_lines = len(matches) - 1
        for match in matches:
            info.append(match)

            # for line in range(ammount_of_lines):
            #     info.append("—" * 80)
            #     ammount_of_lines -= 1

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options))

        choice: str = self.utility._prompt_choice(["1", "b", "lo"])

        if choice == "1":
            return MenuOptions.select_match
        if choice == "lo":
            return MenuOptions.start_screen

        return MenuOptions.admin_screen

    def matches(self) -> MenuOptions:
        """Matches screen, choices: input to select match

        Returns:
            MenuOptions: The next menu to navigate to
        """
        # Get tournament name
        tournament_name: str | None = LogicLayerAPI.save_player()
        if tournament_name is None:  # For type hinting
            return MenuOptions.start_screen

        # Get tournament object
        tournament_object: Tournament | None = (
            LogicLayerAPI.get_tournament_by_name(tournament_name)
        )

        # Get tournament uuid
        tournament_uuid: str = tournament_object.uuid
    

        # Menu and path for the table
        menu: str = "Matches"
        user_path: list[MenuOptions] = [
            MenuOptions.admin_screen,
            MenuOptions.manage_tournament,
            MenuOptions.manage_active_tournament,
            MenuOptions.select_match,
        ]
        # # Gets the whole team vs team string
        # match_list: list[str] = self.utility.list_matches(tournament_uuid, False)
        # match_string: str = "".join(match_list)

        # # Splits the string
        # lines: list[str] = match_string.splitlines()

        # # Filter out the name of the teams
        # match_name_1 = lines[1].replace("Team 1: ", "").rstrip("|")
        # match_name_2 = lines[3].replace("Team 2: ", "").rstrip("|")

        # match_name_1 = match_name_1.strip()
        # match_name_2 = match_name_2.strip()

        info: list[str] = ["- - - - List Of Matches - - - -"]
        self.options: dict[str, str] = {}
        choice_list = []
        message: str = ""

        # Show a list of the matches in the round
        matches: list[str] = self.utility.list_matches(tournament_uuid, True)

        ammount_of_lines = len(matches) -1

        x = 0
        for match in matches:
            info.append(match)
            x += 1
            choice_list.append(str(x))
            match = match[243:-81]
            self.options[str(x)] = f"{"Input Results for:":<77}| \n{match}"
            self.options[("—" * 80)] = ""
            ammount_of_lines -= 1

        self.options[("—" * 80) + " "] = ""
        choice_list.append("b")
        self.options["b"] = "Back"

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
        user_path: list[MenuOptions] = [
            MenuOptions.manage_tournament,
            MenuOptions.manage_active_tournament,
            MenuOptions.select_match,
            MenuOptions.input_results,
        ]

        # Gets the whole team vs team string
        match_string: str = self.options[self.choice]

        # Splits the string
        lines: list[str] = match_string.splitlines()

        # Filter out the name of the teams
        match_team_1: str = lines[1].replace("Team 1: ", "").rstrip("|")
        match_team_2: str = lines[3].replace("Team 2: ", "").rstrip("|")

        match_team_1 = match_team_1.strip()
        match_team_2 = match_team_2.strip()
        
        # Screen to print
        info: list = ["- - - - List Of Matches - - - -"]
        options: dict[str, str] = {
            "1": f"Select {match_team_1} for victory",
            "2": f"Select {match_team_2} for victory",
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
                winner = match_team_1
            case "2":
                winner = match_team_2

        options = {"b": "Back"}
        message = f"{winner} Has Won The Round!"

        tournament_name: str | None = LogicLayerAPI.save_player()
        team1 = LogicLayerAPI.get_team_by_name(match_team_1)
        team2 = LogicLayerAPI.get_team_by_name(match_team_2)

        team1_uuid = team1.uuid
        team2_uuid = team2.uuid

        if type(tournament_name) is str:
            current_tournament: Tournament = LogicLayerAPI.get_tournament_by_name(tournament_name)
            tournament_id: str = current_tournament.uuid

            current_match: Match | str = LogicLayerAPI.get_match(tournament_id, team1_uuid, team2_uuid)
            if type(current_match) is Match:
                match_uuid: str = current_match.uuid
                if winner is not None:
                    winner_team: Team = LogicLayerAPI.get_team_by_name(winner)

                    LogicLayerAPI.change_match_winner(tournament_id, match_uuid, winner)

        print(self.tui.table(menu, user_path, info, options, message))
        choice: str = self.utility._prompt_choice(["b"])

        # TODO: function to choose a team that won update the team and match
        return MenuOptions.manage_active_tournament

    def manage_inactive_tournament(self) -> MenuOptions:
        """Inactive tournament screen, choices: 1,2,3 and b

        Returns:
            MenuOptions: The next menu to navigate to
        """
        tournament_name: str | None = LogicLayerAPI.save_player() or "None"
        tournament_object: Tournament | None = (
            LogicLayerAPI.get_tournament_by_name(tournament_name)
        )
        amount_teams = len(tournament_object.teams_playing)

        menu: str = "Inactive Tournament"
        user_path: list[MenuOptions] = [
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
            "lo": "Log Out",
        }

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options))

        choice: str = self.utility._prompt_choice(["1", "2", "3", "b", "lo"])

        match choice:
            case "1":
                return MenuOptions.manage_teams
            case "2":
                if (
                    amount_teams > 1
                ):  # To stop from going to publish if tournament is too small
                    return MenuOptions.publish
                else:
                    print(
                        "There Need To 2 Or More Teams In A Tournament To Publish."
                    )
                    input("Input Anything To Continue")
                    return MenuOptions.manage_inactive_tournament
            case "3":
                return MenuOptions.edit_tournament
            case "b":
                return MenuOptions.admin_screen
            case "lo":
                return MenuOptions.logout
        return MenuOptions.manage_tournament

    def manage_teams(self) -> MenuOptions:
        """Manage teams screen, choices: 1,2 and b

        Returns:
            MenuOptions: The next menu to navigate to
        """

        # Keep the tournament name from previous screen
        tournament_name: str = LogicLayerAPI.save_player() or "None"

        # Get tournament Object from name
        teams_in_tournament: list[str] = [
            t.name
            for t in LogicLayerAPI.get_teams_from_tournament_name(
                tournament_name
            )
        ]

        tournament_object: Tournament | None = (
            LogicLayerAPI.get_tournament_by_name(tournament_name)
        )
        if tournament_object is None:  # Check if None goes through
            return MenuOptions.start_screen

        menu: str = "Manage Teams"
        user_path: list[MenuOptions] = [
            MenuOptions.admin_screen,
            MenuOptions.manage_tournament,
            MenuOptions.manage_inactive_tournament,
            MenuOptions.manage_teams,
        ]

        info: list = teams_in_tournament
        options: dict[str, str] = {
            "1": "Add Team",
            "2": "Remove Team",
            "b": "Back",
        }

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
        # Tournament data
        tournament_name: str = LogicLayerAPI.save_player() or "None"
        teams_in_tournament: list[str] = [
            t.name
            for t in LogicLayerAPI.get_teams_from_tournament_name(
                tournament_name
            )
        ]
        all_teams: list[str] = self.utility.team_names()

        menu: str = f"Add Team To {tournament_name}"
        user_path: list[MenuOptions] = [
            MenuOptions.manage_tournament,
            MenuOptions.manage_inactive_tournament,
            MenuOptions.manage_teams,
            MenuOptions.add_team,
        ]

        info: list = self.utility.show_main(
            "teams"
        )  # TODO Make it so that only teams not already internment show upp
        options: dict[str, str] = {"t": "Try Again", "b": "Back"}

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info))

        team_to_add: str = input(
            self.message_color + "Input Team Name: " + self.reset
        )

        # Validate team exists
        try:
            team_object: Team | None = LogicLayerAPI.get_team_by_name(
                team_to_add
            )
        except Exception:
            team_object = None

        if team_object is None:
            message = "Team Not Found"
            print(self.tui.table(menu, user_path, info, options, message))
            choice: str = self.utility._prompt_choice(["t", "b"])

            match choice:
                case "t":
                    return MenuOptions.add_team

            return MenuOptions.manage_teams

        if team_to_add in teams_in_tournament:
            message = f"{team_to_add} Is Already In {tournament_name}"

        elif not (3 <= len(team_object.list_player_uuid) <= 5):
            message = f"{team_to_add} Must Have Between 3 And 5 Players"

        elif team_to_add not in all_teams:
            message = f"{team_to_add} Is Not A Valid Team"

        else:
            LogicLayerAPI.add_team(tournament_name, team_to_add)
            message: str = f"{team_to_add} Was Added To {tournament_name}"
            options: dict[str, str] = {"t": "Add Another", "b": "Back"}

        print(self.tui.table(menu, user_path, info, options, message))
        choice: str = self.utility._prompt_choice(["t", "b"])

        match choice:
            case "t":
                return MenuOptions.add_team

        return MenuOptions.manage_teams

    def remove_team(self) -> MenuOptions:
        # Tournament data
        tournament_name: str = LogicLayerAPI.save_player() or "None"

        # Get tournament Object from name
        teams_in_tournament: list[str] = [
            t.name
            for t in LogicLayerAPI.get_teams_from_tournament_name(
                tournament_name
            )
        ]

        menu: str = f"Add Team To {tournament_name}"
        user_path: list[MenuOptions] = [
            MenuOptions.manage_tournament,
            MenuOptions.manage_inactive_tournament,
            MenuOptions.manage_teams,
            MenuOptions.remove_team,
        ]

        info: list = teams_in_tournament
        options: dict[str, str] = {"t": "Try Again", "b": "Back"}

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info))

        team_to_add: str = input(
            self.message_color + "Input Team Name: " + self.reset
        )

        # Validate team exists
        try:
            team_object: Team | None = LogicLayerAPI.get_team_by_name(
                team_to_add
            )
        except Exception:
            team_object = None

        if team_object is None:
            message = "Team Not Found"
            print(self.tui.table(menu, user_path, info, options, message))
            choice: str = self.utility._prompt_choice(["t", "b"])

            match choice:
                case "t":
                    return MenuOptions.remove_team

            return MenuOptions.manage_teams

        if team_to_add in teams_in_tournament:
            LogicLayerAPI.remove_team(tournament_name, team_to_add)
            message: str = f"{team_to_add} Was Removed From {tournament_name}"
            options: dict[str, str] = {"t": "Remove Another", "b": "Back"}
        else:
            message = f"{team_to_add} Is Not A Valid Team"

        print(self.tui.table(menu, user_path, info, options, message))
        choice: str = self.utility._prompt_choice(["t", "b"])

        match choice:
            case "t":
                return MenuOptions.remove_team

        return MenuOptions.manage_teams

    def publish(self) -> MenuOptions:
        """Publish tournament screen, choices: input a tournament to publish

        Returns:
            MenuOptions: The next menu to navigate to
        """
        # Check if None goes through
        tournament_name = LogicLayerAPI.save_player() or "None"
        tournament_object: Tournament | None = (
            LogicLayerAPI.get_tournament_by_name(tournament_name)
        )

        if tournament_object is None:
            return MenuOptions.start_screen

        menu: str = "Publish"
        user_path: list[MenuOptions] = [
            MenuOptions.manage_tournament,
            MenuOptions.manage_inactive_tournament,
            MenuOptions.publish,
        ]
        info: list = [
            f"Do you want to publish {self.message_color}{tournament_object.name}{self.reset}? Y/N"
        ]

        options: dict[str, str] = {
            "Y:": "Yes",
            "N:": "No",
        }
        message = "Publishing cannot be reverted!"

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options, message))

        choice: str = self.utility._prompt_choice(["Y", "y", "N", "n"])

        if choice.lower() == "y":
            try:
                LogicLayerAPI.publish(tournament_name)
                return MenuOptions.manage_tournament
            except ValidationError as ex:
                input(f"Error: {ex} \nInput anything to go back")

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
    
    # Created by Sindri
    def create_club(self) -> MenuOptions:
        """Create club screen, choices: fill info with input (name and color)

        Returns:
            MenuOptions: The next menu to navigate to
        """

        # print("This is the create club screen")
        menu: str = "Create club"
        user_path: list[MenuOptions] = [
            MenuOptions.admin_screen,
            MenuOptions.create_club,
        ]
        info: list[str] = []
        options: dict[str, str] = {"c": "Continue", "b": "Back"}
        message: str = "You Have Created A Club!"

        # Python complained if i did not do this
        club_name = ""
        club_color = ""
        club_country = ""
        club_hometown = ""

        self.tui.clear_saved_data()

        con = "b"
        while con == "b":
            print(self.tui.table(menu, user_path, info))
            club_name: str = self.utility._input_info(
                "Enter Name or 'q' to cancel: \n", "handle", "CLUB"
            )
            if not club_name:
                return user_path[-2]
            self.tui.save_input("Club Name: " + club_name)

            print(self.tui.table(menu, user_path, info, options))
            con: str = self.utility._prompt_choice(["c", "b"])
            if con == "b":
                self.tui.discard_last_input()

        con = "b"
        while con == "b":
            print(self.tui.table(menu, user_path, info))
            club_color: str = str(
                self.utility._input_info(
                    "Enter Basic color or 'q' to cancel: \n", "color", "CLUB"
                )
            )
            if not club_color:
                return user_path[-2]
            self.tui.save_input("Club Color: " + str(club_color))

            print(self.tui.table(menu, user_path, info, options))
            con: str = self.utility._prompt_choice(["c", "b"])
            if con == "b":
                self.tui.discard_last_input()

        con = "b"
        while con == "b":
            print(self.tui.table(menu, user_path, info))
            club_country: str = self.utility._input_info(
                "Enter Club country of origin or 'q' to cancel: \n",
                "name",
                "CLUB",
            )
            if not club_country:
                return user_path[-2]
            self.tui.save_input("Club Country: " + club_country)

            print(self.tui.table(menu, user_path, info, options))
            con: str = self.utility._prompt_choice(["c", "b"])
            if con == "b":
                self.tui.discard_last_input()

        con = "b"
        while con == "b":
            print(self.tui.table(menu, user_path, info))
            club_hometown: str = self.utility._input_info(
                "Enter Club Hometown or 'q' to cancel: \n", "name", "CLUB"
            )
            if not club_hometown:
                return user_path[-2]
            self.tui.save_input("Club Hometown: " + club_hometown)

            print(self.tui.table(menu, user_path, info, options))
            con: str = self.utility._prompt_choice(["c", "b"])
            if con == "b":
                self.tui.discard_last_input()
        # Club input done
        options: dict[str, str] = {
            "c": "Save Info And Continue",
            "b": "Discard Info And Go Back",
        }
        print(self.tui.table(menu, user_path, info, options, message))
        con: str = self.utility._prompt_choice(["c", "b"])

        if con == "b":
            return MenuOptions.admin_screen

        LogicLayerAPI.create_club(
            club_name, club_color, club_country, club_hometown
        )
        return MenuOptions.admin_screen
