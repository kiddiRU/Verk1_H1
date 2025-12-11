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
        user_path: list[MenuOptions] = [MenuOptions.SPECTATE_SCREEN]
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

        choice: str = self.utility.prompt_choice(["1", "2", "3", "4", "b"])
        match choice:
            case "1":
                return MenuOptions.SPECTATE_PLAYERS
            case "2":
                return MenuOptions.SPECTATE_CLUBS
            case "3":
                return MenuOptions.SPECTATE_TEAMS
            case "4":
                return MenuOptions.SPECTATE_TOURNAMENTS
            case "b":
                return MenuOptions.START_SCREEN

        return MenuOptions.START_SCREEN

    def spectate_players(self) -> MenuOptions:
        """Spectate players screen, choices: input a player to view stats

        Returns:
            MenuOptions: The next menu to navigate to
        """
        menu: str = "Spectate Players"
        user_path: list[MenuOptions] = [
            MenuOptions.SPECTATE_SCREEN,
            MenuOptions.SPECTATE_PLAYERS,
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
            return MenuOptions.VIEW_PLAYER_STATS

        print(self.tui.table(menu, user_path, info, options, message))

        choice: str = self.utility.prompt_choice(["t", "b"])
        match choice:
            case "t":
                return MenuOptions.SPECTATE_PLAYERS

        return MenuOptions.SPECTATE_SCREEN

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
            MenuOptions.SPECTATE_SCREEN,
            MenuOptions.SPECTATE_PLAYERS,
            MenuOptions.VIEW_PLAYER_STATS,
        ]
        # Changed by Sindri Freysson
        info: list[str] = [
            "Team: "
            + LogicLayerAPI.get_player_team_and_rank(player_handle)[0],
            "Wins: " + LogicLayerAPI.get_player_wins(player_handle),
            "Points: " + LogicLayerAPI.get_player_points(player_handle),
        ]
        options: dict[str, str] = {}
        message: str = ""

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options, message))
        input("Press Any Key To Go Back")
        return MenuOptions.SPECTATE_PLAYERS

    def spectate_clubs(self) -> MenuOptions:
        """Spectate clubs screen, choices: input a club to view stats

        Returns:
            MenuOptions: The next menu to navigate to
        """
        menu: str = "Clubs"
        user_path: list[MenuOptions] = [
            MenuOptions.SPECTATE_SCREEN,
            MenuOptions.SPECTATE_CLUBS,
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
            return MenuOptions.VIEW_CLUB_STATS

        print(self.tui.table(menu, user_path, info, options, message))

        choice: str = self.utility.prompt_choice(["t", "b"])
        match choice:
            case "t":
                return MenuOptions.SPECTATE_CLUBS

        return MenuOptions.SPECTATE_SCREEN

    def view_club_stats(self) -> MenuOptions:
        """View club stats screen, choices: b
        b: back to spectate players screen

        Returns:
            MenuOptions: The next menu to navigate to
        """
        club_name: str | None = LogicLayerAPI.save_player()

        menu: str = str(club_name) + " Stats"
        user_path: list[MenuOptions] = [
            MenuOptions.SPECTATE_SCREEN,
            MenuOptions.SPECTATE_CLUBS,
            MenuOptions.VIEW_CLUB_STATS,
        ]

        info_a: list[str] = [
            f"Teams:\n{80 * '—'}"
        ] + self.utility.string_to_table(
            self.utility.object_to_string(
                LogicLayerAPI.get_teams_in_club(club_name)
            )
        )
        info_b: list[str] = [
            f"{80 * '—'}\n"
            f"Color: " + LogicLayerAPI.get_club_by_name(club_name).club_color,
            f"Wins: " + LogicLayerAPI.get_club_wins(club_name),
            f"Points: " + LogicLayerAPI.get_club_points(club_name),
        ]
        info = info_a + info_b
        options: dict[str, str] = {}
        message: str = ""

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options, message))
        input("Press Any Key To Go Back")
        return MenuOptions.SPECTATE_CLUBS

    def spectate_teams(self) -> MenuOptions:
        """Spectate teams screen, choices: input a team to view stats

        Returns:
            MenuOptions: The next menu to navigate to
        """
        menu: str = "Teams"
        user_path: list[MenuOptions] = [
            MenuOptions.SPECTATE_SCREEN,
            MenuOptions.SPECTATE_TEAMS,
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
            return MenuOptions.VIEW_TEAM_STATS

        print(self.tui.table(menu, user_path, info, options, message))

        choice: str = self.utility.prompt_choice(["t", "b"])
        match choice:
            case "t":
                return MenuOptions.SPECTATE_TEAMS

        return MenuOptions.SPECTATE_SCREEN

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
            MenuOptions.SPECTATE_SCREEN,
            MenuOptions.SPECTATE_TEAMS,
            MenuOptions.VIEW_TEAM_STATS,
        ]

        info_a: list[str] = [
            "Club: " + LogicLayerAPI.get_team_club(team_name),
            "Wins: " + LogicLayerAPI.get_team_wins(team_name),
            "Points: " + LogicLayerAPI.get_team_points(team_name),
        ]
        info_b: list[str] = [
            f"Team Members:\n{80 * '-'}"
        ] + self.utility.string_to_table(
            self.utility.object_to_string(
                LogicLayerAPI.get_team_members_object(team_name)
            )
        )
        info_c: list[str] = (
            [f"{80 * '*'}"]
            + [f"Tournament History:\n{80 * '-'}"]
            + self.utility.string_to_table(
                LogicLayerAPI.get_team_history(team_name)
            )
        )
        info: list[str] = info_a + info_b + info_c
        options: dict[str, str] = {}
        message: str = ""

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options, message))
        input("Press Any Key To Go Back")
        return MenuOptions.SPECTATE_TEAMS

    def spectate_tournaments(self) -> MenuOptions:
        """Spectate tournaments screen, choose a tournament to view."""

        menu: str = "Tournaments"
        user_path: list[MenuOptions] = [
            MenuOptions.SPECTATE_SCREEN,
            MenuOptions.SPECTATE_TOURNAMENTS,
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
                    MenuOptions.ACTIVE_TOURNAMENT
                    if tournament_object.status == Tournament.StatusType.active
                    else MenuOptions.ARCHIVED_TOURNAMENT
                )

        # Invalid name — show error screen
        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options, message))

        match self.utility.prompt_choice(["t", "b"]):
            case "t":
                return MenuOptions.SPECTATE_TOURNAMENTS
        return MenuOptions.SPECTATE_SCREEN

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
            MenuOptions.SPECTATE_SCREEN,
            MenuOptions.SPECTATE_TOURNAMENTS,
            MenuOptions.ACTIVE_TOURNAMENT,
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

        choice: str = self.utility.prompt_choice(["1", "2", "b"])
        match choice:
            case "1":
                return MenuOptions.GAME_SCHEDULE
            case "2":
                return MenuOptions.TEAMS_IN_TOURNAMENT
            case "b":
                return MenuOptions.SPECTATE_TOURNAMENTS

        return MenuOptions.SPECTATE_TOURNAMENTS

    def archived_tournament(self) -> MenuOptions:
        """Archived tournaments

        Returns:
            MenuOptions: The next menu to navigate to
        """
        tournament_name: str | None = LogicLayerAPI.save_player()
        if tournament_name is None:
            return MenuOptions.START_SCREEN
        tournament_object = LogicLayerAPI.get_tournament_by_name(
            tournament_name
        )
        tournament_uuid: str = tournament_object.uuid

        menu: str = str(tournament_name) + " Stats"
        user_path: list[MenuOptions] = [
            MenuOptions.SPECTATE_SCREEN,
            MenuOptions.SPECTATE_TOURNAMENTS,
            MenuOptions.ARCHIVED_TOURNAMENT,
        ]
        info: list[str] = self.utility.list_matches(tournament_uuid, True)
        options: dict[str, str] = {}
        message: str = ""

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options, message))
        input("Press Any Key To Go Back")
        return MenuOptions.SPECTATE_TOURNAMENTS

    def game_schedule(self) -> MenuOptions:
        """Game schedule screen, choices: b
        b: back to active tournament screen

        Returns:
            MenuOptions: The next menu to navigate to
        """
        tournament_name: str | None = LogicLayerAPI.save_player()
        if tournament_name is None:
            return MenuOptions.START_SCREEN
        tournament_object = LogicLayerAPI.get_tournament_by_name(
            tournament_name
        )
        tournament_uuid: str = tournament_object.uuid

        menu: str = str(tournament_name) + " Stats"
        user_path: list[MenuOptions] = [
            MenuOptions.SPECTATE_SCREEN,
            MenuOptions.SPECTATE_TOURNAMENTS,
            MenuOptions.ACTIVE_TOURNAMENT,
            MenuOptions.GAME_SCHEDULE,
        ]
        info: list[str] = self.utility.list_matches(tournament_uuid, False)
        options: dict[str, str] = {}
        message: str = ""

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options, message))
        input("Press Any Key To Go Back")
        return MenuOptions.ACTIVE_TOURNAMENT

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
            MenuOptions.SPECTATE_SCREEN,
            MenuOptions.SPECTATE_TOURNAMENTS,
            MenuOptions.ACTIVE_TOURNAMENT,
            MenuOptions.TEAMS_IN_TOURNAMENT,
        ]

        unique_names: list[str] = teams_in_tournament

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
            return MenuOptions.TEAM_TOURNAMENT_STATS

        # ---------- INVALID NAME ----------

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options, message))

        match self.utility.prompt_choice(["t", "b"]):
            case "t":
                return MenuOptions.TEAMS_IN_TOURNAMENT

        return MenuOptions.ACTIVE_TOURNAMENT

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
            MenuOptions.SPECTATE_TOURNAMENTS,
            MenuOptions.ACTIVE_TOURNAMENT,
            MenuOptions.TEAMS_IN_TOURNAMENT,
            MenuOptions.TEAM_TOURNAMENT_STATS,
        ]

        info_a: list[str] = [
            "Club: " + LogicLayerAPI.get_team_club(team_name),
            "Wins: " + LogicLayerAPI.get_team_wins(team_name),
            "Points: " + LogicLayerAPI.get_team_points(team_name),
        ]
        info_b: list[str] = [
            f"Team Members:\n{80 * '-'}"
        ] + self.utility.string_to_table(
            self.utility.object_to_string(
                LogicLayerAPI.get_team_members_object(team_name)
            )
        )

        # Table design

        info: list[str] = info_a + info_b
        options: dict[str, str] = {}
        message: str = ""

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options, message))
        input("Press Any Key To Go Back")
        return MenuOptions.TEAMS_IN_TOURNAMENT
