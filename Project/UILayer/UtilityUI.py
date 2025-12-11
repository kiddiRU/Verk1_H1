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
from Models.Match import Match

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

    def prompt_choice(self, valid_choices: list[str]) -> str:
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
    def input_info(self, message: str, attribute: str, info_type: str) -> str:
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
                if choice.lower() == "q":
                    return ""
                valid: str | None = validate(attribute, choice, info_type)
                return str(valid)
            except ValidationError as e:
                print(self.error_color + str(e) + self.reset)
                continue

    def input_change(
        self, message: str, attribute: str, info_type: str
    ) -> str:
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
                if choice.lower() == "q":
                    return choice
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
        team_list: list[Team] = LogicLayerAPI.list_all_teams()
        return [x.name for x in team_list]

    def club_names(self):
        """
        Converts list of Club objects to a list of Club names

        Returns:
            list[str]: Club names
        """
        clubs: list[Club] = LogicLayerAPI.list_all_clubs()
        return [x.name for x in clubs]

    def player_handles(self) -> list[str]:
        """
        Converts list of Player objects to a list of Player handles

        Returns:
            list[str]: PLayer handles
        """
        player_list: list[Player] = LogicLayerAPI.list_all_players()
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

        for tournament in tournaments:
            if tournament.status == tournament_status:
                continue
            output_list.append(
                f"{tournament.name:<68}>{tournament.status:^10}|"
            )
        return output_list

    def list_matches(self, tournament_uuid: str, show_all: bool) -> list[str]:
        """
        Function to show either all matches in a tournament or the next matches
        
        :param self: Description
        :param tournament_uuid: The uuid of a tournament
        :type tournament_uuid: str
        :param show_all: Description
        :type show_all: Choose if you want to show all matches in the tournament
        :return: A formatted f-string to be printed out
        :rtype: list[str]
        """

        if show_all:
            match_list: list[Match] = LogicLayerAPI.get_all_matches(
                tournament_uuid
            )
        else:
            match_list: list[Match] = LogicLayerAPI.get_next_matches(
                tournament_uuid
            )
        # Top info

        line = lambda x: x * 80
        output_list: list[str] = []

        for match in match_list:

            match_winner_uuid: str = str(match.winner)
            if match_winner_uuid != "None":
                match_winner_team: Team = LogicLayerAPI.get_team_by_uuid(match_winner_uuid)
                match_winner_name: str = match_winner_team.name
            else: match_winner_name: str = match_winner_uuid

            

            if show_all:
                revealed: str = "To be revealed"
                if (match.team_1 or match.team_2) == revealed:
                    continue

                match1: Team = LogicLayerAPI.get_team_by_uuid(match.team_1)
                match2: Team = LogicLayerAPI.get_team_by_uuid(match.team_2)

                match_name_1: str = match1.name
                match_name_2: str = match2.name

                output_list.append(
                    f"{line('—')}\n"
                    f"{f"Date: {match.match_date}":<79}|\n"
                    f"{f"Match Time: {str(match.match_time)}":<79}|\n"
                    f"{f"Team 1: {match_name_1}":<79}|\n"
                    f"{'vs':<79}|\n"
                    f"{f"Team 2: {match_name_2}":<79}|\n"
                    f"{f"Match Winner: {str(match_winner_name)}":<79}|"
                )


            else:
                match1: Team = LogicLayerAPI.get_team_by_uuid(match.team_1)
                match2: Team = LogicLayerAPI.get_team_by_uuid(match.team_2)

                match_name_1: str = match1.name
                match_name_2: str = match2.name

                output_list.append(
                    f"{line('—')}\n"
                    f"{f"Date: {match.match_date}":<79}|\n"
                    f"{f"Match Time: {str(match.match_time)}":<79}|\n"
                    f"{f"Team 1: {match_name_1}":<79}|\n"
                    f"{'vs':<79}|\n"
                    f"{f"Team 2: {match_name_2}":<79}|\n"
                    f"{f"Match Winner: {str(match_winner_name)}":<79}|"
                )

        return output_list


    # "Created" by Sindri Freysson
    def string_to_table(
        self, string_list: list[str]) -> list[str]:
        """
        A helper function that formats a given list of string into a 2 column table
        :param object_list: Takes a list of model objects
        :return: A formatted list of strings that when displayed appears as a table
        """
        output_list: list[str] = []
        length: int = len(string_list)

        for value in range(0, len(string_list), 2):
            left = string_list[value]
            if value + 1 < length:

                right = string_list[value + 1]
                output_list.append(f"{left:<39}|{right:<39}|")

            else:  # odd number, last item has no pair
                output_list.append(f"{left:<39}|{" ":<39}|")

        return output_list

    def object_to_string(
        self, object_list: list[Player] | list[Team] | list[Club] | list[Tournament]
    ) -> list[str]:
        """
        Function that converts a list of object to a list of names
        :param object_list: Takes a list of model objects
        :return: Names of model objects as a list of strings
        """
        str_list: list[str] = [x.name for x in object_list]
        return str_list
