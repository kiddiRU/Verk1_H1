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
        user_path: list[MenuOptions] = [MenuOptions.spectate_screen]
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
        user_path: list[MenuOptions] = [
            MenuOptions.spectate_screen,
            MenuOptions.spectate_players,
        ]
        info: list[str] = self.utility.show_main("players")
        options: dict[str, str] = {"t": "Try Again", "b": "Back"}
        message: str = "Player Not Found!"

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info))

        find_handle: str = input(
            self.message_color + "Input Handle or 'q' to cancel: " + self.reset
        )
        if find_handle == "q":
            return user_path[-2]

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
        user_path: list[MenuOptions] = [
            MenuOptions.spectate_screen,
            MenuOptions.spectate_players,
            MenuOptions.view_player_stats,
        ]
        # Changed by Sindri Freysson
        info: list[str] = [
            "Team: " + LogicLayerAPI.get_player_team_and_rank(player_handle)[0],
            "Wins: " + LogicLayerAPI.get_player_wins(player_handle),
            "Points: " + LogicLayerAPI.get_player_points(player_handle),
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
        user_path: list[MenuOptions] = [
            MenuOptions.spectate_screen,
            MenuOptions.spectate_clubs,
        ]
        info: list[str] = self.utility.show_main("clubs")
        options: dict[str, str] = {"t": "Try Again", "b": "Back"}
        message: str = "Club Not Found!"

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info))

        find_club: str = input(
            self.message_color
            + "Input Club Name or 'q' to cancel: "
            + self.reset
        )
        if find_club == "q":
            return user_path[-2]

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
        user_path: list[MenuOptions] = [
            MenuOptions.spectate_screen,
            MenuOptions.spectate_clubs,
            MenuOptions.view_club_stats,
        ]

        infoA: list[str] = [f"Teams: "] + self.utility.show_filtered(
            LogicLayerAPI.get_teams_in_club(club_name)
        )
        infoB: list[str] = [
            f"Color: " + LogicLayerAPI.get_club_by_name(club_name).club_color,
            f"Wins: " + LogicLayerAPI.get_club_wins(club_name),
            f"Points: " + LogicLayerAPI.get_club_points(club_name),
        ]
        info = infoA + infoB
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
        user_path: list[MenuOptions] = [
            MenuOptions.spectate_screen,
            MenuOptions.spectate_teams,
        ]
        info: list[str] = self.utility.show_main("teams")
        options: dict[str, str] = {"t": "Try Again", "b": "Back"}
        message: str = "Team Not Found!"

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info))

        find_handle: str = input(
            self.message_color
            + "Input Team Name or 'q' to cancel: "
            + self.reset
        )
        if find_handle == "q":
            return user_path[-2]

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
        user_path: list[MenuOptions] = [
            MenuOptions.spectate_screen,
            MenuOptions.spectate_teams,
            MenuOptions.view_team_stats,
        ]

        infoA: list[str] = [
            "Club: " + LogicLayerAPI.get_team_club(team_name),
            "Wins: " + LogicLayerAPI.get_team_wins(team_name),
            "Points: " + LogicLayerAPI.get_team_points(team_name),
        ]
        infoB: list[str] = [
            f"Team Members:\n{80 * "-"}"
        ] + self.utility.show_filtered(
            LogicLayerAPI.get_team_members_object(team_name)
        )
        info: list[str] = infoA + infoB
        options: dict[str, str] = {}
        message: str = ""

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options, message))
        input("Press Any Key To Go Back")
        return MenuOptions.spectate_teams

    def spectate_tournaments(self) -> MenuOptions:
        """Spectate tournaments screen, choose a tournament to view."""

        menu: str = "Tournaments"
        user_path: list[MenuOptions] = [
            MenuOptions.spectate_screen,
            MenuOptions.spectate_tournaments,
        ]

        info: list[str] = self.utility.show_tournaments_except_status(
            Tournament.StatusType.inactive
        )
        options: dict[str, str] = {"t": "Try Again", "b": "Back"}
        message: str = "Tournament Not Found!"

        # Show initial table
        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info))

        # User input
        tournament_name = input(
            self.message_color
            + "Input Tournament Name or 'q' to cancel: "
            + self.reset
        )
        if tournament_name == "q":
            return user_path[-2]

        tournament_list: list[Tournament] = LogicLayerAPI.list_tournaments()
        not_inactive: list[str] = self.utility.except_status_tournaments(
            Tournament.StatusType.inactive
        )

        # Validate tournament name
        if tournament_name in not_inactive:
            LogicLayerAPI.save_player(tournament_name)

            # Find the tournament object directly
            tournament_object = None
            for tournament in tournament_list:
                if tournament.name == tournament_name:
                    tournament_object = tournament
                    break

            if tournament_object:
                return (
                    MenuOptions.active_tournament
                    if tournament_object.status == Tournament.StatusType.active
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
        """Active tournament screen, choices: 1, 2 and b
        1: View game schedule
        2: View teams
        b: back to spectate tournaments screen

        Returns:
            MenuOptions: The next menu to navigate to
        """
        tournament_name: str | None = LogicLayerAPI.save_player()

        menu: str = str(tournament_name) + " Stats"
        user_path: list[MenuOptions] = [
            MenuOptions.spectate_screen,
            MenuOptions.spectate_tournaments,
            MenuOptions.active_tournament,
        ]
        info: list = []
        options: dict[str, str] = {
            "1": "Game Info And Schedule",
            "2": "Teams",
            "b": "Back",
        }
        message: str = ""

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options, message))

        choice: str = self.utility._prompt_choice(["1", "2", "b"])
        match choice:
            case "1":
                return MenuOptions.game_schedule
            case "2":
                return MenuOptions.teams_in_tournament
            case "b":
                return MenuOptions.spectate_tournaments

        return MenuOptions.spectate_tournaments

    def archived_tournament(self) -> MenuOptions:
        """Archived tournaments

        Returns:
            MenuOptions: The next menu to navigate to
        """
        tournament_name: str | None = LogicLayerAPI.save_player()
        if tournament_name == None: return MenuOptions.start_screen
        tournament_object = LogicLayerAPI.get_tournament_by_name(tournament_name)
        tournament_uuid: str = tournament_object.uuid

        menu: str = str(tournament_name) + " Stats"
        user_path: list[MenuOptions] = [
            MenuOptions.spectate_screen,
            MenuOptions.spectate_tournaments,
            MenuOptions.archived_tournament,
        ]
        info: list[str] = self.utility.list_matches(tournament_uuid, True)
        options: dict[str, str] = {}
        message: str = ""

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options, message))
        input("Press Any Key To Go Back")
        return MenuOptions.spectate_tournaments


    def game_schedule(self) -> MenuOptions:
        """Game schedule screen, choices: b
        b: back to active tournament screen

        Returns:
            MenuOptions: The next menu to navigate to
        """
        tournament_name: str | None = LogicLayerAPI.save_player()
        if tournament_name == None: return MenuOptions.start_screen
        tournament_object = LogicLayerAPI.get_tournament_by_name(tournament_name)
        tournament_uuid: str = tournament_object.uuid

        menu: str = str(tournament_name) + " Stats"
        user_path: list[MenuOptions] = [
            MenuOptions.spectate_screen,
            MenuOptions.spectate_tournaments,
            MenuOptions.active_tournament,
            MenuOptions.game_schedule,
        ]
        info: list[str] = self.utility.list_matches(tournament_uuid, False)
        options: dict[str, str] = {}
        message: str = ""

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options, message))
        input("Press Any Key To Go Back")
        return MenuOptions.active_tournament

    def teams_in_tournament(self) -> MenuOptions:
        """Teams in tournament screen, user types team name to view stats."""

        # Tournament chosen previously
        tournament_name: str = LogicLayerAPI.save_player() or "None"

        # Teams in this tournament
        teams_in_tournament: list[str] = [
            t.name
            for t in LogicLayerAPI.get_teams_from_tournament_name(
                tournament_name
            )
        ]

        menu: str = f"Teams in {tournament_name}"
        user_path: list[MenuOptions] = [
            MenuOptions.spectate_screen,
            MenuOptions.spectate_tournaments,
            MenuOptions.active_tournament,
            MenuOptions.teams_in_tournament,
        ]

        info: list[str] = teams_in_tournament

        options: dict[str, str] = {"t": "Try Again", "b": "Back"}
        message: str = "Team Not Found!"

        # Show initial table
        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info))

        # User input
        team_name = input(
            self.message_color
            + "Input Team Name or 'q' to cancel: "
            + self.reset
        ).strip()

        if team_name.lower() == "q":
            return user_path[-2]

        # Validate team name
        if team_name in teams_in_tournament:
            # Save selected team for the next screen
            self.temp_team = team_name
            return MenuOptions.team_tournament_stats

        # ---------- INVALID NAME ----------

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options, message))

        match self.utility._prompt_choice(["t", "b"]):
            case "t":
                return MenuOptions.teams_in_tournament

        return MenuOptions.active_tournament

    def team_tournament_stats(self) -> MenuOptions:
        """
        Docstring for team_tournament_stats

        :param self: Description
        :return: Description
        :rtype: MenuOptions
        """

        team_name = self.temp_team

        menu: str = str(team_name) + " Stats"
        user_path: list[MenuOptions] = [
            MenuOptions.spectate_tournaments,
            MenuOptions.active_tournament,
            MenuOptions.teams_in_tournament,
            MenuOptions.team_tournament_stats,
        ]

        infoA: list[str] = [
            "Club: " + LogicLayerAPI.get_team_club(team_name),
            "Wins: " + LogicLayerAPI.get_team_wins(team_name),
            "Points: " + LogicLayerAPI.get_team_points(team_name),
        ]
        infoB: list[str] = [
            f"Team Members:\n{80 * "-"}"
        ] + self.utility.show_filtered(
            LogicLayerAPI.get_team_members_object(team_name)
        )

        # Table design

        info: list[str] = infoA + infoB
        options: dict[str, str] = {}
        message: str = ""

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options, message))
        input("Press Any Key To Go Back")
        return MenuOptions.teams_in_tournament
