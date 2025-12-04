"""
Author: Elmar Sigmarsson <elmars25@ru.is>
Date: 2025-12-03

A validation file that takes inn all info that would need to be validated
"""

from Models.Exception import ValidationError
from DataLayer import DataLayerAPI


def validate_unique_name(unique_name: str, type_of_name: str) -> None:
    """
    Checks if the name is unique and is between 3-40 char in length
    Used for unique player handle, team tournament and club names
    """

    if len(unique_name) >= 3 and len(unique_name) <= 40:
        raise ValidationError("Name needs to be between 3 to 40 characters in length")
    
    if type_of_name is "PLAYER":
        model_player: list = DataLayerAPI.load_players()

        for player in model_player:
            if player.name == unique_name:
                raise ValidationError("Name is already taken")


    #TODO implement check for unique names in team, tournament and club
    if type_of_name is "TEAM":
        pass

    if type_of_name is "TOURNAMENT":
        pass

    if type_of_name is "CLUB":
        pass


def validate_name(name) -> None: # Players full name
    """Checks if the name is in between 3-40 char in length and has only letters"""
    
    if len(name) >= 3 and len(name) <= 40:
        raise ValidationError("Name needs to be between 3 to 40 characters in length")
    
    
def validate_home_address(home_address) -> bool: # Players home address
    """Checks if home address has street name, street number and area (Frostafold 3 Reykjavík)"""
    return home_address

def validate_phone_number(phone_number) -> bool: # Players and tournament contact phone number
    """Checks if phone number is eight in length 7 nums and a dash (123-4567)"""
    return phone_number


def validate_email(email) -> bool: # Players and tournament contact email
    """Checks if email has @, something before the @ and behind it and .XX in the end (johndoe@gmail.com)"""
    return email

def validate_date(date) -> bool: # Date of Birth, Date of Tournament
    """Checks if date format is correct YYYY-MM-DD"""
    return date

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


