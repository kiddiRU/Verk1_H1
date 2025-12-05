"""
Author: Elmar Sigmarsson <elmars25@ru.is>
Date: 2025-12-03

A validation file that takes inn all info that would need to be validated
"""

from Models import Team, ValidationError
from DataLayer import DataLayerAPI
from datetime import date

def validate(attribute: str, value: str, name_type: str = ''):
    if attribute == 'name': return validate_name(value)
    elif attribute == 'date_of_birth': return validate_date(value)
    elif attribute == 'home_address': return validate_home_address(value)
    elif attribute == 'email': return validate_email(value)
    elif attribute == 'phone_number': return validate_phone_number(value)
    elif attribute == 'handle': return validate_unique_name(value, name_type)
    else: return
    
def validate_unique_name(unique_name: str, type_of_name: str) -> str | ValidationError:
    """
    Checks if the name is unique and is between 3-40 char in length
    Used for unique player handle, team tournament and club names
    """

    if len(unique_name) < 3 or len(unique_name) > 40:
        raise ValidationError("Name needs to be between 3 to 40 characters in length")
        
    if type_of_name == "PLAYER":
        model_player: list = DataLayerAPI.load_players()

        for player in model_player:
            if player.handle == unique_name:
                raise ValidationError("Handle is already taken")
        
        return unique_name

    #TODO implement check for unique names in team, tournament and club
    elif type_of_name == "TEAM":
        team_names: list[str] = [team.name for team in DataLayerAPI.load_teams()]

        if unique_name in team_names:
            raise ValidationError('Team name is aldready taken!')
    
        return unique_name

    elif type_of_name == "TOURNAMENT":
        pass

    elif type_of_name == "CLUB":
        pass


def validate_name(name) -> str | ValidationError: # Players full name
    """Checks if the name is in between 3-40 char in length and has only letters"""
    
    if len(name) < 3 or len(name) > 40:
        raise ValidationError("Name needs to be between 3 to 40 characters in length")
    
    else:
        return name
    

def validate_home_address(home_address) -> str | ValidationError: # Players home address
    """Checks if home address has street name, street number and area (Frostafold 3 Reykjavík)"""
    
    try:
        address_list: str = home_address.split()
        street_name: str = address_list[0]
        street_number: str = address_list[1]
        area_name: str = address_list[2]
        
        is_string_street_name: bool = street_name.isalpha()
        is_digit_street_number: bool = street_number.isdigit()
        is_string_area_name: bool = area_name.isalpha()

        if is_string_street_name and is_digit_street_number and is_string_area_name:
            return home_address

        else:
            raise ValidationError

    except:
        raise ValidationError


def validate_phone_number(phone_number) -> str | ValidationError: # Players and tournament contact phone number
    """Checks if phone number is eight in length 7 nums and a dash (123-4567)"""
    
    if "-" in phone_number:
        phone_number_list: list = phone_number.split("-")
        first_half_phone_nr: str = phone_number_list[0]
        second_half_phone_nr: str = phone_number_list[1]

        is_digit_first_half: bool = first_half_phone_nr.isdigit()
        is_digit_second_half: bool = second_half_phone_nr.isdigit()
        length_first_half: bool = len(first_half_phone_nr) == 3
        length_second_half: bool = len(second_half_phone_nr) == 4

        if is_digit_first_half and is_digit_second_half and length_first_half and length_second_half:
            return phone_number

        else:
            raise ValidationError("Phone number inputted incorrectly")
    
    else:
        raise ValidationError("Phone number inputted incorrectly")


def validate_email(email) -> str | ValidationError: # Players and tournament contact email
    """Checks if email has @, and that there is something before and after the @"""

    if "@" in email:
        email_list: list = email.split("@")
        before_at_symbol: str = email_list[0]
        after_at_symbol: str = email_list[1]

        if before_at_symbol == "" or after_at_symbol == "":
            raise ValidationError('Invalid email!')

        else:
            return email


    else:
        raise ValidationError('Invalid email!')


def validate_date(date_input) -> str | ValidationError: # Date of Birth, Date of Tournament
    """Checks if date format is correct YYYY-MM-DD"""

    try:
        date_list = date_input.split("-")
        year: int = int(date_list[0])
        month: int =  int(date_list[1])
        day: int = int(date_list[2])

    except:
        raise ValidationError("Date inputted incorrectly")

    try:
        validate_date = date(year, month, day)
        return str(validate_date)
    
    except:
        raise ValidationError("Date inputted incorrectly")


#TODO add functionality to all function bellow
def validate_date_frame(date_1, date_2) -> bool: # Date frame of tournament
    """Checks if date frame is correct, date_1 is before date_2 (2025-12-01 -> 2025-12-06)"""
    pass

def validate_time() -> bool: # Time of Match and Tournament time frame
    """Checks if time is format is correct HH:MM (12:00)"""
    pass

def validate_time_frame(time_1, time_2) -> bool: # Time frame of tournament
    """Checks if time frame is correct, time_1 is before time_2 (08:00 -> 16:00) """
    pass


def club_color() -> bool: # Club
    """Checks if color is on of the colors implemented (RED, BLUE, YELLOW, GREEN)"""
    pass


