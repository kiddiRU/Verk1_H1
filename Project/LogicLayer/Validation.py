"""
Author: Elmar Sigmarsson <elmars25@ru.is>
Date: 2025-12-03

Minor changes: Andri Már Kristjánsson <andrik25@ru.is>
(just type hinting changes)

A validation file that takes inn all info that would need to be validated
"""

from Models import Team, ValidationError
from DataLayer import DataLayerAPI
from datetime import date, time

def validate_attr(attribute: str, value: str, name_type: str = '') -> str | None:
    if attribute == 'name': return validate_name(value)
    elif attribute == 'date_of_birth': return validate_date(value)
    elif attribute == 'home_address': return validate_home_address(value)
    elif attribute == 'email': return validate_email(value)
    elif attribute == 'phone_number': return validate_phone_number(value)
    elif attribute == 'handle': return validate_unique_name(value, name_type)
    else: return
    

# Player handle, team name, tour name and club name
def validate_unique_name(unique_name: str, type_of_name: str) -> str | None:
    """
    Checks if the name is unique and is between 3-40 char in length
    Used for unique player handle, team tournament and club names
    """

    if len(unique_name) < 3 or len(unique_name) > 40:
        raise ValidationError("Name needs to be between 3 to 40 characters in length")
        
    if type_of_name == "PLAYER":
        player_names: list[str] = [player.handle for player in DataLayerAPI.load_players()]
        if unique_name in player_names:
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
    Checks if the name is in between 3-40 char in length and has only letters
    """
    
    if (len(name) < 3 or len(name) > 40):
        raise ValidationError(
            "Name needs to be between 3 to 40 characters in length and"
            )
    
    if not name.replace(" ","").isalpha():
        raise ValidationError("Name can not have digits")
    
    else:
        return name
    

# Players home address
def validate_home_address(home_address: str) -> str | None:
    """
    Checks if home address has street name, street number and area
    (Frostafold 3 Reykjavík)
    """
    
    try:
        address_list: str = home_address.split()
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
            raise ValidationError("Invalid address")

    except:
        raise ValidationError("Invalid address")


# Players and tournament contact phone number
def validate_phone_number(phone_number: str) -> str | None: 
    """Checks if phone number is eight in length 7 nums and a dash (123-4567)"""
    
    if "-" in phone_number:
        phone_number_list: list = phone_number.split("-")
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
    """

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


# For date of birth and date of a match
def validate_date(date_input: str) -> date | ValidationError: 
    """
    Splits the string and tries to change the numbers in to int and 
    Checks if date format is correct YYYY-MM-DD
    """

    try:
        date_list: list = list(map(int, date_input.split("-")))

        try:
            valid_date = date(date_list[0], date_list[1], date_list[2])
            return valid_date
        
        except:
            raise ValidationError("Not valid date")
        

    except:
        raise ValidationError("Letters are not allowed in a date")



# Date frame for tournament
def validate_date_frame(
        start_date: str,
        end_date: str
        ) -> date | ValidationError:
    """
    Checks if date frame is correct, date_1 is before date_2
    (2025-12-01 -> 2025-12-06)
    """

    valid_date_start = validate_time(start_date)
    valid_date_end = validate_time(end_date)

    if valid_date_start <= valid_date_end:
        return valid_date_start, valid_date_end

    else: 
        raise ValidationError("Not a valid Date frame")


# Time of Match and Tournament time frame
def validate_time(time_input: str) -> time:
    """Checks if time is format is correct HH:MM (12:00)"""

    try:
        time_list = list(map(int, time_input.split(":")))

        try:
            valid_time = time(time_list[0], time_list[1])
            return valid_time
        
        except:
            raise ValidationError("Not a valid time")
    
    except:
        raise ValidationError("Letters are not allowed in time")


# Time frame of tournament
def validate_time_frame(start_time: str, end_time: str) -> time:
    """
    Checks if time frame is correct, time_1 is before time_2 (08:00 -> 16:00)
    """
    
    valid_time_start = validate_time(start_time)
    valid_time_end = validate_time(end_time)

    if valid_time_start <= valid_time_end:
        return valid_time_start, valid_time_end

    else: 
        raise ValidationError("Not a valid Time frame")


