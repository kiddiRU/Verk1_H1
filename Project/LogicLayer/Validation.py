"""
Author: Elmar Sigmarsson <elmars25@ru.is>
Date: 2025-12-03

Minor changes: Andri Már Kristjánsson <andrik25@ru.is>
(just type hinting changes)

A validation file that takes inn all info that would need to be validated
"""

from datetime import date, time
from Models import ValidationError
from DataLayer import DataLayerAPI


def validate_attr(
        attribute: str,
        value: str,
        name_type: str = ''
        ) -> str | date:
    """Validates all attributes that need validating.
    :param attribute:
        The type of attribute which needs validating, available options are

        -   name
        -   date_of_birth
        -   home_address
        -   email
        -   phone_number
        -   handle
        -   tournament_date
        -   tournament_time
        -   color
        -   number

    :param value:
        The value that needs validating.

    :param name_type:
        Only used for attribute handle, this determines the type of handle
        want validated, available options are.

        -   PLAYER
        -   TEAM
        -   TOURNAMENT
        -   CLUB

    :returns:
        Returns the same value back if it's valid, otherwise it raises a
        ValidationError. The only exception is when you call with date
        attribute, in that case it will return date object if it's valid.
    """

    # Checks to see if all characters in value are standard printable ascii
    # characters or in alphabet to allow icelandic letters.
    for char in value:
        if (ord(char) < 32 or ord(char) > 126) and not char.isalpha():
            raise ValidationError(
                "String contains characters not in ascii range"
            )

    if attribute == 'name':
        return validate_name(value)
    elif attribute == 'date_of_birth':
        return validate_date(value)
    elif attribute == 'home_address':
        return validate_home_address(value)
    elif attribute == 'email':
        return validate_email(value)
    elif attribute == 'phone_number':
        return validate_phone_number(value)
    elif attribute == 'handle':
        return validate_unique_name(value, name_type)
    elif attribute == 'tournament_date':
        return validate_tournament_date(value)
    elif attribute == 'tournament_time':
        return validate_tournament_time(value)
    elif attribute == 'color':
        return validate_color(value)
    elif attribute == 'number':
        return validate_number(value)
    else:
        raise ValidationError("attribute not found in list")


def validate_unique_name(unique_name: str, type_of_name: str) -> str:
    """Validates input to a valid unique name

    - Checks if the name is in between the allowed character limit 3-39
    - Checks what type of name to search through

    Then loads the needed name type and checks if
    the unique name is already in the data
    and if so an error is raised

    Only player has an extra check that is that the handle can not be admin

    :param unique_name:
        The name to check if it is unique
    :type unique_name: str

    :param type_of_name:
        Type of name so that it looks through the right data for uniqueness

        - Handle
        - Team
        - Club
        - Tournament
    :type type_of_name: str

    :return:
        Returns the name if it is valid, if not an error is raised
    :rtype: str
    """
    unique_name = unique_name.strip()

    # Checks the length of all types of names
    if len(unique_name) < 3 or len(unique_name) > 39:
        raise ValidationError(
            "Name needs to be between 3 to 39 characters long"
        )

    # For player handles
    if type_of_name == "PLAYER":
        player_names: list[str] = [
            player.handle for player in DataLayerAPI.load_players()
        ]

        if unique_name in player_names or unique_name == "admin":
            raise ValidationError(
                f'The handle \'{unique_name}\' is already taken!'
            )

        return unique_name

    # For Team names
    elif type_of_name == "TEAM":
        team_names: list[str] = [
            team.name for team in DataLayerAPI.load_teams()
        ]

        if unique_name in team_names:
            raise ValidationError(
                f'The name \'{unique_name}\' is already taken!'
            )

        return unique_name

    # For Tournament names
    elif type_of_name == "TOURNAMENT":
        tournament_names: list[str] = [
            t.name for t in DataLayerAPI.load_tournaments()
        ]

        if unique_name in tournament_names:
            raise ValidationError(
                f'The name \'{unique_name}\' is already taken!'
            )

        return unique_name

    # For Club names
    elif type_of_name == "CLUB":
        club_names: list[str] = [c.name for c in DataLayerAPI.load_clubs()]

        if unique_name in club_names:
            raise ValidationError(
                f'The name \'{unique_name}\' is already taken!'
            )

        return unique_name


