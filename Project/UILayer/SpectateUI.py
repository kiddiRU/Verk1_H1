"""
Author: Ísak Elí Hauksson <isak25@ru.is>
Date: 2025-12-04

File that holds all the menus that the spectator can access
"""

from Models.Tournament import Tournament

from UILayer.MenuOptions import MenuOptions
from UILayer.UtilityUI import UtilityUI
from UILayer.Drawer import Drawer

from LogicLayer import LogicLayerAPI


class SpectateUI:
    """Every spectate menu option"""

    def __init__(self) -> None:
        self.utility = UtilityUI()
        self.tui = Drawer()
        self.message_color = "\033[36m"
        self.reset: str = "\033[0m"
        self.underscore = "\033[4m"

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
        user_path: list[str] = [MenuOptions.spectate_screen]
        info: list[str] = []
        options: dict[str, str] = {
            "1": "Player",
            "2": "Clubs",
            "3": "Teams",
            "4": "Tournaments",
            "b": "Back To Start",
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
        menu: str = "Spectate Players"
        user_path: list[str] = [
            MenuOptions.spectate_screen,
            MenuOptions.spectate_players,
        ]
        info: list[str] = self.utility.show_main("players")
        options: dict[str, str] = {"t": "Try Again", "b": "Back"}
        message: str = "Player Not Found!"

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info))

        find_handle: str = input(
            self.message_color + "Input Handle: " + self.reset
        )

        if find_handle in self.utility.player_handles():
            LogicLayerAPI.save_player(find_handle)
            return MenuOptions.view_player_stats

        print(self.tui.table(menu, user_path, info, options, message))

        choice: str = self.utility._prompt_choice(["t", "b"])
        match choice:
            case "t":
                return MenuOptions.spectate_players

        return MenuOptions.spectate_screen

    def view_player_stats(self) -> MenuOptions:
        """View player stats screen, choices: b
        b: back to spectate players screen

        Returns:
            MenuOptions: The next menu to navigate to
        """
        # Remembers what player chosen in spectate_players
        player_handle: str | None = LogicLayerAPI.save_player()

        menu: str = str(player_handle) + " Stats"
        user_path: list[str] = [
            MenuOptions.spectate_screen,
            MenuOptions.spectate_players,
            MenuOptions.view_player_stats,
        ]
        # TODO: FIX WITH REAL INFORMATION
        info: list[str] = [
            "Team: TEAMNAME",
            "Wins: XX",
            "Points: XX",
            "Previous Teams: TEAMNAME ...",
            "Previous Clubs: CLUBNAME ...",
        ]
        options: dict[str, str] = {}
        message: str = ""

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options, message))
        input("Press Any Key To Go Back")
        return MenuOptions.spectate_players

    def spectate_clubs(self) -> MenuOptions:
        """Spectate clubs screen, choices: input a club to view stats

        Returns:
            MenuOptions: The next menu to navigate to
        """
        menu: str = "Clubs"
        user_path: list[str] = [
            MenuOptions.spectate_screen,
            MenuOptions.spectate_clubs,
        ]
        info: list[str] = self.utility.show_main("clubs")
        options: dict[str, str] = {"t": "Try Again", "b": "Back"}
        message: str = "Club Not Found!"

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info))

        find_club: str = input(
            self.message_color + "Input Club Name: " + self.reset
        )

        if find_club in self.utility.club_names():
            LogicLayerAPI.save_player(find_club)
            return MenuOptions.view_club_stats

        print(self.tui.table(menu, user_path, info, options, message))

        choice: str = self.utility._prompt_choice(["t", "b"])
        match choice:
            case "t":
                return MenuOptions.spectate_clubs

        return MenuOptions.spectate_screen

    def view_club_stats(self) -> MenuOptions:
        """View club stats screen, choices: b
        b: back to spectate players screen

        Returns:
            MenuOptions: The next menu to navigate to
        """
        club_name: str | None = LogicLayerAPI.save_player()

        menu: str = str(club_name) + " Stats"
        user_path: list[str] = [
            MenuOptions.spectate_screen,
            MenuOptions.spectate_clubs,
            MenuOptions.view_club_stats,
        ]

        # TODO: FIX WITH REAL INFORMATION
        info: list[str] = [
            f"Teams: TEAMNAME",
            f"Color: club_object.club_color",
            f"Wins: XX",
            f"Points: XX",
        ]
        options: dict[str, str] = {}
        message: str = ""

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options, message))
        input("Press Any Key To Go Back")
        return MenuOptions.spectate_clubs

    def spectate_teams(self) -> MenuOptions:
        """Spectate teams screen, choices: input a team to view stats

        Returns:
            MenuOptions: The next menu to navigate to
        """
        menu: str = "Teams"
        user_path: list[str] = [
            MenuOptions.spectate_screen,
            MenuOptions.spectate_teams,
        ]
        info: list[str] = self.utility.show_main("teams")
        options: dict[str, str] = {"t": "Try Again", "b": "Back"}
        message: str = "Team Not Found!"

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info))

        find_handle: str = input(
            self.message_color + "Input Team Name: " + self.reset
        )

        if find_handle in self.utility.team_names():
            LogicLayerAPI.save_player(find_handle)
            return MenuOptions.view_team_stats

        print(self.tui.table(menu, user_path, info, options, message))

        choice: str = self.utility._prompt_choice(["t", "b"])
        match choice:
            case "t":
                return MenuOptions.spectate_teams

        return MenuOptions.spectate_screen

    def view_team_stats(self) -> MenuOptions:
        """View team stats screen, choices: b
        b: back to spectate players screen

        Returns:
            MenuOptions: The next menu to navigate to
        """
        # Remembers what player chosen in spectate_players
        team_name: str | None = LogicLayerAPI.save_player()

        menu: str = str(team_name) + " Stats"
        user_path: list[str] = [
            MenuOptions.spectate_screen,
            MenuOptions.spectate_teams,
            MenuOptions.view_team_stats,
        ]
        # TODO: FIX WITH REAL INFORMATION
        info: list[str] = [
            "Club: CLUBNAME",
            "Wins: XX",
            "Points: XX",
            "Previous Teams: TEAMNAME ...",
            "Previous Clubs: CLUBNAME ...",
        ]
        options: dict[str, str] = {}
        message: str = ""

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options, message))
        input("Press Any Key To Go Back")
        return MenuOptions.spectate_teams

    def spectate_tournaments(self) -> MenuOptions:
        """Spectate tournaments screen, choose a tournament to view."""

        menu: str = "Tournaments"
        user_path: list[str] = [
            MenuOptions.spectate_screen,
            MenuOptions.spectate_tournaments,
        ]

        info: list[str] = self.utility.show_tournaments_except_status(Tournament.StatusType.inactive)
        options: dict[str, str] = {"t": "Try Again", "b": "Back"}
        message: str = "Tournament Not Found!"

        # Show initial table
        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info))

        # User input
        tournament_name = input(
            self.message_color + "Input Tournament Name: " + self.reset
        )

        tournament_list: list[Tournament] = LogicLayerAPI.list_tournaments()
        not_inactive: list[str] = self.utility.except_status_tournaments(Tournament.StatusType.inactive)

        # Validate tournament name
        if tournament_name in not_inactive:
            LogicLayerAPI.save_player(tournament_name)

            # Find the tournament object directly
            tournament = None
            for t in tournament_list:
                if t.name == tournament_name:
                    tournament = t
                    break

            if tournament:
                return (
                    MenuOptions.active_tournament
                    if tournament.status == Tournament.StatusType.active
                    else MenuOptions.archived_tournament
                )

        # Invalid name — show error screen
        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options, message))

        match self.utility._prompt_choice(["t", "b"]):
            case "t":
                return MenuOptions.spectate_tournaments
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
        tournament_name: str | None = LogicLayerAPI.save_player()

        menu: str = str(tournament_name) + " Stats"
        user_path: list[str] = [
            MenuOptions.spectate_screen,
            MenuOptions.spectate_tournaments,
            MenuOptions.active_tournament,
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
        tournament_name: str | None = LogicLayerAPI.save_player()

        menu: str = str(tournament_name) + " Stats"
        print(menu)
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
