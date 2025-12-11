"""
Author: Ísak Elí Hauksson <isak25@ru.is>
Date: 2025-12-03

Co-Author: Andri Már Kristjánsson <andrik25@ru.is>,
Sindri Freysson <Sindrif25@ru.is>

File that holds the UtilityUI class
which holds functions used in multiple places
"""

from datetime import date

from LogicLayer import LogicLayerAPI
from LogicLayer.LogicLayerAPI import validate

from Models import ValidationError
from Models.Club import Club
from Models.Match import Match
from Models.Player import Player
from Models.Team import Team
from Models.Tournament import Tournament


class UtilityUI:
    """Utility Class for multi use function for ui layer"""

    def __init__(self) -> None:
        self.error_color: str = "\033[31m"
        self.message_color: str = "\033[36m"
        self.reset: str = "\033[0m"

    def prompt_choice(self, valid_choices: list[str]) -> str:
        """
        Helper function that checks for allowed choices

        :param valid_choices: A list of strings that are allowed to input
        :type valid_choices: list[str]
        :return: The choice if it is allowed
        :rtype: str
        """

        # Make valid choices into lowercase
        valid_choices_lower: list[str] = [x.lower() for x in valid_choices]

        # Loop through until input is valid
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
        Helper function that repeats input until it is valid
        or navigation word is entered

        :param message: message to display - "Enter Your name"
        :param attribute: attribute of a model class - "name"
        :param info_type: information type - "PLAYER"
        :return: Repeats until the input is valid or navigation word is entered
        :rtype: str
        """
        while True:
            try:
                print(self.message_color + message + self.reset)
                # Get input and quit if it is "q"
                choice: str = input()
                if choice.lower() == "q":
                    return ""

                # Validate the input before returning
                valid: str | None | date = validate(
                    attribute, choice, info_type
                )
                return str(valid)

            except ValidationError as e:
                # Display error message and retry
                print(self.error_color + str(e) + self.reset)
                continue

    def input_change(
        self, message: str, attribute: str, info_type: str
    ) -> str:
        """
        Helper function that repeats input until it is valid or navigation word is entered

        :param message: Message to display - "Enter Your name"
        :param attribute: Attribute of a model class - "name"
        :param info_type: Information type - "PLAYER"
        :return: Returns the validated input or empty string if 'q' is entered
        :rtype: str
        """
        while True:
            try:
                # Display the input message
                print(self.message_color + message + self.reset)
                # Get input from user
                choice: str = input()

                # Return if user enters 'q' to navigate back
                if choice.lower() == "q":
                    return choice

                # Return if no input is provided
                if not choice:
                    return choice

                # Validate the input before returning
                valid: str | None | date = validate(
                    attribute, choice, info_type
                )
                return str(valid)

            except ValidationError as e:
                # Display error message and retry
                print(self.error_color + str(e) + self.reset)
                continue

    def except_status_tournaments(
        self, tournament_status: Tournament.StatusType
    ) -> list[str]:
        """
        Returns the names of all tournaments that do not have the given status.

        :param tournament_status: The status to exclude. Possible values are
            "ACTIVE", "INACTIVE", and "ARCHIVED".
        :type tournament_status: Tournament.StatusType
        :return: All tournament names whose status does not match
        the input.
        :rtype: list[str]

        """
        # Gets all tournaments and filter out those with the excluded status
        tournaments: list[Tournament] = LogicLayerAPI.list_tournaments()
        return [x.name for x in tournaments if x.status != tournament_status]

    def team_names(self) -> list[str]:
        """
        Get a list of all team names

        :return: A list of team names
        :rtype: list[str]
        """

        # Create a list of team names from Club objects
        team_list: list[Team] = LogicLayerAPI.list_all_teams()
        return [x.name for x in team_list]

    def club_names(self) -> list[str]:
        """
        Get a list of all club names

        :return: A list of club names
        :rtype: list[str]
        """
        # Create a list of club names from Club objects
        clubs: list[Club] = LogicLayerAPI.list_all_clubs()
        return [x.name for x in clubs]

    def player_handles(self) -> list[str]:
        """
        Get a list of all player handles

        :return: A list of player handles
        :rtype: list[str]
        """
        # Create a list of player handles from Player objects
        player_list: list[Player] = LogicLayerAPI.list_all_players()
        return [p.handle for p in player_list]

    def show_main(self, flag: str) -> list[str]:
        """
        Returns a formatted list of player handles, club names, or team names.

        Produces a two-column table layout where each line contains one or
        two names aligned with fixed-width formatting.

        :param flag: Determines which model class to list. Possible values are
            "payers", "clubs", and "teams".
        :type flag: str
        :return: A formatted f-string for printing
        :rtype: list[str]
        """

        # Get which model class to show
        flag_dict = {
            "players": self.player_handles(),
            "clubs": self.club_names(),
            "teams": self.team_names(),
        }

        # For developers in case of spelling mistake
        if flag not in flag_dict:
            return ["Flag is not correct"]

        unique_names: list[str] = flag_dict[flag]  # get all names or handles
        output_list: list[str] = []  # list that holds each line as a f-string

        length: int = len(unique_names)

        # Loop through and append each line of the
        for value in range(0, len(unique_names), 2):
            # Get left side item
            left: str = unique_names[value]

            if value + 1 < length:
                # get right side item
                right: str = unique_names[value + 1]

                output_list.append(f"{left:<39}|{right:<39}|")

            else:  # odd number, last item has no pair
                output_list.append(f"{left:<39}|{' ':<39}|")

        return output_list

    def show_tournaments_except_status(
        self, tournament_status: Tournament.StatusType
    ) -> list[str]:
        """
        Returns formatted rows of tournaments that do not have the given status.

        :param tournament_status: The status to exclude. Possible values are
            "ACTIVE", "INACTIVE", and "ARCHIVED".
        :type tournament_status: Tournament.StatusType
        :return: A list of formatted strings for tournaments without the
            specified status.
        :rtype: list[str]
        """

        # Fetch all tournaments from the logic layer
        tournaments: list[Tournament] = LogicLayerAPI.list_tournaments()

        # Holds each formatted table row
        output_list: list[str] = []

        # Build a formatted row for each tournament whose status does not match
        for tournament in tournaments:
            if tournament.status == tournament_status:
                continue

            output_list.append(
                f"{tournament.name:<68}>{tournament.status:^10}|"
            )

        return output_list

    def list_matches(self, tournament_uuid: str, show_all: bool) -> list[str]:
        """
        Returns formatted match information for a tournament, showing either all
        matches or only the upcoming ones.

        :param tournament_uuid: The UUID of the tournament.
        :type tournament_uuid: str
        :param show_all: Whether to return all matches or only the next matches.
        :type show_all: bool
        :return: A list of formatted strings containing match information.
        :rtype: list[str]
        """

        # Chooses the appropriate match list
        if show_all:
            match_list: list[Match] = LogicLayerAPI.get_all_matches(
                tournament_uuid
            )
        else:
            match_list: list[Match] = LogicLayerAPI.get_next_matches(
                tournament_uuid
            )

        output_list: list[str] = []  # Holds each formatted match block
        revealed: str = "To be revealed"

        for match in match_list:
            # Determine the match winner name (None / UUID / Team)
            match_winner_uuid: str = str(match.winner)
            if match_winner_uuid != "None":
                match_winner_team: Team = LogicLayerAPI.get_team_by_uuid(
                    match_winner_uuid
                )
                match_winner_name: str = match_winner_team.name
            else:
                match_winner_name: str = match_winner_uuid

            # Skip unrevealed matches
            if (match.team_1 or match.team_2) == revealed:
                continue

            # Resolve team objects and names
            match1: Team = LogicLayerAPI.get_team_by_uuid(match.team_1)
            match2: Team = LogicLayerAPI.get_team_by_uuid(match.team_2)

            match_name_1: str = match1.name
            match_name_2: str = match2.name

            # Add formatted match block
            output_list.append(
                f"{80 * '—'}\n"
                f"{f'Date: {match.match_date}':<79}|\n"
                f"{f'Match Time: {str(match.match_time)}':<79}|\n"
                f"{f'Team 1: {match_name_1}':<79}|\n"
                f"{'vs':<79}|\n"
                f"{f'Team 2: {match_name_2}':<79}|\n"
                f"{f'Match Winner: {str(match_winner_name)}':<79}|"
            )

        return output_list

    # "Created" by Sindri Freysson
    def string_to_table(self, string_list: list[str]) -> list[str]:
        """
        A helper function that formats a given list of string into a 2 column table

        :param string_list: Takes a list of model objects
        :type string_list: list[str]
        :return: A formatted list of strings that when displayed appears as a table
        :rtype: list[str]
        """
        output_list: list[str] = []  # list that holds each line as a f-string

        length: int = len(string_list)

        # Loop through and append each line of the
        for value in range(0, len(string_list), 2):
            # Get left side item
            left: str = string_list[value]

            if value + 1 < length:
                # get right side item
                right: str = string_list[value + 1]

                output_list.append(f"{left:<39}|{right:<39}|")

            else:  # odd number, last item has no pair
                output_list.append(f"{left:<39}|{' ':<39}|")

        return output_list

    def object_to_string(
        self,
        object_list: list[Player] | list[Team] | list[Club] | list[Tournament],
    ) -> list[str]:
        """
        Converts a list of model objects into a list of their corresponding names.

        :param object_list: A list containing Player, Team, Club, or Tournament objects.
        :type object_list: list[Player] | list[Team] | list[Club] | list[Tournament]
        :return: A list of names or handles extracted from the model objects.
        :rtype: list[str]
        """

        str_list: list[str] = []

        # Extract the correct string attribute depending on the model type
        for obj in object_list:
            if isinstance(obj, Player):
                str_list.append(obj.handle)
            elif hasattr(obj, "name"):  # Teams, Clubs, Tournaments
                str_list.append(obj.name)

        return str_list
