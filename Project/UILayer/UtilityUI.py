"""
Author: Ísak Elí Hauksson <isak25@ru.is>
Date: 2025-12-03

Co-Author: Andri Már Kristjánsson <andrik25@ru.is>,
Sindri Freysson <Sindrif25@ru.is>

File that holds the UtilityUI class
which holds functions used in multiple places
"""

from Models.Player import Player
from Models.Team import Team

from UILayer.MenuOptions import MenuOptions
from LogicLayer.LogicLayerAPI import validate
from Models import ValidationError
from LogicLayer import LogicLayerAPI


class UtilityUI:
    """Utility Class for multi use function for ui layer"""

    def __init__(self) -> None:
        self.error_color: str = "\033[31m"
        self.message_color: str = "\033[36m"
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

            print(
                self.error_color + "Not a valid option try again" + self.reset
            )

    # Created by Sindri
    def _input_info(self, message: str, attribute: str, info_type: str) -> str:
        """
        Helper function that repeats input until it is valid or navigation word is entered
        :param message: message to display - "Enter Your name"
        :param attribute: attribute of a model class - "name"
        :param info_type: information type - "PLAYER"
        :return: Repeats until the input is valid or navigation word is entered
        """
        while True:
            try:
                print(self.message_color + message + self.reset)
                choice: str = input()
                if choice.strip().lower() in ["c", "b"]:
                    return choice
                valid = validate(attribute, choice, info_type)
                return valid
            except ValidationError as e:
                print(self.error_color + str(e) + self.reset)
                continue

    def screen_not_exist_error(self) -> MenuOptions:
        """When a screen doesn't exist"""
        print("Screen doesn't exist")
        input("Input anything to go back to start: ")
        return MenuOptions.start_screen

    def search_for_player(self):
        # TODO: Get logic from LL
        pass

    def show_tournaments(self):
        pass

    def show_specific_tournament(self, tournament_name):
        pass

    def show_all_team_names(self):
        # team_list: list[Team] = LogicLayerAPI.
        pass

    def show_specific_team(self, team_name):
        print("My team: players in team:")

    def show_clubs(self):
        pass

    def show_specific_club(self):
        pass

    def show_all_player_handles(self) -> list[str]:
        """Returns a list of all player handles formatted neatly to be printed

        Returns:
            list[str]: A list of f-strings for printing
        """
        player_list: list[Player] = LogicLayerAPI.list_players()

        handle_list: list[str] = [p.handle for p in player_list]

        output_list: list[str] = []  # list that holds each line as a f-string

        for value in range(0, len(handle_list), 2):
            try:
                output_list.append(
                    f"{handle_list[value]:<{39}}||{handle_list[value + 1]:>{39}}"
                )
            except IndexError:  # IF there is an odd amount of players
                output_list.append(f"{handle_list[-1]:<{39}}||")

        return output_list

# TODO: MOVE THIS SHIT INTO THE LL
    def show_specific_player(self, player_handle: str) -> Player | None:
        """
        Get specific player object based on player handle

        Args:
            player_handle (str): handle of a player

        Returns:
            Player | None: _description_
        """
        player_list: list[Player] = LogicLayerAPI.list_players()

        for p in player_list:
            if p.handle == player_handle:
                return p
        
        return None

    def show_schedule(self):
        pass
