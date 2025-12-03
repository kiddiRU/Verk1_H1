"""
Author: Elmar Sigmarsson <elmars25@ru.is>
Date: 2025-12-03

A validation file that takes inn all info that would need to be validated
"""

def validate_unique_name(): # Player Handle, Tournament, Team, Club names
    """Checks if the name is unique and is between 3-30 char in length"""
    pass

def validate_name(): # Players full name
    """Checks if the name is in between 3-30 char in length and has only letters"""
    pass


def validate_home_address(): # Players home address
    """Checks if home address has street name, street number and area (Frostafold 3 Reykjavík)"""
    pass

def validate_phone_number(): # Players and tournament contact phone number
    """Checks if phone number is eight in length 7 nums and a dash (123-4567)"""
    pass


def validate_email(): # Players and tournament contact email
    """Checks if email has @, something before the @ and behind it and .XX in the end (johndoe@gmail.com)"""
    pass

def validate_date(): # Date of Birth, Date of Tournament
    """Checks if date format is correct YYYY-MM-DD"""
    pass

def validate_date_frame(date_1, date_2): # Date frame of tournament
    """Checks if date frame is correct, date_1 is before date_2 (2025-12-01 -> 2025-12-06)"""
    pass

def validate_time(): # Time of Match and Tournament time frame
    """Checks if time is format is correct HH:MM (12:00)"""
    pass

def validate_time_frame(time_1, time_2): # Time frame of tournament
    """Checks if time frame is correct, time_1 is before time_2 (08:00 -> 16:00) """
    pass


def club_color(): # Club
    """Checks if color is on of the colors implemented (RED, BLUE, YELLOW, GREEN)"""
    pass


