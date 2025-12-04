"""
Author: Ísak Elí Hauksson <isak25@ru.is>
Date: 2025-12-03

File that holds the UtilityUI class
which holds functions used in multiple places
"""
from UILayer.MenuOptions import MenuOptions

class UtilityUI:
    """ Utility Class for multi use function for ui layer """

    def _prompt_choice(self, valid_choices: list[str]) -> str:
        """
        Helper function for allowed choices for the user

        Args:
            valid_choices (list[str]): A list of valid choices for the user to input

        Returns:
            str: _description_
        """
        valid_choices_lower: list[str] = [x.lower() for x in valid_choices]

        while True:
            choice: str = input("> ").strip().lower()
            if choice in valid_choices_lower:
                return choice

            print("Not a valid option try again")

    def _input_info(self, message: str) -> str:
        """
        A helper function for inputted string that checks for too long strings

        Args:
            message (str): The input message to the user

        Returns:
            str: The input from the user
        """
        while True:
            choice: str = input(message)
            if len(choice) >= 3 and len(choice) <= 40:
                return choice.strip()
            print("Not a valid length")

    def screen_exist_error(self) -> MenuOptions:
        """ When a screen doesn't exist """
        print("Screen doesn't exist")
        anything: str = input("Input anything to go back to start: ")
        return MenuOptions.main_menu
    
    def show_tournaments(self):
        pass

    def show_specific_tournament(self, tournament_name):
        pass

    def show_teams(self):
        pass

    def show_specific_team(self, team_name):
        print("My team: players in team:")

    def show_clubs(self):
        pass

    def show_players(self):
        pass

    def show_specific_player(self):
        pass

    def show_schedule(self):
        pass
