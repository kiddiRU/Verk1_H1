"""
Author: Ísak Elí Hauksson <isak25@ru.is>
Date: 2025-12-04

File that holds all the menus that the spectator can access
"""

from UILayer.MenuOptions import MenuOptions
from UILayer.UtilityUI import UtilityUI


class SpectateUI:
    """Every spectate menu option"""

    def __init__(self) -> None:
        self.utility = UtilityUI()

    def spectate_screen(self) -> MenuOptions:
        """Spectate screen, choices: 1,2,3 and b
        1: Check players
        2: Check clubs
        3: Check teams
        4: Check tournaments
        b: Back to start page

        Returns:
            MenuOptions: The next menu to navigate to
        """
        print("")

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
                return MenuOptions.main_menu

        return MenuOptions.main_menu

    def spectate_players(self) -> MenuOptions:
        """Spectate players screen, choices: input a player to view stats

        Returns:
            MenuOptions: The next menu to navigate to
        """
        # TODO: implement search player functionality
        print("")
        return MenuOptions.spectate_screen

    def view_player_stats(self) -> MenuOptions:
        """View player stats screen, choices: b
        b: back to spectate players screen

        Returns:
            MenuOptions: The next menu to navigate to
        """
        print("This is the view player stats page")
        return MenuOptions.spectate_screen

    def spectate_clubs(self) -> MenuOptions:
        """Spectate clubs screen, choices: input a club to view stats

        Returns:
            MenuOptions: The next menu to navigate to
        """
        print("This is the spectate clubs page")
        print("<list of clubs>")

        return MenuOptions.spectate_screen

    def view_club_stats(self) -> MenuOptions:
        """View club stats screen, choices: b
        b: back to spectate players screen

        Returns:
            MenuOptions: The next menu to navigate to
        """
        print("This is the view club stats page")
        return MenuOptions.spectate_screen

    def spectate_teams(self) -> MenuOptions:
        """Spectate teams screen, choices: input a team to view stats

        Returns:
            MenuOptions: The next menu to navigate to
        """
        print("This is the spectate teams page")
        print("<list of teams>")

        return MenuOptions.spectate_screen

    def view_team_stats(self) -> MenuOptions:
        """View team stats screen, choices: b
        b: back to spectate players screen

        Returns:
            MenuOptions: The next menu to navigate to
        """
        print("This is the view team stats page")
        return MenuOptions.spectate_screen

    def spectate_tournaments(self) -> MenuOptions:
        """Spectate tournaments screen, choices: input a tournament to view


        Returns:
            MenuOptions: The next menu to navigate to
        """
        print("This is the spectate tournaments page")
        print("<list of tournaments>")

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
        print("This is the active tournament page")
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
        return MenuOptions.spectate_tournaments

    def game_schedule(self) -> MenuOptions:
        """Game schedule screen, choices: b
        b: back to active tournament screen

        Returns:
            MenuOptions: The next menu to navigate to
        """
        print("This is the game schedule page")
        return MenuOptions.active_tournament

    def view_bracket(self) -> MenuOptions:
        """View bracket screen, choices: b
        b: back to active tournament screen

        Returns:
            MenuOptions: The next menu to navigate to
        """
        print("This is the view bracket page")
        return MenuOptions.active_tournament

    def teams_in_tournament(self) -> MenuOptions:
        """Teams in tournament screen, choices: input a team to view stats

        Returns:
            MenuOptions: The next menu to navigate to
        """
        print("This is the teams in tournament page")
        print("<list of teams in tournament>")

        return MenuOptions.active_tournament

    def team_tournament_stats(self) -> MenuOptions:
        """Team tournament stats screen, choices: b
        b: back to teams in tournament screen

        Returns:
            MenuOptions: The next menu to navigate to
        """
        print("This is the team tournament stats page")
        return MenuOptions.teams_in_tournament
