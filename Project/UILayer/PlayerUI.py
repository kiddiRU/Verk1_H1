"""
Author: Ísak Elí Hauksson <isak25@ru.is>
Date: 2025-12-04

Author: Andri Már Kristjánsson <andrik25@ru.is>

File that holds all the menus that the player can access
"""

from UILayer.MenuOptions import MenuOptions
from UILayer.UtilityUI import UtilityUI
from UILayer.Drawer import Drawer
from LogicLayer import LogicLayerAPI
from Models.Player import Player


class PlayerUI:
    """Every player menu option"""

    def __init__(self) -> None:
        self.utility = UtilityUI()
        self.tui = Drawer()
        self.input_color = "\033[36m"
        self.reset: str = "\033[0m"
        self.underscore = "\033[4m"

    def start_screen(self) -> MenuOptions:
        """
        Display the start screen and handle initial navigation choices.

        The user may select one of the following options:
            1: Go to the login screen
            2: Go to the register screen
            3: Go to the spectating page
            q: Quit the program

        Returns:
            MenuOptions: The next menu to navigate to.
        """
        menu: str = "Start Page"
        user_path: list[MenuOptions] = [MenuOptions.START_SCREEN]
        options: dict[str, str] = {
            "1": "Log in",
            "2": "Register",
            "3": "Spectate",
            "q": "Quit program",
        }

        # Render the start screen table.
        print(self.tui.start_table(menu, user_path, options))

        # Ask the user for a valid menu selection.
        choice: str = self.utility.prompt_choice(["1", "2", "3", "q"])

        # Navigate based on the user's selection.
        match choice:
            case "1":
                return MenuOptions.LOGIN
            case "2":
                return MenuOptions.REGISTER
            case "3":
                return MenuOptions.SPECTATE_SCREEN
            case "q":
                return MenuOptions.QUIT

        return MenuOptions.START_SCREEN

    def login_screen(self) -> MenuOptions:
        """
        Display and handle the login screen workflow.

        This method renders the login UI, prompts the user for a handle,
        validates it using the LogicLayerAPI, and returns the next
        MenuOptions enum value that determines where the application
        should navigate next.

        Returns:
            MenuOptions: The next menu to display.
        """
        menu: str = "Log In"
        user_path: list[MenuOptions] = [
            MenuOptions.START_SCREEN,
            MenuOptions.LOGIN,
        ]
        info: list[str] = []
        options: dict[str, str] = {
            "t": "Try Again",
            "b": "Back",
        }

        # Clear previous UI state.
        self.tui.clear_saved_data()

        # Render initial login UI.
        print(self.tui.table(menu, user_path, info))

        # Prompt user input.
        prompt = (
            f"{self.input_color}"
            "Input Your Handle Or 'q' To Cancel:\n"
            f"{self.reset}"
        )
        login_handle: str = input(prompt)

        # Allow user to cancel login.
        if login_handle.lower() == "q":
            return MenuOptions.START_SCREEN

        # Attempt to resolve handle to a UUID.
        user_uuid = LogicLayerAPI.player_handle_to_uuid(login_handle)
        if user_uuid:
            LogicLayerAPI.save_player(login_handle)
            return MenuOptions.PLAYER_SCREEN

        # Special internal handles.
        match login_handle:
            case "admin":
                return MenuOptions.ADMIN_SCREEN
            case "Shrek":
                return MenuOptions.ONION
            case "Carlos Ray":
                return MenuOptions.MASTERPIECE

        # If handle not found, show error message.
        message: str = f"{login_handle} Not Found!"
        print(self.tui.table(menu, user_path, info, options, message))

        # Let user decide whether to retry or go back.
        choice: str = self.utility.prompt_choice(["t", "b"])

        if choice == "t":
            return MenuOptions.LOGIN

        return MenuOptions.START_SCREEN

    def register_screen(self) -> MenuOptions:
        """
        Display and manage the player registration workflow.

        The user is prompted to enter the following fields step by step:
            - Name
            - Date of birth
            - Home address
            - Email
            - Phone number
            - Handle
            - Optional URL

        At each step the user may:
            - c: Continue to the next field
            - b: Re-enter the current field
            - q: Cancel the registration entirely

        Returns:
            MenuOptions: The next menu to navigate to.
        """
        menu: str = "Register"
        user_path: list[MenuOptions] = [
            MenuOptions.START_SCREEN,
            MenuOptions.REGISTER,
        ]
        info: list[str] = []
        options: dict[str, str] = {"c": "Continue", "b": "Back"}
        message: str = "You Have Created A Player!"

        # Prevent unbound variables (VSCode warnings).
        user_name: str = ""
        user_dob: str = ""
        user_addr: str = ""
        user_email: str = ""
        user_phnum: str = ""
        user_handle: str = ""
        user_url: str = ""

        self.tui.clear_saved_data()

        # Gets the users information
        # Temprarily saves the data
        # So that the user can see their inputs before saving the registration
        # Allowes the user to cancel the registration an any time by inputing q

        # ---------------------- NAME ----------------------
        con: str = "b"
        while con == "b":
            print(self.tui.table(menu, user_path, info))
            user_name: str = self.utility.input_info(
                "Enter Name Or 'q' To Cancel:",
                "name",
                "PLAYER",
            )
            if not user_name:
                return MenuOptions.START_SCREEN

            self.tui.save_input(f"Name: {user_name}")
            print(self.tui.table(menu, user_path, info, options))
            con = self.utility.prompt_choice(["c", "b"])

            if con == "b":
                self.tui.discard_last_input()

        # ---------------------- DATE OF BIRT ----------------------
        con = "b"
        while con == "b":
            print(self.tui.table(menu, user_path, info))
            user_dob: str = str(
                self.utility.input_info(
                    (
                        "Enter Date Of Birth Or 'q' To Cancel:\n"
                        "(yyyy-mm-dd)"
                    ),
                    "date_of_birth",
                    "PLAYER",
                )
            )
            if not user_dob:
                return MenuOptions.START_SCREEN

            self.tui.save_input(f"Date Of Birth: {user_dob}")
            print(self.tui.table(menu, user_path, info, options))
            con = self.utility.prompt_choice(["c", "b"])
            if con == "b":
                self.tui.discard_last_input()

        # ---------------------- HOME ADDRESS ----------------------
        con = "b"
        while con == "b":
            print(self.tui.table(menu, user_path, info))
            user_addr: str = self.utility.input_info(
                (
                    "Enter Home Address Or 'q' To Cancel:\n"
                    "(Streetname 00 Cityname)"
                ),
                "home_address",
                "PLAYER",
            )
            if not user_addr:
                return MenuOptions.START_SCREEN

            self.tui.save_input(f"Home Address: {user_addr}")
            print(self.tui.table(menu, user_path, info, options))
            con = self.utility.prompt_choice(["c", "b"])
            if con == "b":
                self.tui.discard_last_input()

        # ---------------------- EMAIL ----------------------
        con = "b"
        while con == "b":
            print(self.tui.table(menu, user_path, info))
            user_email: str = self.utility.input_info(
                "Enter Email Or 'q' To Cancel:",
                "email",
                "PLAYER",
            )
            if not user_email:
                return MenuOptions.START_SCREEN

            self.tui.save_input(f"Email: {user_email}")
            print(self.tui.table(menu, user_path, info, options))
            con = self.utility.prompt_choice(["c", "b"])
            if con == "b":
                self.tui.discard_last_input()

        # ---------------------- PHONE NUMBER ----------------------
        con = "b"
        while con == "b":
            print(self.tui.table(menu, user_path, info))
            user_phnum: str = self.utility.input_info(
                "Enter Phone Number Or 'q' To Cancel:\n(123-4567)",
                "phone_number",
                "PLAYER",
            )
            if not user_phnum:
                return MenuOptions.START_SCREEN

            self.tui.save_input(f"Phone Number: {user_phnum}")
            print(self.tui.table(menu, user_path, info, options))
            con = self.utility.prompt_choice(["c", "b"])
            if con == "b":
                self.tui.discard_last_input()

        # ---------------------- HANDLE ----------------------
        con = "b"
        while con == "b":
            print(self.tui.table(menu, user_path, info))
            user_handle: str = self.utility.input_info(
                "Enter Handle Or 'q' To Cancel:",
                "handle",
                "PLAYER",
            )
            if not user_handle:
                return MenuOptions.START_SCREEN

            self.tui.save_input(f"Handle: {user_handle}")
            print(self.tui.table(menu, user_path, info, options))
            con = self.utility.prompt_choice(["c", "b"])
            if con == "b":
                self.tui.discard_last_input()

        # ---------------------- URL (OPTIONAL) ----------------------
        con = "b"
        while con == "b":
            print(self.tui.table(menu, user_path, info))
            user_url: str = input(
                f"{self.input_color}"
                "Enter URL Or 'q' To Cancel:\n"
                "(Optional, press Enter to leave blank)\n"
                f"{self.reset}"
            )
            if user_url.lower() == "q":
                return MenuOptions.START_SCREEN

            self.tui.save_input(f"URL: {user_url}")
            print(self.tui.table(menu, user_path, info, options))
            con = self.utility.prompt_choice(["c", "b"])
            if con == "b":
                self.tui.discard_last_input()

        # ---------------------- FINAL CONFIRMATION ----------------------
        final_options: dict[str, str] = {
            "c": "Save Info And Continue",
            "b": "Discard Info And Go Back",
        }

        print(
            self.tui.table(
                menu,
                user_path,
                info,
                final_options,
                message,
            )
        )

        final_choice: str = self.utility.prompt_choice(["c", "b"])
        if final_choice == "b":
            return MenuOptions.START_SCREEN

        # If the user saves the registration
        # it creates a new player in the system
        LogicLayerAPI.create_player(
            user_name,
            user_dob,
            user_addr,
            user_email,
            user_phnum,
            user_handle,
            user_url,
        )

        LogicLayerAPI.save_player(user_handle)

        return MenuOptions.PLAYER_SCREEN

    def player_screen(self) -> MenuOptions:
        """
        Display the player screen and show player info and available actions.

        Options:
            1: Edit info
            2: See team
            3: Create a team
            lo: Log out

        Returns:
            MenuOptions: The next menu to navigate to.
        """
        # Retrieve the currently logged-in handle.
        current_login_handle: str = str(LogicLayerAPI.save_player())
        current_login_uuid = LogicLayerAPI.player_handle_to_uuid(
            current_login_handle
        )

        player: Player | str = LogicLayerAPI.get_player_by_uuid(
            current_login_uuid
        )
        team, rank = LogicLayerAPI.get_player_team_and_rank(
            current_login_handle
        )
        club = LogicLayerAPI.get_team_club(team)

        # If the Player is not in a team
        # this will set the variables to the approptiate info
        if not team:
            team = None
            rank = "Player"
            club = None

        # Prevent unbound variables (VSCode warnings).
        current_login_name = None
        current_login_dob = None
        current_login_addr = None
        current_login_phnum = None
        current_login_email = None
        current_login_url = None
        current_login_team = team
        current_login_club = club
        current_login_rank = rank

        if isinstance(player, Player):
            current_login_name = player.name
            current_login_dob = player.date_of_birth
            current_login_addr = player.home_address
            current_login_phnum = player.phone_number
            current_login_email = player.email
            current_login_url = player.url

        menu: str = "Player Page"
        user_path: list[MenuOptions] = [MenuOptions.PLAYER_SCREEN]

        info_text = (
            f"Handle: {current_login_handle}\n"
            f"Name: {current_login_name}\n"
            f"Date of Birth: {current_login_dob}\n"
            f"Home Address: {current_login_addr}\n"
            f"Phone Number: {current_login_phnum}\n"
            f"Email: {current_login_email}\n"
            f"URL: {current_login_url}\n"
            f"Team: {current_login_team}\n"
            f"Club: {current_login_club}\n"
            f"Rank: {current_login_rank}"
        )

        info: list[str] = [info_text]

        options: dict[str, str] = {
            "1": "Edit Info",
            "2": "My Team",
            "3": "Create a Team",
            "lo": "Log Out",
        }

        message: str = ""

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options, message))

        choice: str = self.utility.prompt_choice(["1", "2", "3", "lo"])

        # Navigate based on the user's selection.
        match choice:
            case "1":
                return MenuOptions.EDIT_PLAYER_INFO
            case "2":
                if current_login_team is None:
                    return MenuOptions.MY_TEAM_EMPTY
                return MenuOptions.MY_TEAM_NOT_EMPTY
            case "3":
                if current_login_team is None:
                    return MenuOptions.CREATE_TEAM
                return MenuOptions.CREATE_TEAM_IN_TEAM
            case "lo":
                return MenuOptions.LOGOUT

        return MenuOptions.START_SCREEN

    def create_team(self) -> MenuOptions:
        """
        Display the create team screen
        and collect team information from the user.

        The user can input:
            - Team Name (required)
            - Team URL (optional)
            - Team ASCII art (optional)
            - Club (must exist in the club list)

        After input, the team is created and the user is assigned as captain.

        Returns:
            MenuOptions: The next menu to navigate to.
        """
        current_login_handle: str | None = LogicLayerAPI.save_player()
        player_list: list[Player] = LogicLayerAPI.list_all_players()

        # Prevent unbound variables (VSCode warnings).
        team_name: str | None = ""
        team_captain: Player = player_list[0]
        team_club: str = ""
        team_url: str = ""
        team_ascii: str = ""

        # Set the current logged-in player as the team captain.
        for player in player_list:
            if player.handle == current_login_handle:
                team_captain = player

        menu: str = "Create Team"
        user_path: list[MenuOptions] = [
            MenuOptions.PLAYER_SCREEN,
            MenuOptions.CREATE_TEAM,
        ]

        # List all available clubs.
        info: list[str] = ["- - - - List Of Clubs - - - -"]
        clubs = LogicLayerAPI.list_all_clubs()
        club_names = [club.name for club in clubs]
        info.extend(club_names)

        options: dict[str, str] = {"c": "Continue", "b": "Back"}
        message: str = "By Creating A Team You Are Assigned As The Captain!"

        # Get the team information from the user
        # Temporaraly save the info
        # Allows the user to cancel the team creation whenever by pressing q

        # ---------------------- TEAM NAME ----------------------
        con: str = "b"
        while con == "b":
            self.tui.clear_saved_data()
            print(self.tui.table(menu, user_path, [], {}, message))
            team_name = self.utility.input_info(
                "Enter Team Name Or 'q' To Cancel:\n", "handle", "TEAM"
            )
            if not team_name:
                return user_path[-2]

            self.tui.save_input(f"Team Name: {team_name}")
            print(self.tui.table(menu, user_path, [], options))
            con = self.utility.prompt_choice(["c", "b"])
            if con == "b":
                self.tui.discard_last_input()

        # ---------------------- TEAM URL (OPTIONAL) ----------------------
        con = "b"
        while con == "b":
            print(self.tui.table(menu, user_path))
            team_url = input(
                f"{self.input_color}Enter Team URL (Optional):\n{self.reset}"
            )
            self.tui.save_input(f"Team Url: {team_url}")
            print(self.tui.table(menu, user_path, [], options))
            con = self.utility.prompt_choice(["c", "b"])
            if con == "b":
                self.tui.discard_last_input()

        # ---------------------- TEAM ASCII ART (OPTIONAL) --------------------
        con = "b"
        while con == "b":
            print(self.tui.table(menu, user_path))
            team_ascii = input(
                f"""{self.input_color}Enter A Single Line Team ASCII Art
                (Optional):\n"""
                f"{self.reset}"
            )
            self.tui.save_input(f"Team ASCII Art: {team_ascii}")
            print(self.tui.table(menu, user_path, [], options))
            con = self.utility.prompt_choice(["c", "b"])
            if con == "b":
                self.tui.discard_last_input()

        # ---------------------- TEAM CLUB ----------------------
        message = ""
        while team_club not in club_names:
            print(self.tui.table(menu, user_path, info, {}, message))
            team_club = input(
                f"{self.input_color}Choose A Club To Join:\n{self.reset}"
            )
            if team_club not in club_names:
                message = f"{team_club} Does Not Exist Or Is Not Available"
            else:
                self.tui.save_input(f"Club: {team_club}")
                print(self.tui.table(menu, user_path, [], options))
                con = self.utility.prompt_choice(["c", "b"])
                if con == "b":
                    self.tui.discard_last_input()

        # ---------------------- FINAL CONFIRMATION ----------------------
        final_options: dict[str, str] = {
            "c": "Save Info And Continue",
            "b": "Discard Info And Go Back",
        }
        message = "You Have Created A Team!"
        print(self.tui.table(menu, user_path, [], final_options, message))
        choice: str = self.utility.prompt_choice(["c", "b"])

        # Creates the team and saves it in the system
        # and returns to the team screen
        if choice == "c":
            LogicLayerAPI.create_team(
                team_name, team_captain, team_club, team_url, team_ascii
            )
            return MenuOptions.MY_TEAM_NOT_EMPTY

        return MenuOptions.PLAYER_SCREEN

    def create_team_in_team(self) -> MenuOptions:
        """
        Display a screen when a player already in a team
        Tries to create a new team.

        The user is informed that they cannot create another team while already
        being a member of an existing team. They can only go back.

        Returns:
            MenuOptions: The next menu to navigate to.
        """
        menu: str = "Create A Team"
        user_path: list[MenuOptions] = [
            MenuOptions.PLAYER_SCREEN,
            MenuOptions.CREATE_TEAM_IN_TEAM,
        ]
        info: list[str] = []
        options: dict[str, str] = {"b": "Back"}
        message: str = "You Are Already In A Team!"

        # Shows a mesage letting the user know that they are in a team
        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options, message))

        choice: str = self.utility.prompt_choice(["b"])
        match choice:
            case "b":
                return MenuOptions.PLAYER_SCREEN

        return MenuOptions.PLAYER_SCREEN

    def edit_player_info(self) -> MenuOptions:
        """
        Display the edit player info screen and allow the user to update
        their personal information.

        The user may edit:
            - Name
            - Handle
            - Date of Birth
            - Home Address
            - Phone Number
            - Email
            - URL

        Leaving a field empty will keep it unchanged. Typing 'q' cancels
        editing and returns to the previous menu.

        Returns:
            MenuOptions: The next menu to navigate to.
        """
        current_login_handle: str | None = LogicLayerAPI.save_player()
        if isinstance(current_login_handle, str):
            login_uuid: str = LogicLayerAPI.player_handle_to_uuid(
                current_login_handle
            )
        else:
            login_uuid = ""  # type hinting safeguard

        current_player: Player | str = LogicLayerAPI.get_player_by_uuid(
            login_uuid
        )
        if not isinstance(current_player, Player):
            return MenuOptions.PLAYER_SCREEN

        # Existing player info
        name: str = current_player.name
        dob: str = current_player.date_of_birth
        addr: str = current_player.home_address
        email: str = current_player.email
        phnum: str = current_player.phone_number
        handle: str = current_player.handle
        url: str = current_player.url

        # Prevent unbound variables (VSCode warnings).
        new_name = name
        new_dob = dob
        new_addr = addr
        new_email = email
        new_phnum = phnum
        new_handle = handle
        new_url = url

        menu: str = "Edit Player Info"
        user_path: list[MenuOptions] = [
            MenuOptions.PLAYER_SCREEN,
            MenuOptions.EDIT_PLAYER_INFO,
        ]
        info: list[str] = []
        options: dict[str, str] = {"c": "Continue", "b": "Back"}
        message: str = "You Have Changed Your Info!"
        unchanged_message: str = (
            "(Leave Field Empty If You Want To Leave Them Unchanged)")

        # Gets new info from user and temporaraly saves it
        # untill user selects to fully save the changes
        # ---------------------- NAME ----------------------
        con: str = "b"
        while con == "b":
            print(self.tui.table(menu, user_path, info))
            new_name = self.utility.input_change(
                f"{unchanged_message}\nEnter New Name Or 'q' To Cancel:\n",
                "name", "PLAYER"
            )
            if new_name == "q":
                return user_path[-2]
            if not new_name:
                new_name = name

            self.tui.save_input(f"Name: {new_name}")
            print(self.tui.table(menu, user_path, [], options))
            con = self.utility.prompt_choice(["c", "b"])
            if con == "b":
                self.tui.discard_last_input()
                new_name = name

        # ---------------------- HANDLE ----------------------
        con = "b"
        while con == "b":
            print(self.tui.table(menu, user_path, info))
            new_handle = self.utility.input_change(
                f"{unchanged_message}\nEnter New Handle Or 'q' To Cancel:\n",
                "handle", "PLAYER"
            )
            if new_handle == "q":
                return user_path[-2]
            if not new_handle:
                new_handle = handle

            self.tui.save_input(f"Handle: {new_handle}")
            print(self.tui.table(menu, user_path, [], options))
            con = self.utility.prompt_choice(["c", "b"])
            if con == "b":
                self.tui.discard_last_input()
                new_handle = handle

        # ---------------------- DATE OF BIRTH ----------------------
        con = "b"
        while con == "b":
            print(self.tui.table(menu, user_path, info))
            new_dob = self.utility.input_change(
                f"""{unchanged_message}
Enter New Date Of Birth Or 'q' To Cancel:
(yyyy-mm-dd)""",  # Line was too long
                "date_of_birth", "PLAYER"
            )
            if new_dob == "q":
                return user_path[-2]
            if not new_dob:
                new_dob = dob

            self.tui.save_input(f"Date Of Birth: {new_dob}")
            print(self.tui.table(menu, user_path, [], options))
            con = self.utility.prompt_choice(["c", "b"])
            if con == "b":
                self.tui.discard_last_input()
                new_dob = dob

        # ---------------------- HOME ADDRESS ----------------------
        con = "b"
        while con == "b":
            print(self.tui.table(menu, user_path, info))
            new_addr = self.utility.input_change(
                f"""{unchanged_message}
Enter New Home Address Or 'q' To Cancel:
(Streetname 00 Cityname)""",  # Line was too long
                "home_address", "PLAYER"
            )
            if new_addr == "q":
                return user_path[-2]
            if not new_addr:
                new_addr = addr

            self.tui.save_input(f"Home Address: {new_addr}")
            print(self.tui.table(menu, user_path, [], options))
            con = self.utility.prompt_choice(["c", "b"])
            if con == "b":
                self.tui.discard_last_input()
                new_addr = addr

        # ---------------------- PHONE NUMBER ----------------------
        con = "b"
        while con == "b":
            print(self.tui.table(menu, user_path, info))
            new_phnum = self.utility.input_change(
                f"""{unchanged_message}
Enter New Phone Number Or 'q' To Cancel:
(123-4567)""",  # Line was too long
                "phone_number", "PLAYER"
            )
            if new_phnum == "q":
                return user_path[-2]
            if not new_phnum:
                new_phnum = phnum

            self.tui.save_input(f"Phone Number: {new_phnum}")
            print(self.tui.table(menu, user_path, [], options))
            con = self.utility.prompt_choice(["c", "b"])
            if con == "b":
                self.tui.discard_last_input()
                new_phnum = phnum

        # ---------------------- EMAIL ----------------------
        con = "b"
        while con == "b":
            print(self.tui.table(menu, user_path, info))
            new_email = self.utility.input_change(
                f"{unchanged_message}\nEnter New Email Or 'q' To Cancel:\n",
                "email", "PLAYER"
            )
            if new_email == "q":
                return user_path[-2]
            if not new_email:
                new_email = email

            self.tui.save_input(f"Email: {new_email}")
            print(self.tui.table(menu, user_path, [], options))
            con = self.utility.prompt_choice(["c", "b"])
            if con == "b":
                self.tui.discard_last_input()
                new_email = email

        # ---------------------- URL ----------------------
        con = "b"
        while con == "b":
            print(self.tui.table(menu, user_path, info))
            new_url = input(
                f"""{unchanged_message}
{self.input_color}Enter New URL Or 'q' To Cancel:
{self.reset}"""  # Line was a little too long
            )
            if new_url == "q":
                return user_path[-2]
            if not new_url:
                new_url = url

            self.tui.save_input(f"URL: {new_url}")
            print(self.tui.table(menu, user_path, [], options))
            con = self.utility.prompt_choice(["c", "b"])
            if con == "b":
                self.tui.discard_last_input()
                new_url = url

        # ---------------------- FINAL CONFIRMATION ----------------------
        final_options: dict[str, str] = {
            "c": "Save Info And Continue",
            "b": "Discard Info And Go Back",
        }
        print(self.tui.table(menu, user_path, [], final_options, message))
        choice: str = self.utility.prompt_choice(["c", "b"])

        # Saves the new user info in the system
        if choice == "c":
            LogicLayerAPI.update_player_info(
                current_player,
                new_name,
                new_dob,
                new_addr,
                new_email,
                new_phnum,
                new_handle,
                new_url
            )
            LogicLayerAPI.save_player(new_handle)

        return MenuOptions.PLAYER_SCREEN

    def my_team_empty(self) -> MenuOptions:
        """
        Display the 'My Team' screen when the player is not part of a team.

        The only available option is to go back to the player screen.

        Returns:
            MenuOptions: The next menu to navigate to.
        """
        menu: str = "My Team"
        user_path: list[MenuOptions] = [
            MenuOptions.PLAYER_SCREEN,
            MenuOptions.MY_TEAM_EMPTY,
        ]
        info: list[str] = []
        options: dict[str, str] = {"b": "Back"}
        message: str = "You Are Not In A Team!"

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options, message))

        choice: str = self.utility.prompt_choice(["b"])
        match choice:
            case "b":
                return MenuOptions.PLAYER_SCREEN

        return MenuOptions.PLAYER_SCREEN

    def my_team_not_empty(self) -> MenuOptions:
        """
        Display the 'My Team' screen when the player is part of a team.

        Options:
            1: Edit team (only for Captain)
            2: Leave team
            b: Back to the player screen

        Returns:
            MenuOptions: The next menu to navigate to.
        """
        current_login_handle: str = str(LogicLayerAPI.save_player())
        team, rank = LogicLayerAPI.get_player_team_and_rank(
            current_login_handle)

        team_members = LogicLayerAPI.get_team_members(team)

        menu: str = "My Team"
        user_path: list[MenuOptions] = [
            MenuOptions.PLAYER_SCREEN,
            MenuOptions.MY_TEAM_NOT_EMPTY,
        ]

        info: list[str] = [
            f"- - - -{team}- - - -",
            f"{self.underscore + 'Rank:'} \t \t Handle:{self.reset}"
        ]

        options: dict[str, str] = {
            "1": "Edit Team",
            "2": "Leave Team",
            "b": "Back",
        }

        # Gets team member info
        for member_uuid in team_members:
            player: Player | str = LogicLayerAPI.get_player_by_uuid(
                member_uuid)
            if isinstance(player, Player):
                _, member_rank = LogicLayerAPI.get_player_team_and_rank(
                    player.handle)
                if member_rank == "Captain":
                    info.append(f"{member_rank} \t {player.handle}")
                else:
                    info.append(f"{member_rank} \t \t {player.handle}")

        self.tui.clear_saved_data()

        # Captain options
        if rank == "Captain":
            print(self.tui.table(menu, user_path, info, options))
            choice: str = self.utility.prompt_choice(["1", "2", "b"])
            match choice:
                case "1":
                    return MenuOptions.EDIT_TEAM
                case "2":
                    return MenuOptions.LEAVE_TEAM
                case "b":
                    return MenuOptions.PLAYER_SCREEN
            return MenuOptions.PLAYER_SCREEN

        # Non- captain options
        options = {"1": "Leave Team", "b": "Back"}
        print(self.tui.table(menu, user_path, info, options))
        choice: str = self.utility.prompt_choice(["1", "b"])
        match choice:
            case "1":
                return MenuOptions.LEAVE_TEAM
            case "b":
                return MenuOptions.PLAYER_SCREEN

        return MenuOptions.PLAYER_SCREEN

    def edit_team(self) -> MenuOptions:
        """
        Display the edit team screen, showing the team members and
        allowing the captain to add or remove players.

        Options:
            1: Add player to team
            2: Remove player from team
            b: Back to My Team

        Returns:
            MenuOptions: The next menu to navigate to.
        """
        current_login_handle: str = str(LogicLayerAPI.save_player())

        # Get the team name
        team, _ = LogicLayerAPI.get_player_team_and_rank(current_login_handle)

        team_members = LogicLayerAPI.get_team_members(team)

        menu: str = "Edit Team"
        user_path: list[MenuOptions] = [
            MenuOptions.PLAYER_SCREEN,
            MenuOptions.MY_TEAM_NOT_EMPTY,
            MenuOptions.EDIT_TEAM,
        ]

        info: list[str] = [
            f"- - - -{team}- - - -",
            f"{self.underscore + 'Rank:'} \t \t Handle:{self.reset}"
        ]

        options: dict[str, str] = {
            "1": "Add Player To Team",
            "2": "Remove Player From Team",
            "b": "Back",
        }

        # Get team member info
        for member_uuid in team_members:
            member_player: Player | str = LogicLayerAPI.get_player_by_uuid(
                member_uuid)
            if isinstance(member_player, Player):
                _, member_rank = LogicLayerAPI.get_player_team_and_rank(
                    member_player.handle)

                # Format the captain and players accordingly
                if member_rank == "Captain":
                    info.append(f"{member_rank} \t {member_player.handle}")
                else:
                    info.append(f"{member_rank} \t \t {member_player.handle}")

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options))

        choice: str = self.utility.prompt_choice(["1", "2", "b"])
        match choice:
            case "1":
                return MenuOptions.ADD_PLAYER
            case "2":
                return MenuOptions.REMOVE_PLAYER
            case "b":
                return MenuOptions.MY_TEAM_NOT_EMPTY

        return MenuOptions.PLAYER_SCREEN

    def add_player(self) -> MenuOptions:
        """
        Display the screen to add a player to the current team.

        Shows a list of players not currently in a team. The user can
        select a player by handle to add them to the team.

        Returns:
            MenuOptions: The next menu to navigate to.
        """
        menu: str = "Add Player"
        user_path: list[MenuOptions] = [
            MenuOptions.PLAYER_SCREEN,
            MenuOptions.MY_TEAM_NOT_EMPTY,
            MenuOptions.EDIT_TEAM,
            MenuOptions.ADD_PLAYER,
        ]
        options: dict[str, str] = {"b": "Back"}
        message: str = ""

        # Get all players that are not in any team
        not_in_team: list[Player] = LogicLayerAPI.get_all_players_not_in_team()
        handles_not_team: list[str] = [p.handle for p in not_in_team]

        current_login_handle: str = str(LogicLayerAPI.save_player())
        team, _ = LogicLayerAPI.get_player_team_and_rank(current_login_handle)
        team_members = LogicLayerAPI.get_team_members(team)

        # Format the handles for display in two columns
        handles_not_team_format: list[str] = []
        length: int = len(handles_not_team)
        for i in range(0, length, 2):
            left = handles_not_team[i]
            if i + 1 < length:
                right = handles_not_team[i + 1]
                handles_not_team_format.append(f"{left:<39}|{right:<39}|")
            else:
                handles_not_team_format.append(f"{left:<39}|{' ':<39}|")

        info: list[str] = handles_not_team_format

        # Check if the team is full or ther are no players to add
        if not handles_not_team or len(team_members) >= 5:
            message = "No Players To Add To Team Or Team Is Full"
            self.tui.clear_saved_data()
            print(self.tui.table(menu, user_path, [], options, message))
            self.utility.prompt_choice(["b"])
            return MenuOptions.EDIT_TEAM

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info))
        add_handle: str = input(
            self.input_color
            + "Enter a player's handle to add them or 'q' to cancel:\n"
            + self.reset
        )
        if add_handle.lower() == "q":
            return MenuOptions.EDIT_TEAM

        self.tui.save_input(f"Player To Add: {add_handle}")

        add_uuid = LogicLayerAPI.player_handle_to_uuid(add_handle)
        add_in_team = LogicLayerAPI.get_players_team_uuid(add_uuid)

        # Check if player is found and available
        if add_uuid and not add_in_team:
            message = (
                f"The Player {add_handle} Was Found\n"
                "Do You Want To Add Them To Your Team? Y/N:"
            )
            print(self.tui.table(menu, user_path, info, {}, message))

            choice: str = self.utility.prompt_choice(["y", "n"])
            final_options: dict[str, str] = {"c": "Continue"}

            if choice == "n":
                message = "Operation Cancelled"
                print(self.tui.table(
                    menu, user_path, info, final_options, message))
                self.utility.prompt_choice(["c"])
                return MenuOptions.EDIT_TEAM

            current_login_handle = str(LogicLayerAPI.save_player())
            current_login_uuid = LogicLayerAPI.player_handle_to_uuid(
                current_login_handle)
            current_player: Player | str = LogicLayerAPI.get_player_by_uuid(
                current_login_uuid)

            if isinstance(current_player, Player):
                LogicLayerAPI.add_player(add_handle, current_player)

            message = f"{add_handle} Has Been Added To Your Team!"
            print(self.tui.table(
                menu, user_path, info, final_options, message))
            self.utility.prompt_choice(["c"])
            return MenuOptions.EDIT_TEAM

        # Player not found or unavailable
        message = (
            f"The Player {add_handle} Was Not Found Or Is Not Available\n"
            "Do You Want To Try Again? Y/N:"
        )
        print(self.tui.table(menu, user_path, info, {}, message))
        choice = self.utility.prompt_choice(["y", "n"])
        if choice == "n":
            return MenuOptions.EDIT_TEAM

        return MenuOptions.ADD_PLAYER

    def remove_player(self) -> MenuOptions:
        """
        Display the screen to remove a player from the current team.

        Shows the team members and allows the captain to remove a player
        by entering their handle.

        Returns:
            MenuOptions: The next menu to navigate to.
        """
        current_login_handle: str = str(LogicLayerAPI.save_player())
        current_uuid: str = LogicLayerAPI.player_handle_to_uuid(
            current_login_handle)
        current_player: Player | str = LogicLayerAPI.get_player_by_uuid(
            current_uuid)
        team, _ = LogicLayerAPI.get_player_team_and_rank(current_login_handle)
        team_members = LogicLayerAPI.get_team_members(team)

        menu: str = "Remove Player"
        user_path: list[MenuOptions] = [
            MenuOptions.PLAYER_SCREEN,
            MenuOptions.MY_TEAM_NOT_EMPTY,
            MenuOptions.EDIT_TEAM,
            MenuOptions.REMOVE_PLAYER,
        ]
        info: list[str] = [
            f"- - - -{team}- - - -",
            f"{self.underscore + 'Rank:'} \t \t Handle:{self.reset}",
        ]
        options: dict[str, str] = {"c": "Continue"}
        message: str = ""

        # Get team member info
        for member_uuid in team_members:
            member_player: Player | str = LogicLayerAPI.get_player_by_uuid(
                member_uuid)
            if isinstance(member_player, Player):
                _, member_rank = LogicLayerAPI.get_player_team_and_rank(
                    member_player.handle)
                if member_rank != "Captain":
                    info.append(f"{member_rank} \t \t {member_player.handle}")

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info))

        remove_handle: str = input(
            self.input_color
            + "Enter A Player's Handle To Remove Them Or 'q' To Cancel:\n"
            + self.reset
        )
        if remove_handle.lower() == "q":
            return MenuOptions.EDIT_TEAM

        current_team, _ = LogicLayerAPI.get_player_team_and_rank(remove_handle)
        remove_player_team, _ = LogicLayerAPI.get_player_team_and_rank(
            current_login_handle)

        # Player is in the same team and is not the captain themselves
        if (current_team == remove_player_team
                and remove_handle != current_login_handle):
            message = (
                f"The Player {remove_handle} Was Found\n"
                "Do You Want To Remove Them From Your Team? Y/N:"
            )
            print(self.tui.table(menu, user_path, info, {}, message))

            choice: str = self.utility.prompt_choice(["y", "n"])
            if choice == "n":
                message = "Operation Cancelled"
                print(self.tui.table(menu, user_path, info, options, message))
                self.utility.prompt_choice(["c"])
                return MenuOptions.EDIT_TEAM

            if isinstance(current_player, Player):
                LogicLayerAPI.remove_player(remove_handle, current_player)

            message = f"{remove_handle} Has Been Removed From Your Team!"
            print(self.tui.table(menu, user_path, info, options, message))
            self.utility.prompt_choice(["c"])
            return MenuOptions.EDIT_TEAM

        # Player not found or cannot be removed
        message = (
            f"The Player {remove_handle} Was Not Found Or Is Not Removable\n"
            "Do You Want To Try Again? Y/N:"
        )
        print(self.tui.table(menu, user_path, info, {}, message))
        choice: str = self.utility.prompt_choice(["y", "n"])
        if choice == "n":
            return MenuOptions.EDIT_TEAM

        return MenuOptions.REMOVE_PLAYER

    def leave_team(self) -> MenuOptions:
        """
        Display the leave team screen and handle leaving logic.

        If the player is the captain, they must select a new captain
        before leaving the team. Otherwise, they can confirm leaving.

        Returns:
            MenuOptions: The next menu to navigate to.
        """
        # Turn into a string for the type hinting (VSCode warnings)
        current_login_handle: str = str(LogicLayerAPI.save_player())

        current_uuid: str = LogicLayerAPI.player_handle_to_uuid(
            current_login_handle)
        current_player: Player | str = LogicLayerAPI.get_player_by_uuid(
            current_uuid)
        team, rank = LogicLayerAPI.get_player_team_and_rank(
            current_login_handle)
        team_members = LogicLayerAPI.get_team_members(team)
        number_of_players = len(team_members)

        menu: str = "Leave Team"
        user_path: list[MenuOptions] = [
            MenuOptions.PLAYER_SCREEN,
            MenuOptions.MY_TEAM_NOT_EMPTY,
            MenuOptions.LEAVE_TEAM,
        ]
        info: list[str] = []
        options: dict[str, str] = {"Y": "Yes", "N": "No"}
        message: str = f"Are You Sure You Want To Leave {team}?"

        # Captain leaving
        if rank == "Captain":
            if number_of_players > 1:
                # Select new captain
                message = f"Select a new captain before leaving {team}"
                print(self.tui.table(menu, user_path, info, {}, message))
                new_captain = input(
                    self.input_color
                    + "Enter a player's handle to promote them to captain:\n"
                    + self.reset
                )

                current_team, _ = LogicLayerAPI.get_player_team_and_rank(
                    new_captain)
                new_captain_team, _ = LogicLayerAPI.get_player_team_and_rank(
                    current_login_handle)

                # Trying to promote someone form the team
                # That is not the current captain
                if ((current_team == new_captain_team
                        and new_captain != current_login_handle)):
                    message = (
                        f"The Player {new_captain} Was Found\n"
                        "Do You Want To Promote Them To Captain? Y/N:"
                    )
                    print(self.tui.table(menu, user_path, info, {}, message))

                    choice: str = self.utility.prompt_choice(["y", "n"])
                    if choice == "y" and isinstance(current_player, Player):
                        LogicLayerAPI.promote_captain(
                            current_player, new_captain)
                        LogicLayerAPI.remove_player(
                            current_login_handle, current_player)
                        return MenuOptions.PLAYER_SCREEN
                    return MenuOptions.EDIT_TEAM

                # Player not found or unavailable
                message = """Player Was Not Found Or Not Available
Do You Want To Try Again? Y/N:"""
                print(self.tui.table(menu, user_path, info, {}, message))
                choice = self.utility.prompt_choice(["y", "n"])
                if choice == "n":
                    return MenuOptions.EDIT_TEAM
                return MenuOptions.LEAVE_TEAM

            # Captain is the only member
            message = (
                f"You Are The Only One Left In The Team\n"
                f"If You Leave, the team {team} will no longer be accessible\n"
                "Are You Sure You Want To Leave? Y/N"
            )
            print(self.tui.table(menu, user_path, info, options, message))
            choice: str = self.utility.prompt_choice(["y", "n"])
            final_options: dict[str, str] = {"c": "Continue"}
            if choice == "y" and isinstance(current_player, Player):
                LogicLayerAPI.remove_player(
                    current_login_handle, current_player)
                message = "You Have Successfully Left The Team!"
                print(self.tui.table(
                    menu, user_path, info, final_options, message))
                self.utility.prompt_choice(["c"])
                return MenuOptions.PLAYER_SCREEN

        # Non-captain leaving and confirmation
        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options, message))
        choice: str = self.utility.prompt_choice(["y", "n"])
        final_options = {"c": "Continue"}

        if choice == "n":
            message = "Operation Canceled"
            print(self.tui.table(
                menu, user_path, info, final_options, message))
            self.utility.prompt_choice(["c"])
            return MenuOptions.MY_TEAM_NOT_EMPTY

        if isinstance(current_player, Player):
            LogicLayerAPI.remove_player(current_login_handle, current_player)

        message = "You Have Successfully Left The Team!"
        print(self.tui.table(menu, user_path, info, final_options, message))
        self.utility.prompt_choice(["c"])
        return MenuOptions.PLAYER_SCREEN

    def onion(self) -> MenuOptions:
        """This Program Has Layers

        :returns:
            MenuOptions: The next menu to navigate to
        """

        # Well ogres arent white, are they?
        shrek: str = "\033[32m"
        reset: str = "\033[0m"

        # GET OUTTA MA SWAMP!
        # *Insert ogre roar here*
        print(shrek + """
    ⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀
    ⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀
    ⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆
    ⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆
    ⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆
    ⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿
    ⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉
    ⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
    ⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇
    ⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇
    ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿
    ⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇
    ⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃
    ⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠛⠉
    """ + reset + """
Somebody once told me the world is gonna roll me
I ain't the sharpest tool in the shed
She was looking kind of dumb with her finger and her thumb
In the shape of an "L" on her forehead
Well, the years start comin' and they don't stop comin'
Fed to the rules and I hit the ground runnin'
Didn't make sense not to live for fun
Your brain gets smart, but your head gets dumb
So much to do, so much to see
So, what's wrong with taking the backstreets?
You'll never know if you don't go (go)
You'll never shine if you don't glow
Hey now, you're an all-star
Get your game on, go play
Hey now, you're a rock star
Get the show on, get paid
(And all that glitters is gold)
Only shootin' stars break the mold
It's a cool place, and they say it gets colder
You're bundled up now, wait 'til you get older
But the meteor men beg to differ
Judging by the hole in the satellite picture
The ice we skate is gettin' pretty thin
The water's gettin' warm, so you might as well swim
My world's on fire, how 'bout yours?
That's the way I like it, and I'll never get bored
Hey now, you're an all-star
Get your game on, go play
Hey now, you're a rock star
Get the show on, get paid
(All that glitters is gold)
Only shootin' stars break the mold
Go for the moon
(Go, go, go) go for the moon
(Go, go, go) go for the moon
Go (go), go for the moon
Hey now, you're an all-star
Get your game on, go play
Hey now, you're a rock star
Get the show on, get paid
(And all that glitters is gold)
Only shooting stars
Somebody once asked, "Could I spare some change for gas?
I need to get myself away from this place"
I said, "Yep, what a concept, I could use a little fuel myself
And we could all use a little change"
Well, the years start comin' and they don't stop comin'
Fed to the rules and I hit the ground runnin'
Didn't make sense not to live for fun
Your brain gets smart, but your head gets dumb
So much to do, so much to see
So, what's wrong with taking the backstreets?
You'll never know if you don't go (go!)
You'll never shine if you don't glow
Hey now, you're an all-star
Get your game on, go play
Hey now, you're a rock star
Get the show on, get paid
(And all that glitters is gold)
Only shootin' stars break the mold
Only shootin' stars break the mold
Go for the moon
Go for the moon
Go for the moon
This is how we do it

                    """)

        # *Swamp bubble sounds*
        a = input()
        if a == "GET OUTTA MA SWAMP!":
            return MenuOptions.START_SCREEN

        return MenuOptions.ONION

    def masterpiece(self) -> MenuOptions:
        """I think Gylfi will like this one

        :returns:
            MenuOptions: The next screen to navigate to"""

        # This is just to have a bit of fun cus my sanity is fullt drained
        # His hat is a bit messed up because it broke the 79 character limmit
        print("""
                                     MMMMMMMMMMM
                                  MMMMMMMMMMMMMMMMM
                              NMMMMMMMMMMMMMMMMMMMMMMMM
                           MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                         MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
                        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMD
                       DMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                      MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                      MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                     MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
                    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
                    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
NM                  MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMM              MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMM8MMMMMMMMMIMMMMM8,. ...........OMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMM ..N. .....MMMM...............:MMMMNMMMMMMMMMMMMMMMM
    NMMMMMMMMMMMMMMMMMMMMM.....:..DMMMMMNZ Z.... .......M$MMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMNMMMMMMM....... 7=MMMMMMO....Z .......MM7MMMMMMMMMMMMMMMMMMMM
            MMMMMMMMMMMMMMMMM  Z...MMMZ .. .,M..,........MMMMMMMMMMMMMMMMMMMMMM
                MMMMMM.......DOM ....N7..................MMMMMMMMMMMMMMMMMMMMMM
                    MMM....... M. ... .  ... ..............M...$MMMMMMMMMMMMMMM
                    ........... ......... ..............M..=....+MMMMMMMMMMMMMM
                    ......+.NMI........ . ..............M.,.I...MMMMMMMMMMMMMMN
                    ......$... ...... O..................,.....$MMMMMMMMMMMMN
                    .....M.......... M M.. .............. 8  .OMMMMMMMMMMMN
                    ..=7I,,.,,IMI...M.................. ..MMMMMMMMMMM
                    ....DMMMMMMMMMMMMMMMO..............D...MMMMMMMMM
                        .MMMMMMMMMMMMMMDDMM:,N..............DMMMMMMMMMMM
                        NMMMMMNMM8 . .... ...,............  MMMMMMMMM
                        MMMMM,:......::..M8M8MM...............MMMMMM
                        MMMM ... . .........,MM..............MMMMMO$
                        MMMMM... =.=. .. . . MM ....... . ...MMMMMMM
                        NMMMMMMMMMM?  ..O.?NM7 ....... ......MMMMMM
                        NMMMMMMMMMMMMMMMMM........  $ . ...MMMNMMM
                        MMMMMMMMMMMMMMM.........,, ......MMMMMMMM
                            OMMMMMMMM8 , .. .. .,N.... ...:MMMMMMMMMMN
                            MMMMMMMM?N. ...MD.:MNI8MMMMMMMMMMMMMMMMMN
                        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
                    NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
                    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
                MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
            MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
            NMMMMMMMMMMMMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
            MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM


            """)
        # Unfortunatly could not find any ascii art of a 2 liter pepsi bottle
        print("""
            ⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣷⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀
            ⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠟
            ⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⡆⠀⠀⠀⠀⢠⣶⡿⠟⠻⢿⣦⡀⠀⠀⣠⣾⠿⠛⠿⣷⣄⠀⠀⢠⣶⡿⠟⠻⢿⣦⡀⠀⢠⣾⠟⠛⠻⠷⠀⠀⢸⡇
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⣸⣿⠀⠀⠀⠀⣿⠏⠀⠀⠀⠀⢹⣿⠀⢸⣿⣁⣀⣀⣀⣈⣿⡆⠀⣿⠏⠀⠀⠀⠀⢹⣿⠀⠸⣿⣤⣀⣀⡀⠀⠀⢸⡇
            ⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⢀⣴⣿⣿⠀⠀⠀⢠⣿⡄⠀⠀⠀⠀⣸⣿⠀⢸⣿⡋⠉⠛⠛⢛⠉⠁⢀⣿⡆⠀⠀⠀⠀⣸⣿⠀⠀⠀⠉⠉⠛⣿⡆⠀⢸⡇
            ⠸⣿⣿⣿⣿⡿⠟⠉⠀⠀⢀⣀⣤⣶⣿⣿⣿⠇⠀⠀⠀⢸⣿⠿⣶⣤⣤⣾⠟⠁⠀⠀⠙⢿⣶⣤⣶⡿⠗⠀⢈⣿⠻⣶⣤⣤⣾⠟⠁⠀⠺⢷⣦⣤⣶⡿⠃⠀⢸⡇
            ⠀⠙⢛⣋⣥⣤⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠈⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠈⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠈⠉⠛⠛⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")

        like = input(
            self.input_color
            + "Do you like my art? Y/N 	⤜(ⱺ ʖ̯ⱺ)⤏ \n"
            + self.reset
        )

        # You better like the art
        # Or else you dont have the privlage of using this program
        if like.lower() == "y":
            print("YAY")
            input("BYE BYE ⊂(◉‿◉)つ")
            return MenuOptions.START_SCREEN

        print("\033[31m" + "Deleting File And System" + "\033[0m")
        return MenuOptions.QUIT