def validate_name(name: str) -> str:
    """Validates input to a valid name

    - Checks if the name is in between 3-39 long and has only letters

    :param name:
        Real name of player that is being validated
    :type name: str

    :return:
        Returns the name if it is valid, otherwise an error is raised
    :rtype: str
    """
    name = name.strip()

    # Checks the length of the name
    if (len(name) < 3 or len(name) > 39):
        raise ValidationError(
            "Name needs to be between 3 to 39 characters in length and"
        )

    # Checks that their are no numbers
    if not name.replace(" ", "").isalpha():
        raise ValidationError("Name can only have letters")

    return name


def validate_home_address(home_address: str) -> str:
    """Validates input to a valid home address

    - Checks if the address is spilt into 3 parts
    - Checks if the first and third parts are letters
    - Checks if the second part is digits and
    if all are true the address is valid

    (Street_name Street_number, City_name)

    :param home_address:
        The address to be validated
    :type home_address: str

    :return:
        Returns the address if it is valid, otherwise an error is raised
    :rtype: str
    """
    home_address = home_address.strip()

    # Splits the address into parts and check that there are only three parts
    address_list: list[str] = home_address.split()
    if len(address_list) < 3 or len(address_list) > 3:
        raise ValidationError(f"Invalid address: {home_address}")

    street_name: str = address_list[0]
    street_number: str = address_list[1]
    city_name: str = address_list[2]

    # Checks that the right parts are the right type
    is_string_street_name: bool = street_name.isalpha()
    is_digit_street_number: bool = street_number.isdigit()
    is_string_area_name: bool = city_name.isalpha()

    # Checks that all parts are true
    if (
        is_string_street_name
        and is_digit_street_number
        and is_string_area_name
    ):

        return home_address

    # If one part is False an error is raised
    else:
        raise ValidationError(f"Invalid address: {home_address}")


def validate_phone_number(phone_number: str) -> str:
    """Validates input to a valid phone number

    - Checks if there is a dash in the string
    - Splits the string by the dash
    - Checks that both parts are all numbers and that
      the first is 3 characters long and the second 4 long
    - If all parts are true the number is valid, otherwise an error is raised

    :param phone_number:
        The phone number to validate
    :type phone_number: str

    :return:
    Returns the phone number if it is valid,
    otherwise an error is raised
    :rtype: str
    """
    phone_number = phone_number.strip()

    # Checks if a dash is in the string and splits it by the dash
    if "-" in phone_number:
        phone_number_list: list[str] = phone_number.split("-")
        first_half_phone_nr: str = phone_number_list[0]
        second_half_phone_nr: str = phone_number_list[1]

        # Checks the length and that everything are numbers in the parts
        is_digit_first_half: bool = first_half_phone_nr.isdigit()
        is_digit_second_half: bool = second_half_phone_nr.isdigit()
        length_first_half: bool = len(first_half_phone_nr) == 3
        length_second_half: bool = len(second_half_phone_nr) == 4

        # Checks that everything is True
        if (
            is_digit_first_half
            and is_digit_second_half
            and length_first_half
            and length_second_half
        ):

            return phone_number

        # If any part comes as false
        else:
            raise ValidationError("Phone number inputted incorrectly")

    # If there is no dash in the string
    else:
        raise ValidationError("Phone number inputted incorrectly")


def validate_email(email: str) -> str:
    """Validates input to a valid email

    - Checks if the length is not over 39
    - Checks that there is an @ and only one
    - Checks splits the email by the @ and checks that there are two parts
    - Checks that there is something before and after the @

    :param email:
        The email to validate
    :type email: str

    :return:
        Returns the email if it's valid,
        otherwise an error is raised
    :rtype: str
    """
    email = email.strip()

    # Checks the length of the email
    if len(email) > 39:
        raise ValidationError("Email can't be longer then 39 characters long")

    # Checks that there is an @ and only one
    # Splits the string by the @
    if ("@" in email) and (email.count("@") == 1):
        email_list: list[str] = email.split("@")
        before_at_symbol: str = email_list[0]
        after_at_symbol: str = email_list[1]

        # Checks that its not empty before and after the @
        if before_at_symbol == "" or after_at_symbol == "":
            raise ValidationError('Invalid email!')

        else:
            return email

    # if the email dose not have an @ or more than one
    else:
        raise ValidationError('Invalid email!')


