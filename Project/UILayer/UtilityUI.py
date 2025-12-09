"""
Author: Ísak Elí Hauksson <isak25@ru.is>
Date: 2025-12-03

Co-Author: Andri Már Kristjánsson <andrik25@ru.is>,
Sindri Freysson <Sindrif25@ru.is>

File that holds the UtilityUI class
which holds functions used in multiple places
"""

from Models.Player import Player
from Models.Club import Club
from Models.Team import Team
from Models.Tournament import Tournament

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
                valid: str | None = validate(attribute, choice, info_type)
                return str(valid)
            except ValidationError as e:
                print(self.error_color + str(e) + self.reset)
                continue

    # Created by Sindri Freysson
    def prompt_builder(options: list[str]) -> dict[int, str]:
        """
        Helper function that takes in list of MenuOptions and returns an enumerated dictionary of options
        Use dict.update after building if you want to add extra options to the menu
        :param options: List of strings representing the options that the user can use
        :return: Dictionary of options -> string
        """
        prompt_dict: dict[int|str, str] = {}
        for i, choice in enumerate(options, start=1):
            prompt_dict[i] = choice
        return prompt_dict
    # Created by Sindri Freysson
    def prompt_choice(self, valid_choices: dict[int|str, str]) -> str:
        """
        Takes in a list of valid choices and returns a string representing the choice
        :param self:
        :param valid_choices: Dictionary of valid choices that the user can input
        :return: Returns a string of the allowed choice
        """
        while True:
            choice: str = input("> ").strip().lower()
            if choice in valid_choices:
                return valid_choices[choice]
            print(
                self.error_color + "Not a valid option try again" + self.reset
            )

    def _input_change(self, message: str, attribute: str, info_type: str) -> str:
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
                if not choice:
                    return choice
                valid: str | None = validate(attribute, choice, info_type)
                return str(valid)
            except ValidationError as e:
                print(self.error_color + str(e) + self.reset)
                continue


    def screen_not_exist_error(self) -> MenuOptions:
        """When a screen doesn't exist"""
        print("Screen doesn't exist")
        input("Input anything to go back to start: ")
        return MenuOptions.start_screen

    def show_schedule(self):
        pass

    def search_for_player(self):
        # TODO: Get logic from LL
        pass


    # -----------------------------------------------

    # def show_specific_tournament(self, tournament_name):
    #     pass

    # def show_specific_team(self, team_name: str) -> Team | None:
    #     team_list: list[Team] = LogicLayerAPI.list_teams()
    #     team_names = [x.name for x in team_list]
    #     team_uuids = [x.uuid for x in team_list]

    #     for index, name in enumerate(team_names):
    #         if name == team_name:
    #             return LogicLayerAPI.get_team_object(team_uuids[index])

    # def show_specific_club(self, club_name: str) -> Club | None:
    #     """
    #     Get Club object from club name

    #     Args:
    #         club_name (str): unique name of a club

    #     Returns:
    #         Club | None: Club object of club is found else return None
    #     """
    #     club_list: list[Club] = LogicLayerAPI.list_clubs()

    #     for club in club_list:
    #         if club.name == club_name:
    #             return club

    # def show_specific_player(self, player_handle: str) -> Player | None:
    #     """
    #     Get specific player object based on player handle

    #     Args:
    #         player_handle (str): Handle of a player

    #     Returns:
    #         Player | None: Player object if player is found else returns None
    #     """
    #     player_list: list[Player] = LogicLayerAPI.list_players()

    #     for p in player_list:
    #         if p.handle == player_handle:
    #             return p
    #     return None

    # _____________________________ MODULAR DESIGN ___________________________

    def tournaments_name(self) -> list[str]:
        """
        Converts list of Tournament objects to a list of Tournament names

        Returns:
            list[str]: Tournament names
        """
        tournaments: list[Tournament] = LogicLayerAPI.list_tournaments()
        return [x.name for x in tournaments]

    def except_status_tournaments(
        self, tournament_status: Tournament.StatusType
    ) -> list[str]:
        """
        Returns a list of tournaments that do not have the inputted status

        Args:
            tournament_status (Tournament.StatusType): Status that is not supposed to be in the tournament list

        Returns:
            list[str]: list of tournaments without the inputted status
        """
        tournaments: list[Tournament] = LogicLayerAPI.list_tournaments()
        return [x.name for x in tournaments if x.status != tournament_status]

    def team_names(self) -> list[str]:
        """
        Converts list of Team objects to a list of Team names

        Returns:
            list[str]: Team names
        """
        team_list: list[Team] = LogicLayerAPI.list_teams()
        return [x.name for x in team_list]

    def club_names(self):
        """
        Converts list of Club objects to a list of Club names

        Returns:
            list[str]: Club names
        """
        clubs: list[Club] = LogicLayerAPI.list_clubs()
        return [x.name for x in clubs]

    def player_handles(self) -> list[str]:
        """
        Converts list of Player objects to a list of Player handles

        Returns:
            list[str]: PLayer handles
        """
        player_list: list[Player] = LogicLayerAPI.list_players()
        return [p.handle for p in player_list]

    def show_main(self, flag: str) -> list[str]:
        """
        Modular design to make a list of players, clubs and teams

        Args:
            flag (str): "players", "clubs", "teams"

        Returns:
            list[str]: A list of f-strings for printing
        """
        flag_dict = {
            "players": self.player_handles(),
            "clubs": self.club_names(),
            "teams": self.team_names(),
        }

        unique_names: list[str] = flag_dict[flag]

        output_list: list[str] = []  # list that holds each line as a f-string

        length: int = len(unique_names)

        for value in range(0, len(unique_names), 2):
            left = unique_names[value]
            if value + 1 < length:

                right = unique_names[value + 1]
                output_list.append(f"{left:<39}|{right:<39}|")

            else:  # odd number, last item has no pair
                output_list.append(f"{left:<39}|{" ":<39}|")

        return output_list

    def show_tournaments_except_status(
        self, tournament_status: Tournament.StatusType
    ) -> list[str]:
        """
        An f-string to show tournaments that do not have the status

        Args:
            tournament_status (Tournament.StatusType): active, inactive, archived

        Returns:
            list[str]: a list of f-strings to show tournaments without specific status
        """
        tournaments: list[Tournament] = LogicLayerAPI.list_tournaments()

        output_list: list[str] = []  # list that holds each line as a f-string

        for t in tournaments:
            if t.status == tournament_status:
                continue
            output_list.append(f"{t.name:<68}>{t.status:^10}|")
        return output_list
