"""
Author: Ísak Elí Hauksson <isak25@ru.is>
Date: 2025-12-04

File that holds all the menus that the admin can access
"""

from datetime import date, time

from LogicLayer import LogicLayerAPI
from Models.Exceptions import ValidationError
from Models.Match import Match
from Models.Team import Team
from Models.Tournament import Tournament

from UILayer.Drawer import Drawer
from UILayer.MenuOptions import MenuOptions
from UILayer.UtilityUI import UtilityUI


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
        user_path: list[MenuOptions] = [MenuOptions.ADMIN_SCREEN]
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

        choice: str = self.utility.prompt_choice(["1", "2", "3", "lo"])
        match choice:
            case "1":
                return MenuOptions.CREATE_TOURNAMENT
            case "2":
                return MenuOptions.MANAGE_TOURNAMENT
            case "3":
                return MenuOptions.CREATE_CLUB
            case "lo":
                return MenuOptions.LOGOUT
        return MenuOptions.LOGOUT

    def create_tournament(self) -> MenuOptions:
        """Create tournament screen, choices: fill info with input

        Returns:
            MenuOptions: The next menu to navigate to
        """
        # Main info of table
        menu: str = "Create Tournament"
        user_path: list[MenuOptions] = [
            MenuOptions.ADMIN_SCREEN,
            MenuOptions.CREATE_TOURNAMENT,
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
        tournament_servers: str = ""

        self.tui.clear_saved_data()

        con = "b"
        while con.lower() == "b":
            print(self.tui.table(menu, user_path, info))
            tournament_name: str = self.utility.input_info(
                "Enter Tournament Name or 'q' to cancel: \n",
                "handle",
                "TOURNAMENT",
            )
            if not tournament_name:
                return MenuOptions.ADMIN_SCREEN

            self.tui.save_input("Name: " + tournament_name)
            print(self.tui.table(menu, user_path, info, options))
            con: str = self.utility.prompt_choice(["c", "b"])
            if con.lower() == "b":
                self.tui.discard_last_input()

        con = "b"
        while con.lower() == "b":
            print(self.tui.table(menu, user_path, info))
            tournament_date: str = self.utility.input_info(
                "Enter Start And End Date or 'q' to cancel: (yyyy-mm-dd yyyy-mm-dd) \n",
                "tournament_date",
                "TOURNAMENT",
            )
            if not tournament_date:
                return MenuOptions.ADMIN_SCREEN

            self.tui.save_input("Start And End Dates: " + tournament_date)
            print(self.tui.table(menu, user_path, info, options))
            con: str = self.utility.prompt_choice(["c", "b"])
            if con.lower() == "b":
                self.tui.discard_last_input()

        con = "b"
        while con.lower() == "b":
            print(self.tui.table(menu, user_path, info))
            tournament_time: str = self.utility.input_info(
                "Enter Start And End Time or 'q' to cancel: (hh:mm hh:mm) \n",
                "tournament_time",
                "TOURNAMENT",
            )
            if not tournament_time:
                return MenuOptions.ADMIN_SCREEN

            self.tui.save_input("Start And End Time: " + tournament_time)
            print(self.tui.table(menu, user_path, info, options))
            con: str = self.utility.prompt_choice(["c", "b"])
            if con.lower() == "b":
                self.tui.discard_last_input()

        con = "b"
        while con.lower() == "b":
            print(self.tui.table(menu, user_path, info))
            tournament_addr: str = self.utility.input_info(
                "Enter Venue Address or 'q' to cancel: (Streetname 00 Cityname)\n",
                "home_address",
                "TOURNAMENT",
            )
            if not tournament_addr:
                return MenuOptions.ADMIN_SCREEN

            self.tui.save_input("Venue Address: " + tournament_addr)
            print(self.tui.table(menu, user_path, info, options))
            con: str = self.utility.prompt_choice(["c", "b"])
            if con.lower() == "b":
                self.tui.discard_last_input()

        con = "b"
        while con.lower() == "b":
            print(self.tui.table(menu, user_path, info))
            tournament_email: str = self.utility.input_info(
                "Enter Contact Email or 'q' to cancel: \n", "email", "PLAYER"
            )
            if not tournament_email:
                return MenuOptions.ADMIN_SCREEN

            self.tui.save_input("Email: " + tournament_email)
            print(self.tui.table(menu, user_path, info, options))
            con: str = self.utility.prompt_choice(["c", "b"])
            if con.lower() == "b":
                self.tui.discard_last_input()

        con = "b"
        while con.lower() == "b":
            print(self.tui.table(menu, user_path, info))
            tournament_phnum: str = self.utility.input_info(
                "Enter Contact Phone Number or 'q' to cancel: 123-4567 \n",
                "phone_number",
                "PLAYER",
            )
            if not tournament_phnum:
                return MenuOptions.ADMIN_SCREEN

            self.tui.save_input("Phone Number: " + tournament_phnum)
            print(self.tui.table(menu, user_path, info, options))
            con: str = self.utility.prompt_choice(["c", "b"])
            if con.lower() == "b":
                self.tui.discard_last_input()

        con = "b"
        while con.lower() == "b":
            print(self.tui.table(menu, user_path, info))
            tournament_servers: str = self.utility.input_info(
                "Enter Amount of Servers or 'q' to cancel (1-8 servers allowed)\n",
                "number",
                "",
            )
            if not tournament_servers:
                return MenuOptions.ADMIN_SCREEN

            self.tui.save_input("Amount Of Servers: " + tournament_servers)
            print(self.tui.table(menu, user_path, info, options))
            con: str = self.utility.prompt_choice(["c", "b"])
            if con.lower() == "b":
                self.tui.discard_last_input()

        options: dict[str, str] = {
            "c": "Save Info And Continue",
            "b": "Discard Info And Go Back",
        }
        print(self.tui.table(menu, user_path, info, options, message))
        con: str = self.utility.prompt_choice(["c", "b"])

        if con.lower() == "b":
            return MenuOptions.ADMIN_SCREEN

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
            int(tournament_servers),
        )

        LogicLayerAPI.save_player(tournament_name)

        return MenuOptions.MANAGE_INACTIVE_TOURNAMENT

    def manage_tournaments(self) -> MenuOptions:
        """Manage tournaments screen, choices: choose with input

        Returns:
            MenuOptions: The next menu to navigate to
        """

        menu: str = "Manage Tournaments"
        user_path: list[MenuOptions] = [
            MenuOptions.ADMIN_SCREEN,
            MenuOptions.MANAGE_TOURNAMENT,
        ]
        info: list[str] = self.utility.show_tournaments_except_status(
            Tournament.StatusType.archived
        )
        options: dict[str, str] = {"t": "Try Again", "b": "Back"}
        message: str = "Tournament Not Found!"

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info))

        find_name: str = input(
            self.message_color
            + "Input Tournament Name or 'q' to go back: \n"
            + self.reset
        )
        if find_name.lower() == "q":
            return user_path[-2]
        if find_name.lower() == "lo":
            return MenuOptions.LOGOUT

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
            if tournament is None:
                return MenuOptions.MANAGE_TOURNAMENT
            if tournament.status == Tournament.StatusType.active:
                return MenuOptions.MANAGE_ACTIVE_TOURNAMENT
            if tournament.status == Tournament.StatusType.inactive:
                return MenuOptions.MANAGE_INACTIVE_TOURNAMENT

        print(self.tui.table(menu, user_path, info, options, message))

        choice: str = self.utility.prompt_choice(["t", "b"])
        match choice:
            case "t":
                return MenuOptions.MANAGE_TOURNAMENT

        return MenuOptions.ADMIN_SCREEN

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
            return MenuOptions.START_SCREEN

        # Get tournament object
        tournament_object: Tournament | None = (
            LogicLayerAPI.get_tournament_by_name(tournament_name)
        )
        if tournament_object is None:  # Check if None goes through
            return MenuOptions.START_SCREEN

        # Get tournament uuid
        tournament_uuid: str = tournament_object.uuid

        menu: str = "Active Tournament"
        user_path: list[MenuOptions] = [
            MenuOptions.ADMIN_SCREEN,
            MenuOptions.MANAGE_TOURNAMENT,
            MenuOptions.MANAGE_ACTIVE_TOURNAMENT,
        ]
        info: list[str] = [
            f"{f'- - - - {str(tournament_name)} - - - -': <79}" + "|"
        ]
        options: dict[str, str] = {
            "1": "Input Results Of A Match",
            "b": "Back",
            "lo": "Log Out",
        }

        matches = self.utility.list_matches(tournament_uuid, True)

        for match in matches:
            info.append(match)

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options))

        choice: str = self.utility.prompt_choice(["1", "b", "lo"])

        if choice == "1":
            return MenuOptions.SELECT_MATCH
        if choice == "lo":
            return MenuOptions.START_SCREEN

        return MenuOptions.ADMIN_SCREEN

    def matches(self) -> MenuOptions:
        """Matches screen, choices: input to select match

        Returns:
            MenuOptions: The next menu to navigate to
        """
        # Get tournament name
        tournament_name: str | None = LogicLayerAPI.save_player()
        if tournament_name is None:  # For type hinting
            return MenuOptions.START_SCREEN

        # Get tournament object
        tournament_object: Tournament | None = (
            LogicLayerAPI.get_tournament_by_name(tournament_name)
        )

        # Get tournament uuid
        tournament_uuid: str = tournament_object.uuid

        # Menu and path for the table
        menu: str = "Matches"
        user_path: list[MenuOptions] = [
            MenuOptions.ADMIN_SCREEN,
            MenuOptions.MANAGE_TOURNAMENT,
            MenuOptions.MANAGE_ACTIVE_TOURNAMENT,
            MenuOptions.SELECT_MATCH,
        ]

        self.options: dict[str, str] = {}
        choice_list = []
        message: str = ""

        # Show a list of the matches in the round
        matches: list[str] = self.utility.list_matches(tournament_uuid, False)

        amount_of_lines = len(matches) - 1

        x = 0
        for match in matches:
            x += 1
            choice_list.append(str(x))
            match = match[243:-81]
            self.options[str(x)] = (
                f"{'Input Results for:':<77}|\n{match}\n{'—' * 80}"
            )

            amount_of_lines -= 1

        # When the tournament is over takes the user to Admin Screen
        if not self.options:
            self.tui.clear_saved_data()
            print(self.tui.table(menu, user_path, [], self.options, message))
            input("The Tournament Is Over")
            return MenuOptions.ADMIN_SCREEN

        choice_list.append("b")
        self.options["b"] = "Back"

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, [], self.options, message))
        self.choice: str = self.utility.prompt_choice(choice_list)

        match self.choice:
            case "b":
                return MenuOptions.MANAGE_ACTIVE_TOURNAMENT

        return MenuOptions.INPUT_RESULTS

    def match_results(self) -> MenuOptions:
        """Match results screen, choices: input a match that won

        Returns:
            MenuOptions: The next menu to navigate to
        """

        menu: str = "Matches"
        user_path: list[MenuOptions] = [
            MenuOptions.MANAGE_TOURNAMENT,
            MenuOptions.MANAGE_ACTIVE_TOURNAMENT,
            MenuOptions.SELECT_MATCH,
            MenuOptions.INPUT_RESULTS,
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
        choice: str = self.utility.prompt_choice(["1", "2", "b"])

        winner = None

        match choice:
            case "b":
                return MenuOptions.SELECT_MATCH
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

        if isinstance(tournament_name, str):
            current_tournament: Tournament = (
                LogicLayerAPI.get_tournament_by_name(tournament_name)
            )
            tournament_id: str = current_tournament.uuid

            current_match: Match | str = LogicLayerAPI.get_match(
                tournament_id, team1_uuid, team2_uuid
            )
            if isinstance(current_match, Match):
                match_uuid: str = current_match.uuid
                if winner is not None:
                    winner_team: Team = LogicLayerAPI.get_team_by_name(winner)
                    winner_uuid = winner_team.uuid

                    LogicLayerAPI.change_match_winner(
                        tournament_id, match_uuid, winner_uuid
                    )

        print(self.tui.table(menu, user_path, info, options, message))
        choice: str = self.utility.prompt_choice(["b"])

        return MenuOptions.MANAGE_ACTIVE_TOURNAMENT

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
            MenuOptions.ADMIN_SCREEN,
            MenuOptions.MANAGE_TOURNAMENT,
            MenuOptions.MANAGE_INACTIVE_TOURNAMENT,
        ]
        info: list = [f"- - - - {str(tournament_name)} - - - -"]

        options: dict[str, str] = {
            "1": "Manage Teams",
            "2": "Publish",
            "b": "Back",
            "lo": "Log Out",
        }

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options))

        choice: str = self.utility.prompt_choice(["1", "2", "b", "lo"])

        match choice:
            case "1":
                return MenuOptions.MANAGE_TEAMS
            case "2":
                if (
                    amount_teams > 1
                ):  # To stop from going to PUBLISH if tournament is too small
                    return MenuOptions.PUBLISH
                else:
                    print(
                        "There Need To 2 Or More Teams In A Tournament To Publish."
                    )
                    input("Input Anything To Continue")
                    return MenuOptions.MANAGE_INACTIVE_TOURNAMENT
            case "b":
                return MenuOptions.ADMIN_SCREEN
            case "lo":
                return MenuOptions.LOGOUT
        return MenuOptions.MANAGE_TOURNAMENT

    def manage_teams(self) -> MenuOptions:
        """Manage teams screen, choices: 1,2 and b

        Returns:
            MenuOptions: The next menu to navigate to
        """

        # Keep the tournament name from previous screen
        tournament_name: str = LogicLayerAPI.save_player() or "None"

        tournament_object: Tournament | None = (
            LogicLayerAPI.get_tournament_by_name(tournament_name)
        )

        if tournament_object is None:  # Check if None goes through
            return MenuOptions.START_SCREEN

        menu: str = "Manage Teams"
        user_path: list[MenuOptions] = [
            MenuOptions.ADMIN_SCREEN,
            MenuOptions.MANAGE_TOURNAMENT,
            MenuOptions.MANAGE_INACTIVE_TOURNAMENT,
            MenuOptions.MANAGE_TEAMS,
        ]

        info: list = []
        options: dict[str, str] = {
            "1": "Add Team",
            "2": "Remove Team",
            "b": "Back",
        }

        x = 0
        for t in LogicLayerAPI.get_teams_from_tournament_name(tournament_name):
            x += 1
            info.append((f"{(str(x) + '. '): <4}" + t.name))

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options))

        choice: str = self.utility.prompt_choice(["1", "2", "b"])

        match choice:
            case "1":
                return MenuOptions.ADD_TEAM
            case "2":
                return MenuOptions.REMOVE_TEAM
            case "b":
                return MenuOptions.MANAGE_INACTIVE_TOURNAMENT
        return MenuOptions.MANAGE_INACTIVE_TOURNAMENT

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
            MenuOptions.MANAGE_TOURNAMENT,
            MenuOptions.MANAGE_INACTIVE_TOURNAMENT,
            MenuOptions.MANAGE_TEAMS,
            MenuOptions.ADD_TEAM,
        ]
        teams_not_in_tournament: list[str] = [
            x for x in all_teams if x not in teams_in_tournament
        ]

        unique_names: list[str] = teams_not_in_tournament

        output_list: list[str] = []  # list that holds each line as a f-string

        length: int = len(unique_names)

        for value in range(0, len(unique_names), 2):
            left = unique_names[value]
            if value + 1 < length:
                right = unique_names[value + 1]
                output_list.append(f"{left:<39}|{right:<39}|")

            else:  # odd number, last item has no pair
                output_list.append(f"{left:<39}|{' ':<39}|")

        info: list[str] = output_list

        options: dict[str, str] = {"t": "Try Again", "b": "Back"}

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info))

        team_to_add: str = input(
            self.message_color
            + "Input Team Name or 'q' to go back: \n"
            + self.reset
        )
        if team_to_add.lower() == "q":
            return MenuOptions.MANAGE_TEAMS

        # Validate team exists
        try:
            team_object: Team | None = LogicLayerAPI.get_team_by_name(
                team_to_add
            )
        except ValidationError:
            team_object = None

        if team_object is None:
            message = "Team Not Found"
            print(self.tui.table(menu, user_path, info, options, message))
            choice: str = self.utility.prompt_choice(["t", "b"])

            match choice:
                case "t":
                    return MenuOptions.ADD_TEAM

            return MenuOptions.MANAGE_TEAMS

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
        choice: str = self.utility.prompt_choice(["t", "b"])

        match choice:
            case "t":
                return MenuOptions.ADD_TEAM

        return MenuOptions.MANAGE_TEAMS

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
            MenuOptions.MANAGE_TOURNAMENT,
            MenuOptions.MANAGE_INACTIVE_TOURNAMENT,
            MenuOptions.MANAGE_TEAMS,
            MenuOptions.REMOVE_TEAM,
        ]

        info: list = teams_in_tournament
        options: dict[str, str] = {"t": "Try Again", "b": "Back"}

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info))

        team_to_add: str = input(
            self.message_color + "Input Team Name: \n" + self.reset
        )

        # Validate team exists
        try:
            team_object: Team | None = LogicLayerAPI.get_team_by_name(
                team_to_add
            )
        except ValidationError:
            team_object = None

        if team_object is None:
            message = "Team Not Found"
            print(self.tui.table(menu, user_path, info, options, message))
            choice: str = self.utility.prompt_choice(["t", "b"])

            match choice:
                case "t":
                    return MenuOptions.REMOVE_TEAM

            return MenuOptions.MANAGE_TEAMS

        if team_to_add in teams_in_tournament:
            LogicLayerAPI.remove_team(tournament_name, team_to_add)
            message: str = f"{team_to_add} Was Removed From {tournament_name}"
            options: dict[str, str] = {"t": "Remove Another", "b": "Back"}
        else:
            message = f"{team_to_add} Is Not A Valid Team"

        print(self.tui.table(menu, user_path, info, options, message))
        choice: str = self.utility.prompt_choice(["t", "b"])

        match choice:
            case "t":
                return MenuOptions.REMOVE_TEAM

        return MenuOptions.MANAGE_TEAMS

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
            return MenuOptions.START_SCREEN

        menu: str = "Publish"
        user_path: list[MenuOptions] = [
            MenuOptions.MANAGE_TOURNAMENT,
            MenuOptions.MANAGE_INACTIVE_TOURNAMENT,
            MenuOptions.PUBLISH,
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

        choice: str = self.utility.prompt_choice(["Y", "y", "N", "n"])

        if choice.lower() == "y":
            try:
                LogicLayerAPI.publish(tournament_name)
                return MenuOptions.MANAGE_TOURNAMENT
            except ValidationError as ex:
                input(f"Error: {ex} \nInput anything to go back")

        return MenuOptions.MANAGE_INACTIVE_TOURNAMENT

    # Created by Sindri
    def create_club(self) -> MenuOptions:
        """Create club screen, choices: fill info with input (name and color)

        Returns:
            MenuOptions: The next menu to navigate to
        """

        # print("This is the create club screen")
        menu: str = "Create club"
        user_path: list[MenuOptions] = [
            MenuOptions.ADMIN_SCREEN,
            MenuOptions.CREATE_CLUB,
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
            club_name: str = self.utility.input_info(
                "Enter Name or 'q' to cancel: \n", "handle", "CLUB"
            )
            if not club_name:
                return user_path[-2]
            self.tui.save_input("Club Name: " + club_name)

            print(self.tui.table(menu, user_path, info, options))
            con: str = self.utility.prompt_choice(["c", "b"])
            if con == "b":
                self.tui.discard_last_input()

        con = "b"
        while con == "b":
            print(self.tui.table(menu, user_path, info))
            club_color: str = str(
                self.utility.input_info(
                    "Choose color: Red, Green, yellow, blue, pink, cyan or 'q' to cancel: \n", "color", "CLUB"
                )
            )
            if not club_color:
                return user_path[-2]
            self.tui.save_input("Club Color: " + str(club_color))

            print(self.tui.table(menu, user_path, info, options))
            con: str = self.utility.prompt_choice(["c", "b"])
            if con == "b":
                self.tui.discard_last_input()

        con = "b"
        while con == "b":
            print(self.tui.table(menu, user_path, info))
            club_country: str = self.utility.input_info(
                "Enter Club country of origin or 'q' to cancel: \n",
                "name",
                "CLUB",
            )
            if not club_country:
                return user_path[-2]
            self.tui.save_input("Club Country: " + club_country)

            print(self.tui.table(menu, user_path, info, options))
            con: str = self.utility.prompt_choice(["c", "b"])
            if con == "b":
                self.tui.discard_last_input()

        con = "b"
        while con == "b":
            print(self.tui.table(menu, user_path, info))
            club_hometown: str = self.utility.input_info(
                "Enter Club Hometown or 'q' to cancel: \n", "name", "CLUB"
            )
            if not club_hometown:
                return user_path[-2]
            self.tui.save_input("Club Hometown: " + club_hometown)

            print(self.tui.table(menu, user_path, info, options))
            con: str = self.utility.prompt_choice(["c", "b"])
            if con == "b":
                self.tui.discard_last_input()
        # Club input done
        options: dict[str, str] = {
            "c": "Save Info And Continue",
            "b": "Discard Info And Go Back",
        }
        print(self.tui.table(menu, user_path, info, options, message))
        con: str = self.utility.prompt_choice(["c", "b"])

        if con == "b":
            return MenuOptions.ADMIN_SCREEN

        LogicLayerAPI.create_club(
            club_name, club_color, club_country, club_hometown
        )
        return MenuOptions.ADMIN_SCREEN