def validate_date(date_input: str) -> date:
    """Validates input to a valid date

    Checks if input can be parsed to a valid pair of Year Month and Day
    - Checks if the string can be spit by the dashes (-)
    - Checks that the date valid
    - "YYYY-MM-DD"

    :param date_input:
        The date to validate
    :type date_input: str

    :return:
        Returns the date object if its valid,
        otherwise an error is raised
    :rtype: date
    """
    date_input = date_input.strip()

    # Checks if the date can be split by the dashes (-) and are numbers
    try:
        date_list: list[int] = list(map(int, date_input.split("-")))

        # Check if the date is valid
        try:
            valid_date = date(date_list[0], date_list[1], date_list[2])
            return valid_date

        except (ValueError, IndexError):
            raise ValidationError("Invalid date")

    except ValueError:
        raise ValidationError("Invalid date")


def validate_time(time_input: str) -> time:
    """Validates input to a valid time

    Checks if input can be parsed to a valid pair of Hours and Minuets
    - Checks if the string can be split by the colon (:)
    - Checks if the time is valid
    - "HH:MM"

    :param time_input:
        The time to validate
    :type time_input: str

    :return:
        Returns the time if its valid,
        otherwise an error is raised
    :rtype: time
    """
    """Checks if time is format is correct HH:MM (12:00)"""
    time_input = time_input.strip()

    # Checks if the string can be split by the colon (:)
    try:
        time_list = list(map(int, time_input.split(":")))

        # Checks if the time is valid
        try:
            valid_time = time(time_list[0], time_list[1])
            return valid_time

        except ValueError:
            raise ValidationError("Invalid time")

    except ValueError:
        raise ValidationError("Invalid time")


def validate_tournament_date(value: str) -> str:
    """Validates input to be a pair of start and end dates in a tournament.

    Checks if input can be parsed to a valid pair of start and end date for
    a tournament. A valid format is "YYYY-MM-DD YYYY-MM-DD".

    :param value:
        The value to check if it can be changed to start and end date

    :returns:
        Returns the same string back if it's valid, otherwise it raises
        a ValidationError.
    """

    # Strips the input of its whitespace.
    value: str = value.strip()

    # Checks whether it can be split into two values.
    try:
        begin: str
        end: str
        begin, end = value.split()
    except ValueError:
        raise ValidationError("Could not split dates")

    # Validates both dates individually.
    begin_date: date = validate_date(begin)
    end_date: date = validate_date(end)

    # Checks whether the end date comes before the beginning date.
    if begin_date <= end_date:
        return value
    else:
        raise ValidationError("Beginning date happens after end date")


def validate_tournament_time(value: str) -> str:
    """Validates input to be a pair of start and end times in a tournament.

    Checks if input can be parsed to a valid pair of start and end times for
    a tournament. A valid format is "HH:MM HH:MM".

    :param value:
        The value to check if it can be changed to start and end time

    :returns:
        Returns the same string back if it's valid, otherwise it raises
        a ValidationError.
    """

    # Strips the input of its whitespace.
    value = value.strip()

    # Checks whether it can be split into two values.
    try:
        begin: str
        end: str
        begin, end = value.split()
    except ValueError:
        raise ValidationError("Could not split time input")

    # Validates both times individually.
    begin_time: time = validate_time(begin)
    end_time: time = validate_time(end)

    # Make sure the minute values are the same
    if begin_time.minute != end_time.minute:
        raise ValidationError("Begin and end minutes do not match")

    # Checks to make sure begin and end time aren't the same.
    if begin_time == end_time:
        raise ValidationError("Begin time happens after end time")

    return value


def validate_color(value: str) -> str:
    """Validates input to be a valid color option.

    Valid color options are

    -   red
    -   green
    -   yellow
    -   blue
    -   pink
    -   cyan

    :param value:
        The value being checked

    :returns:
        Returns the value as is if it's valid, otherwise it raises an error.
    """

    # Strips the value of its whitespaces.
    value = value.strip().lower()
    available_colors = ["red", "green", "yellow", "blue", "pink", "cyan"]

    # Checks to see if the given value is in the list of available colors.
    if value in available_colors:
        return value

    raise ValidationError("Color not one of the available ones.")


def validate_number(number: str) -> str:
    """Validates input to a valid number for amount of servers

    Checks that the number is in between 1 and 8

    :param number:
        The amount of servers that is valid
    :type number: str

    :return:
        Returns a string number if ist valid,
        otherwise an error is raised
    :rtype: str
    """
    # Checks if the string is a number and that its in between 1-8
    try:
        if int(number) < 1 or int(number) > 8:
            raise ValidationError("Amount of servers can be between 1 - 8")
    except ValueError:
        raise ValidationError("Amount of servers can be between 1 - 8")

    return number
