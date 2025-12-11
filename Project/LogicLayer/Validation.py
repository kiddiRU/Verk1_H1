"""
Author: Elmar Sigmarsson <elmars25@ru.is>
Date: 2025-12-03

Minor changes: Andri Már Kristjánsson <andrik25@ru.is>
(just type hinting changes)

A validation file that takes inn all info that would need to be validated
"""

from typing import Callable
from datetime import date, time
from Models import ValidationError
from DataLayer import DataLayerAPI

# def validate_attr(attribute: str, value: str, name_type: str = '') -> str | None | date:

#     for char in value:
#         if (ord(char) < 32 or ord(char) > 126) and not char.isalpha:
#             raise ValidationError("String contains characters not in ascii range")

#     if attribute == 'name': return validate_name(value)
#     elif attribute == 'date_of_birth': return validate_date(value)
#     elif attribute == 'home_address': return validate_home_address(value)
#     elif attribute == 'email': return validate_email(value)
#     elif attribute == 'phone_number': return validate_phone_number(value)
#     elif attribute == 'handle': return validate_unique_name(value, name_type)
#     elif attribute == 'tournament_date': return validate_tournament_date(value)
#     elif attribute == 'tournament_time': return validate_tournament_time(value)
#     elif attribute == 'color': return validate_color(value)
#     elif attribute == 'number': return validate_number(value)
#     else: return

Validator = Callable[[str], str | None]

def validate_attr(attribute: str, value: str, name_type: str = '') -> str | None:
    ''' Docstring '''

    for char in value:
        if (ord(char) < 32 or ord(char) > 126) and not char.isalpha():
            raise ValidationError("String contains characters not in ascii range")

    validators: dict[str, Validator] = {
        'name': validate_name,
        'date_of_birth': validate_date,
        'home_address': validate_home_address,
        'email': validate_email,
        'phone_number': validate_phone_number,
        'handle': lambda v: validate_unique_name(v, name_type),
        'tournament_date': validate_tournament_date,
        'tournament_time': validate_tournament_time,
        'color': validate_color,
        'number': validate_number,
    }

    validator = validators.get(attribute)
    if validator is None:
        return None

    return validator(value)


# Player handle, team name, tour name and club name
def validate_unique_name(unique_name: str, type_of_name: str) -> str | None:
    """
    Checks if the name is unique and is between 3-39 char in length
    Used for unique player handle, team tournament and club names
    """
    unique_name = unique_name.strip()

    if len(unique_name) < 3 or len(unique_name) > 39:
        raise ValidationError("Name needs to be between 3 to 39 characters in length")

    if type_of_name == "PLAYER":
        player_names: list[str] = [player.handle for player in DataLayerAPI.load_players()]

        if unique_name in player_names or unique_name == "admin":
            raise ValidationError(f'The handle \'{unique_name}\' is already taken!')

        return unique_name

    elif type_of_name == "TEAM":
        team_names: list[str] = [team.name for team in DataLayerAPI.load_teams()]

        if unique_name in team_names:
            raise ValidationError(f'The name \'{unique_name}\' is already taken!')

        return unique_name

    elif type_of_name == "TOURNAMENT":
        tournament_names: list[str] = [t.name for t in DataLayerAPI.load_tournaments()]

        if unique_name in tournament_names:
            raise ValidationError(f'The name \'{unique_name}\' is already taken!')

        return unique_name

    elif type_of_name == "CLUB":
        club_names: list[str] = [c.name for c in DataLayerAPI.load_clubs()]

        if unique_name in club_names:
            raise ValidationError(f'The name \'{unique_name}\' is already taken!')

        return unique_name

# Players full name
def validate_name(name: str) -> str | None:
    """
    Checks if the name is in between 3-39 char in length and has only letters
    """
    name = name.strip()

    if (len(name) < 3 or len(name) > 39):
        raise ValidationError(
            "Name needs to be between 3 to 39 characters in length and"
            )

    if not name.replace(" ","").isalpha():
        raise ValidationError("Name can only have letters")

    return name


