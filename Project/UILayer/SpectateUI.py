"""
Author: Ísak Elí Hauksson <isak25@ru.is>
Date: 2025-12-04

File that holds all the menus that the spectator can access
"""

from UILayer.MenuOptions import MenuOptions
from UILayer.UtilityUI import UtilityUI
from UILayer.Drawer import Drawer

from LogicLayer import LogicLayerAPI


class SpectateUI:
    """Every spectate menu option"""

    def __init__(self) -> None:
        self.utility = UtilityUI()
        self.tui = Drawer()

    # TODO: self.list_players = LogicLayerAPI.list_players()

    def spectate_screen(self) -> MenuOptions:
        """Spectate screen, choices: 1,2,3 and b
        1: Check players
        2: Check clubs
        3: Check teams
        4: Check tournaments
        b: Back to start screen

        Returns:
            MenuOptions: The next menu to navigate to
        """

        menu: str = "Spectator Screen"
        user_path: list[str] = ["StartScreen", "SpectatorScreen"]
        info: list[str] = []
        options: dict[str, str] = {
            "1": "Player",
            "2": "Clubs",
            "3": "Teams",
            "4": "Tournaments",
            "b": "Back",
        }
        message: str = ""

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options, message))

        choice: str = self.utility._prompt_choice(["1", "2", "3", "4", "b"])
        match choice:
            case "1":
                return MenuOptions.spectate_players
            case "2":
                return MenuOptions.spectate_clubs
            case "3":
                return MenuOptions.spectate_teams
            case "4":
                return MenuOptions.spectate_tournaments
            case "b":
                return MenuOptions.start_screen

        return MenuOptions.start_screen

    def spectate_players(self) -> MenuOptions:
        """Spectate players screen, choices: input a player to view stats

        Returns:
            MenuOptions: The next menu to navigate to
        """
        menu: str = "Players"
        user_path: list[str] = ["SpectatorScreen", menu]
        info: list[str] = []
        options: dict[str, str] = {
            "Enter A Players Name Or The First Letter(s) To Search:": ""
        }
        message: str = ""

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options, message))
        # TODO: implement search player functionality from LL into utility class
        choice: str = self.utility._input_info("")
        match choice:
            # case "":
            #     self.list_players()
            case "b":
                return MenuOptions.spectate_screen
        return MenuOptions.view_player_stats

    def view_player_stats(self) -> MenuOptions:
        """View player stats screen, choices: b
        b: back to spectate players screen

        Returns:
            MenuOptions: The next menu to navigate to
        """
        stopper = input("This is the view player stats screen")
        return MenuOptions.spectate_screen

    def spectate_clubs(self) -> MenuOptions:
        """Spectate clubs screen, choices: input a club to view stats

        Returns:
            MenuOptions: The next menu to navigate to
        """
        menu: str = "Clubs"
        user_path: list[str] = ["SpectatorScreen", menu]
        info: list[str] = []
        options: dict[str, str] = {
            "Enter A Clubs Name Or The First Letter(s) To Search:": ""
        }
        message: str = ""

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options, message))

        # TODO: GET A LIST IF ALL CLUBS
        stopper = input("This is the spectate clubs screen")

        return MenuOptions.view_club_stats

    def view_club_stats(self) -> MenuOptions:
        """View club stats screen, choices: b
        b: back to spectate players screen

        Returns:
            MenuOptions: The next menu to navigate to
        """
        menu: str = "View Club Stats"
        user_path: list[str] = ["SpectatorScreen", "Clubs", "ClubStats"]
        info: list[str] = []
        options: dict[str, str] = {}
        message: str = ""

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options, message))
        stopper = input("This is the view club stats screen")
        match stopper:
            case "b":
                return MenuOptions.spectate_clubs
        return MenuOptions.spectate_screen

    def spectate_teams(self) -> MenuOptions:
        """Spectate teams screen, choices: input a team to view stats

        Returns:
            MenuOptions: The next menu to navigate to
        """
        menu: str = "Teams"
        user_path: list[str] = ["SpectatorScreen", menu]
        info: list[str] = []
        options: dict[str, str] = {
            "Enter A Teams Name Or The First Letter(s) To Search:": ""
        }
        message: str = ""

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options, message))
        stopper = input("This is the spectate teams screen")

        return MenuOptions.spectate_screen

    def view_team_stats(self) -> MenuOptions:
        """View team stats screen, choices: b
        b: back to spectate players screen

        Returns:
            MenuOptions: The next menu to navigate to
        """
        stopper = input("This is the view team stats screen")
        return MenuOptions.spectate_screen

    def spectate_tournaments(self) -> MenuOptions:
        """Spectate tournaments screen, choices: input a tournament to view


        Returns:
            MenuOptions: The next menu to navigate to
        """
        menu: str = "Tournaments"
        user_path: list[str] = ["SpectatorScreen", menu]
        info: list = []
        options: dict[str, str] = {
            "Enter A Tournaments Name Or The First Letter(s) To Search:": ""
        }
        message: str = ""

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options, message))

        stopper = input("This is the spectate tournaments screen")

        if ...:  # If the tournament is active
            return MenuOptions.active_tournament

        elif ...:  # If the tournament is archived
            return MenuOptions.archived_tournament

        return MenuOptions.spectate_screen

    def active_tournament(self) -> MenuOptions:
        """Active tournament screen, choices: 1, 2, 3 and b
        1: View game schedule
        2: View teams
        3: View bracket
        b: back to spectate tournaments screen

        Returns:
            MenuOptions: The next menu to navigate to
        """
        menu: str = "Active Tournament"
        user_path: list[str] = [
            "SpectatorScreen",
            "Tournaments",
            menu.replace(" ", ""),
        ]
        info: list = []
        options: dict[str, str] = {
            "1": "Game Info And Schedule",
            "2": "Teams",
            "3": "Brackets",
            "b": "Back",
        }
        message: str = ""

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options, message))
        
        choice: str = self.utility._prompt_choice(["1", "2", "3", "b"])
        match choice:
            case "1":
                return MenuOptions.game_schedule
            case "2":
                return MenuOptions.teams_in_tournament
            case "3":
                return MenuOptions.view_bracket
            case "b":
                return MenuOptions.spectate_tournaments

        return MenuOptions.spectate_tournaments

    def archived_tournament(self) -> MenuOptions:
        """Archived tournaments

        Returns:
            MenuOptions: The next menu to navigate to
        """
        # TODO: implement archived tournament screen
        stopper = input("This is the archived tournaments screen")
        return MenuOptions.spectate_tournaments

    def game_schedule(self) -> MenuOptions:
        """Game schedule screen, choices: b
        b: back to active tournament screen

        Returns:
            MenuOptions: The next menu to navigate to
        """
        stopper = input("This is the game schedule screen")
        return MenuOptions.active_tournament

    def view_bracket(self) -> MenuOptions:
        """View bracket screen, choices: b
        b: back to active tournament screen

        Returns:
            MenuOptions: The next menu to navigate to
        """
        stopper = input("This is the view bracket screen")
        return MenuOptions.active_tournament

    def teams_in_tournament(self) -> MenuOptions:
        """Teams in tournament screen, choices: input a team to view stats

        Returns:
            MenuOptions: The next menu to navigate to
        """
        stopper = input("This is the teams in tournament screen")

        return MenuOptions.active_tournament

    def team_tournament_stats(self) -> MenuOptions:
        """Team tournament stats screen, choices: b
        b: back to teams in tournament screen

        Returns:
            MenuOptions: The next menu to navigate to
        """
        stopper = input("This is the team tournament stats screen")
        return MenuOptions.teams_in_tournament
