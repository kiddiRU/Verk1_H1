"""
Author: Ísak Elí Hauksson <isak25@ru.is>
Date: 2025-12-03

Co-Author: Andri Már Kristjánsson <andrik25@ru.is>,
Sindri Freysson

File that holds the UtilityUI class
which holds functions used in multiple places
"""

from UILayer.MenuOptions import MenuOptions
from LogicLayer.LogicLayerAPI import validate
from Models import ValidationError

class UtilityUI:
    """Utility Class for multi use function for ui layer"""


    def __init__(self) -> None:
        self.error_color: str = "\033[31m"
        self.reset: str = "\033[0m"

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

            print(self.error_color + "Not a valid option try again" + self.reset)

    # Created by Sindri
    def _input_info(self, message, attribute: str, info_type: str) -> str | None:
        """
        Helper function that repeats input until it is valid or navigation word is entered
        :param message: message to display - "Enter Your name"
        :param attribute: attribute of a model class - "name"
        :param info_type: information type - "PLAYER"
        :return: Repeats until the input is valid or navigation word is entered
        """
        while True:
            try:
                print(message)
                choice: str = input()
                if choice.strip().lower() in ["c", "b"]:
                    return choice
                valid = validate(attribute, choice, info_type)
                return valid
            except ValidationError as e:
                print(self.error_color + e + self.reset)
                continue




    def screen_not_exist_error(self) -> MenuOptions:
        """When a screen doesn't exist"""
        print("Screen doesn't exist")
        anything: str = input("Input anything to go back to start: ")
        return MenuOptions.start_screen

    def search_for_player(self):
        # TODO: Get logic from LL
        pass

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