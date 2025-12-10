"""
Author: Kristinn Hrafn <kristinnd25@ru.is>
Date: 2025-12-03

Functions which let you read, write and update clubs
stored in the ./DataLayer/Repository/clubs.json
"""

import json
from Models import Club, ValidationError

FILE_PATH = "DataLayer/Repository/clubs.json"


def store_club(club: Club) -> None:
    """Stores new clubs in a json file to be fetched later.

    :param club:
        The club object to store.
    """
    # Changes object club into a dictionary mapping attributes to keys.
    data = club.__dict__

    # Reads json file containing clubs and stores the contents as a
    # dictionary.
    try:
        with open(FILE_PATH, "r") as club_file:
            file_content = dict(json.load(club_file))
    except:
        raise ValidationError("Could not read club file.")

    # Adds the new club into the dictionary mapping it's uuid to the
    # object for easy lookup.
    file_content[club.uuid] = data
    
    # Writes the updated file content back into the json file.
    try:
        with open(FILE_PATH, "w") as club_file:
            json.dump(file_content, club_file, indent=4)
    except:
        raise ValidationError("Could not write into club file")

def load_club() -> list[Club]:
    """Gets a list of all clubs stored with the store_club function.

    :returns:
        The list of clubs.
    """
    # Reads the json file containing clubs and stores it as a dictionary.
    try:
        with open(FILE_PATH, "r") as club_file:
            file_content = dict(json.load(club_file))
    except:
        raise ValidationError("Could not read club file")

    # Creates a list of all clubs in the club file.
    # Each clubs is stored as a Club model object.
    club_list: list[Club] = []
    for value in file_content.values():
        # Uses **value to unpack the dictionary into a Club model object.
        try: 
            club_list.append(Club(**value))
        except:
            raise ValidationError("Could not change file content into Club object.")

    return club_list


def update_club(uuid: str, updated_club: Club) -> None:
    """Updates a club stored with the store_club function.

    Looks for a club stored with the store_club function which
    has the same uuid as the given uuid, then updates that tournament.

    :param uuid:
        uuid to look up the club to update.

    :param updated_club:
        The club object to update the team to.
    """
    # Reads the json file containing clubs and stores it as a dictionary.
    try:
        with open(FILE_PATH, "r") as club_file:
            file_content = dict(json.load(club_file))
    except:
        raise ValidationError("Could not read Club file.")

    # Overwrites the object tied to the given uuid to the object
    # given after checking if it exists to prevent key error.
    if uuid in file_content:
        file_content[uuid] = updated_club.__dict__
    else:
        raise ValidationError("Could not find club with given uuid.")
    
    # Writes the updated dictionary into the club file.
    try:
        with open(FILE_PATH, "w") as club_file:
            json.dump(file_content, club_file, indent=4)
    except:
        raise ValidationError("Could not write into club file.")
