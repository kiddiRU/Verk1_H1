"""
Author: Ísak Elí Hauksson <isak25@ru.is>
Date: 2025-12-04

Minor changes: Andri Már Kristjánsson <andrik25@ru.is>

File that holds all the menus that the spectator can access
"""

from Models.Tournament import Tournament
from Models.Player import Player
from Models.Team import Team

from UILayer.MenuOptions import MenuOptions
from UILayer.UtilityUI import UtilityUI
from UILayer.Drawer import Drawer

from LogicLayer import LogicLayerAPI


class SpectateUI:
    """
    Handles all menu options related to spectating
    players, teams, clubs, and tournaments.
    """

    def __init__(self) -> None:
        """
        Initializes the SpectateUI controller.

        Sets up the utility UI, drawer interface, and basic formatting
        attributes for displaying spectating menus.
        """
        # Utility helper for inputs and other reusable functions
        self.utility: UtilityUI = UtilityUI()
        self.tui: Drawer = Drawer()  # Draw interface for tables and menus
        self.message_color: str = "\033[36m"  # Cyan color for messages
        self.reset: str = "\033[0m"  # Reset color
        self.underscore: str = "\033[4m"  # Underline formatting
        self.green: str = "\033[32m"  # Green color
        self.temp_team: str = ""

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
        """
        Main spectate menu screen.

        Allows the user to choose which type of entity to view,
        such as players, clubs, teams, or tournaments.

        :return: The next menu option to navigate to.
        :rtype: MenuOptions
        """

        # UI Setup
        menu: str = "Spectate Players"
        user_path: list[MenuOptions] = [
            MenuOptions.SPECTATE_SCREEN,
            MenuOptions.SPECTATE_PLAYERS,
        ]
        info: list[str] = self.utility.show_main("players")
        options: dict[str, str] = {"t": "Try Again", "b": "Back"}
        message: str = "Player Not Found!"

        # Clear previous UI data and display table
        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info))

        # Prompt user for player handle
        find_handle: str = input(
            self.message_color
            + "Input Handle or 'q' to cancel:\n"
            + self.reset
        )
        if find_handle == "q":
            return user_path[-2]  # Go back to previous menu

        # If handle exists, save and navigate to player stats
        if find_handle in self.utility.player_handles():
            LogicLayerAPI.save_player(find_handle)
            return MenuOptions.VIEW_PLAYER_STATS

        # Handle invalid input
        print(self.tui.table(menu, user_path, info, options, message))
        choice: str = self.utility.prompt_choice(["t", "b"])
        match choice:
            case "t":
                return MenuOptions.SPECTATE_PLAYERS

        return MenuOptions.SPECTATE_SCREEN

    def view_player_stats(self) -> MenuOptions:
        """
        Display the selected player's statistics.

        Shows the team, wins, and points of the player previously selected
        in the spectate menu. User can press enter to return to the
        Spectate Players screen.

        :return: The next menu option to navigate to.
        :rtype: MenuOptions
        """

        # Retrieve the handle of the player selected previously
        player_handle: str | None = LogicLayerAPI.save_player()
        player: Player | str = LogicLayerAPI.get_player_by_handle(
            str(player_handle))
        if not isinstance(player, Player):
            return MenuOptions.SPECTATE_TEAMS

        if player_handle is None:
            return MenuOptions.SPECTATE_SCREEN

        # UI Setup
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
            "URL: " + str(player.url),
            "Wins: " + LogicLayerAPI.get_player_wins(player_handle),
            "Points: " + LogicLayerAPI.get_player_points(player_handle),
        ]
        options: dict[str, str] = {}
        message: str = ""

        # Clear UI and display table
        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options, message))

        # Wait for user input before returning
        input("Press Enter To Go Back")
        return MenuOptions.SPECTATE_SCREEN

    def spectate_clubs(self) -> MenuOptions:
        """
        Display a list of clubs for the user to select and view stats.

        Allows the user to input a club name to view its statistics.
        User can also cancel or retry if the input is invalid.

        :return: The next menu option to navigate to.
        :rtype: MenuOptions
        """

        # UI Setup
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

        # Prompt user for club selection
        find_club: str = input(
            self.message_color
            + "Input Club Name or 'q' to cancel:\n"
            + self.reset
        )
        if find_club == "q":
            return user_path[-2]  # Go back to previous menu

        if find_club in self.utility.club_names():
            LogicLayerAPI.save_player(find_club)
            return MenuOptions.VIEW_CLUB_STATS

        # Show error message if club not found
        print(self.tui.table(menu, user_path, info, options, message))
        choice: str = self.utility.prompt_choice(["t", "b"])

        match choice:
            case "t":
                return MenuOptions.SPECTATE_CLUBS

        return MenuOptions.SPECTATE_SCREEN

    def view_club_stats(self) -> MenuOptions:
        """
        Display statistics for a selected club.

        Shows teams in the club, club color, total wins, and points.
        User can only go back to the spectate clubs screen.

        :return: The next menu option to navigate to.
        :rtype: MenuOptions
        """

        # Retrieve the currently selected club
        club_name: str | None = LogicLayerAPI.save_player()
        if club_name is None:
            return MenuOptions.SPECTATE_SCREEN

        menu: str = f"{club_name} Stats"
        user_path: list[MenuOptions] = [
            MenuOptions.SPECTATE_SCREEN,
            MenuOptions.SPECTATE_CLUBS,
            MenuOptions.VIEW_CLUB_STATS,
        ]

        # Build display info for the club's teams
        info_a: list[str] = [
            f"Teams:\n{80 * '—'}"
        ] + self.utility.string_to_table(
            self.utility.object_to_string(
                LogicLayerAPI.get_teams_in_club(club_name)
            )
        )

        # Build display info for club stats
        info_b: list[str] = [
            f"{80 * '—'}\n"
            "Color: " + LogicLayerAPI.get_club_by_name(club_name).club_color,
            "Wins: " + LogicLayerAPI.get_club_wins(club_name),
            "Points: " + LogicLayerAPI.get_club_points(club_name),
        ]

        # Combine all info for display
        info = info_a + info_b
        options: dict[str, str] = {}

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options))
        input("Press Enter To Go Back")

        return MenuOptions.SPECTATE_SCREEN

    def spectate_teams(self) -> MenuOptions:
        """
        Display a list of teams for the spectator to choose from.

        Spectator can input a team name to view its stats or cancel.
        Provides feedback if the team is not found.

        :return: The next menu option to navigate to.
        :rtype: MenuOptions
        """

        # Setup UI
        menu: str = "Teams"
        user_path: list[MenuOptions] = [
            MenuOptions.SPECTATE_SCREEN,
            MenuOptions.SPECTATE_TEAMS,
        ]
        # Retrieve a formatted list of all team
        list_table: list[str] = self.utility.show_main("teams")

        info: list[str] = list_table
        options: dict[str, str] = {"t": "Try Again", "b": "Back"}
        message: str = "Team Not Found!"

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info))

        # Prompt the user to input a team name or cancel
        find_team: str = input(
            self.message_color
            + "Input Team Name or 'q' to cancel:\n"
            + self.reset
        )
        if find_team == "q":
            return user_path[-2]  # Go back to previous menu

        # Check if the team exists
        if find_team in self.utility.team_names():
            LogicLayerAPI.save_player(find_team)
            return MenuOptions.VIEW_TEAM_STATS

        # Show error message if team not found
        print(self.tui.table(menu, user_path, info, options, message))
        choice: str = self.utility.prompt_choice(["t", "b"])
        match choice:
            case "t":
                return MenuOptions.SPECTATE_TEAMS

        return MenuOptions.SPECTATE_SCREEN

    def view_team_stats(self) -> MenuOptions:
        """
        Display detailed statistics for a selected team.

        Shows the team's club, wins, points, members, and tournament history.
        Spectator can view this information and press enter to return.

        :return: The next menu option to navigate to.
        :rtype: MenuOptions
        """

        # Remembers what player chosen in spectate_players
        team_name: str | None = LogicLayerAPI.save_player()
        team: Team = LogicLayerAPI.get_team_by_name(str(team_name))
        if team_name is None:
            return MenuOptions.SPECTATE_SCREEN

        # UI Setup
        menu: str = str(team_name) + " Stats"
        user_path: list[MenuOptions] = [
            MenuOptions.SPECTATE_SCREEN,
            MenuOptions.SPECTATE_TEAMS,
            MenuOptions.VIEW_TEAM_STATS,
        ]

        # Stats: Clubs, Wins and Points
        info_stats: list[str] = [
            "ASCII Art: " + str(team.ascii_art),
            "URL: " + str(team.url_homepage),
            "Club: " + LogicLayerAPI.get_team_club(team_name),
            "Wins: " + LogicLayerAPI.get_team_wins(team_name),
            "Points: " + LogicLayerAPI.get_team_points(team_name),
        ]

        # Team members
        info_members: list[str] = [
            f"Team Members:\n{80 * '—'}"
        ] + self.utility.string_to_table(
            self.utility.object_to_string(
                LogicLayerAPI.get_team_members_object(team_name)
            )
        )

        # Tournament history
        info_history: list[str] = (
            [f"{80 * '—'}"]
            + [f"Tournament History:\n{80 * '—'}"]
            + self.utility.string_to_table(
                LogicLayerAPI.get_team_history(team_name)
            )
        )

        # Combine all info sections
        info: list[str] = info_stats + info_members + info_history
        options: dict[str, str] = {}

        # Display the table
        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options))

        input("Press Enter To Go Back")
        return MenuOptions.SPECTATE_SCREEN

    def spectate_tournaments(self) -> MenuOptions:
        """
        Display a list of tournaments for spectators and allow selection.

        Shows all tournaments except those with inactive status.
        Spectator can input a tournament name to view its details or
        go back to the previous menu.

        :return: The next menu option to navigate to.
        :rtype: MenuOptions
        """

        # UI Setup
        menu: str = "Tournaments"
        user_path: list[MenuOptions] = [
            MenuOptions.SPECTATE_SCREEN,
            MenuOptions.SPECTATE_TOURNAMENTS,
        ]

        # List tournaments excluding inactive ones
        info: list[str] = self.utility.show_tournaments_except_status(
            Tournament.StatusType.INACTIVE
        )
        options: dict[str, str] = {"t": "Try Again", "b": "Back"}
        message: str = "Tournament Not Found!"

        # Show initial table
        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info))

        # User input
        tournament_name = input(
            self.message_color
            + "Input Tournament Name or 'q' to cancel:\n"
            + self.reset
        )
        if tournament_name == "q":
            return user_path[-2]  # Go back to previous menu

        tournament_list: list[Tournament] = LogicLayerAPI.list_tournaments()
        not_inactive: list[str] = self.utility.except_status_tournaments(
            Tournament.StatusType.INACTIVE
        )

        # Validate tournament name
        if tournament_name in not_inactive:
            LogicLayerAPI.save_player(tournament_name)

            # Find the tournament object by name
            tournament_object = None
            for tournament in tournament_list:
                if tournament.name == tournament_name:
                    tournament_object = tournament
                    break

            if tournament_object:
                return (
                    MenuOptions.ACTIVE_TOURNAMENT
                    if tournament_object.status == Tournament.StatusType.ACTIVE
                    else MenuOptions.ARCHIVED_TOURNAMENT
                )

        # Invalid name show error message
        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options, message))

        match self.utility.prompt_choice(["t", "b"]):
            case "t":
                return MenuOptions.SPECTATE_TOURNAMENTS

        return MenuOptions.SPECTATE_SCREEN

    def active_tournament(self) -> MenuOptions:
        """
        Display an active tournament's overview for spectators.

        Shows the tournament name and allows spectators to view
        either the game schedule or the participating teams.

        :return: The next menu option to navigate to.
        :rtype: MenuOptions
        """

        # Get the currently selected tournament name
        tournament_name: str | None = LogicLayerAPI.save_player()

        # UI Setup
        menu: str = str(tournament_name) + " Stats"
        user_path: list[MenuOptions] = [
            MenuOptions.SPECTATE_SCREEN,
            MenuOptions.SPECTATE_TOURNAMENTS,
            MenuOptions.ACTIVE_TOURNAMENT,
        ]
        info: list[str] = []
        options: dict[str, str] = {
            "1": "Game Info And Schedule",
            "2": "Teams",
            "b": "Back",
        }

        # Clear previous table and display current
        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options))

        # Prompt for user input
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
        """
        Display an archived tournament's details for spectators.

        Shows all matches in the tournament and highlights
        the tournament winner.

        :return: The next menu option to navigate to.
        :rtype: MenuOptions
        """

        # Get the currently selected tournament name
        tournament_name: str | None = LogicLayerAPI.save_player()
        if tournament_name is None:
            return MenuOptions.START_SCREEN

        # Get the tournament object and its UUID
        tournament_object = LogicLayerAPI.get_tournament_by_name(
            tournament_name
        )
        tournament_uuid: str = tournament_object.uuid

        # UI Setup
        menu: str = str(tournament_name) + " Stats"
        user_path: list[MenuOptions] = [
            MenuOptions.SPECTATE_SCREEN,
            MenuOptions.SPECTATE_TOURNAMENTS,
            MenuOptions.ARCHIVED_TOURNAMENT,
        ]

        # List all matches in the tournament
        match_list: list[str] = self.utility.list_matches(
            tournament_uuid, True
        )

        # Extract tournament winner from the last match
        match_split = match_list[0].split("\n")
        tournament_winner: str = (
            match_split[-1].replace("Match Winner: ", "").rstrip("|").strip()
        )

        # Format winner display
        win: str = "Tournament Winner:"
        tournament_winner_formatted: list[str] = [
            (80 * "—"),
            f"{f'{self.green}{win} {tournament_winner} {self.reset}':<88}|",
        ]

        # Combine match list with winner display
        info: list[str] = match_list + tournament_winner_formatted

        options: dict[str, str] = {}
        message: str = ""

        # Clear previous table data and display current table
        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options, message))

        input("Press Enter To Go Back")

        return MenuOptions.SPECTATE_SCREEN

    def game_schedule(self) -> MenuOptions:
        """
        Display the game schedule for the currently active tournament.

        Shows all scheduled matches for the tournament. Spectators can view the
        match list but cannot make changes.

        :return: The next menu option to navigate to.
        :rtype: MenuOptions
        """

        # Retrieve the currently selected tournament
        tournament_name: str | None = LogicLayerAPI.save_player()
        if tournament_name is None:
            return MenuOptions.START_SCREEN

        # Get the tournament object and its UUID
        tournament_object = LogicLayerAPI.get_tournament_by_name(
            tournament_name
        )
        tournament_uuid: str = tournament_object.uuid

        # Setup UI
        menu: str = str(tournament_name) + " Stats"
        user_path: list[MenuOptions] = [
            MenuOptions.SPECTATE_SCREEN,
            MenuOptions.SPECTATE_TOURNAMENTS,
            MenuOptions.ACTIVE_TOURNAMENT,
            MenuOptions.GAME_SCHEDULE,
        ]
        # Retrieve the list of matches for the tournament
        match_list: list[str] = self.utility.list_matches(
            tournament_uuid, False
        )

        info: list[str] = match_list

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info))

        input("Press Enter To Go Back")

        return MenuOptions.SPECTATE_SCREEN

    def teams_in_tournament(self) -> MenuOptions:
        """
        Display all teams in the currently active tournament and allow the
        user to select a team to view its stats.

        Teams are shown in a two-column table for readability. Users can type
        a team name to view details, or cancel to go back.

        :return: The next menu option to navigate to.
        :rtype: MenuOptions
        """

        # Retrieve the current tournament
        tournament_name: str = LogicLayerAPI.save_player() or "None"

        # List all teams in the tournament
        teams_in_tournament: list[str] = [
            t.name
            for t in LogicLayerAPI.get_teams_from_tournament_name(
                tournament_name
            )
        ]

        # Menu UI
        menu: str = f"Teams in {tournament_name}"
        user_path: list[MenuOptions] = [
            MenuOptions.SPECTATE_SCREEN,
            MenuOptions.SPECTATE_TOURNAMENTS,
            MenuOptions.ACTIVE_TOURNAMENT,
            MenuOptions.TEAMS_IN_TOURNAMENT,
        ]

        # Format teams into two-column table for display
        output_list: list[str] = []  # list that holds each line as a f-string
        length: int = len(teams_in_tournament)

        for value in range(0, length, 2):
            left = teams_in_tournament[value]
            if value + 1 < length:
                right = teams_in_tournament[value + 1]
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
            + "Input Team Name or 'q' to cancel:\n"
            + self.reset
        ).strip()

        if team_name.lower() == "q":
            return user_path[-2]  # Go to last screen

        # Validate team name
        if team_name in teams_in_tournament:
            # Save selected team for the next screen
            self.temp_team: str = team_name
            return MenuOptions.TEAM_TOURNAMENT_STATS

        # Invalid name, show error message
        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options, message))

        match self.utility.prompt_choice(["t", "b"]):
            case "t":
                return MenuOptions.TEAMS_IN_TOURNAMENT

        return MenuOptions.ACTIVE_TOURNAMENT

    def team_tournament_stats(self) -> MenuOptions:
        """
        Display detailed stats for a specific team within a tournament.

        Shows the team's club, total wins, points, and a list of team members.
        Allows the user to view all information in
        a formatted table and go back.

        :return: The next menu option to navigate to.
        :rtype: MenuOptions
        """

        # Get the team selected in the previous screen
        team_name = self.temp_team

        # UI Setup
        menu: str = str(team_name) + " Stats"
        user_path: list[MenuOptions] = [
            MenuOptions.SPECTATE_TOURNAMENTS,
            MenuOptions.ACTIVE_TOURNAMENT,
            MenuOptions.TEAMS_IN_TOURNAMENT,
            MenuOptions.TEAM_TOURNAMENT_STATS,
        ]

        # Get stat information
        info_stats: list[str] = [
            "Club: " + LogicLayerAPI.get_team_club(team_name),
            "Wins: " + LogicLayerAPI.get_team_wins(team_name),
            "Points: " + LogicLayerAPI.get_team_points(team_name),
        ]
        # Get team members to be displayed
        info_team_members: list[str] = [
            f"Team Members:\n{80 * '-'}"
        ] + self.utility.string_to_table(
            self.utility.object_to_string(
                LogicLayerAPI.get_team_members_object(team_name)
            )
        )

        # Combine info sections
        info: list[str] = info_stats + info_team_members

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info))

        input("Press Enter To Go Back")

        return MenuOptions.TEAMS_IN_TOURNAMENT