# Players home address
def validate_home_address(home_address: str) -> str | None:
    """
    Checks if home address has street name, street number and area
    (Frostafold 3 Reykjavík)
    """
    home_address = home_address.strip()

    try:
        address_list: list[str] = home_address.split()
        street_name: str = address_list[0]
        street_number: str = address_list[1]
        area_name: str = address_list[2]

        is_string_street_name: bool = street_name.isalpha()
        is_digit_street_number: bool = street_number.isdigit()
        is_string_area_name: bool = area_name.isalpha()

        if (is_string_street_name
            and is_digit_street_number
            and is_string_area_name):

            return home_address

        else:
            raise ValidationError("Invalid address:", home_address)

    except:
        raise ValidationError("Invalid address:", home_address)


# Players and tournament contact phone number
def validate_phone_number(phone_number: str) -> str | None:
    """Checks if phone number is eight in length 7 nums and a dash (123-4567)"""
    phone_number = phone_number.strip()

    if "-" in phone_number:
        phone_number_list: list[str] = phone_number.split("-")
        first_half_phone_nr: str = phone_number_list[0]
        second_half_phone_nr: str = phone_number_list[1]

        is_digit_first_half: bool = first_half_phone_nr.isdigit()
        is_digit_second_half: bool = second_half_phone_nr.isdigit()
        length_first_half: bool = len(first_half_phone_nr) == 3
        length_second_half: bool = len(second_half_phone_nr) == 4

        if (is_digit_first_half
            and is_digit_second_half
            and length_first_half
            and length_second_half):

            return phone_number

        else:
            raise ValidationError("Phone number inputted incorrectly")

    else:
        raise ValidationError("Phone number inputted incorrectly")


#Players and tournament contact email
def validate_email(email: str) -> str | None:
    """
    Checks if email has @, and that there is something before and after the @
    can only have one @
    """
    email = email.strip()

    if ("@" in email) and (email.count("@") == 1) :
        email_list: list[str] = email.split("@")
        before_at_symbol: str = email_list[0]
        after_at_symbol: str = email_list[1]

        if before_at_symbol == "" or after_at_symbol == "":
            raise ValidationError('Invalid email!')

        else:
            return email


    else:
        raise ValidationError('Invalid email!')


# For date of birth and date of a match
def validate_date(date_input: str) -> date:
    """
    Splits the string and tries to change the numbers in to int and 
    Checks if date format is correct YYYY-MM-DD
    """
    date_input = date_input.strip()

    try:
        date_list: list[int] = list(map(int, date_input.split("-")))

        try:
            valid_date = date(date_list[0], date_list[1], date_list[2])
            return valid_date

        except:
            raise ValidationError("Invalid date")

    except:
        raise ValidationError("Invalid date")



# Time of Match and Tournament time frame
def validate_time(time_input: str) -> time:
    """Checks if time is format is correct HH:MM (12:00)"""
    time_input = time_input.strip()

    try:
        time_list = list(map(int, time_input.split(":")))

        try:
            valid_time = time(time_list[0], time_list[1])
            return valid_time

        except:
            raise ValidationError("Not a valid time")

    except:
        raise ValidationError("Letters are not allowed in time")


def validate_tournament_date(value: str) -> str:
    value = value.strip()

    try:
        begin, end = value.split()
    except:
        raise ValidationError("Could not split dates")

    begin_date = validate_date(begin)
    end_date = validate_date(end)

    if begin_date <= end_date:
        return value
    else:
        raise ValidationError("Beginning date happens after end date")

def validate_tournament_time(value: str) -> str:
    value = value.strip()

    try:
        begin, end = value.split()
    except:
        raise ValidationError("Could not split time input")

    begin_time = validate_time(begin)
    end_time = validate_time(end)

    if begin_time.minute != end_time.minute:
        raise ValidationError("Begin and end minutes do not match")


    if begin_time == end_time:
        raise ValidationError("Begin time happens after end time")

    return value

def validate_color(value: str) -> str:
    value = value.strip().lower()
    available_colors = ["red", "green", "yellow", "blue", "pink", "cyan"]

    if value in available_colors:
        return value

    raise ValidationError("Color not one of the available ones.")


def validate_number(number: str) -> str:

    try:
        if int(number) < 1 or int(number) > 8 :
            raise ValidationError("Amount of servers can be between 1 - 8")
    except:
        raise ValidationError("Amount of servers can be between 1 - 8")

    return number
