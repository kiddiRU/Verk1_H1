"""
Author: Kristinn Hrafn <kristinnd25@ru.is>
Date: 2025-12-05

Functions which let you read, write and update servers
stored in the ./DataLayer/Repository/match.json
"""

import json
from Models import Match, ValidationError
from datetime import date, datetime

FILE_PATH = "DataLayer/Repository/match.json"


def store_match(match: Match) -> None:
    """Stores new matches in a JSON file to be fetched later.

    :param match:
        The match object to store.
    """
    # Changes object Match into a dictionary mapping attributes to keys.
    data = match.__dict__

    # Reads JSON file containing matches and stores the contents as a
    # dictionary.
    try:
        with open(FILE_PATH, "r", encoding='utf-8') as match_file:
            file_content = dict(json.load(match_file))
    except:
        raise ValidationError("Could not read match file.")

    # Adds the new match into the dictionary mapping it's uuid to the
    # object for easy lookup.
    file_content[match.uuid] = data
    
    # Writes the updated file content back into the JSON file.
    try:
        with open(FILE_PATH, "w", encoding='utf-8') as match_file:
            json.dump(file_content, match_file, indent=4, default=str)
    except:
        raise ValidationError("Could not write into match file.")


def load_match() -> list[Match]:
    """Gets a list of all matches stored with the store_match function.

    :returns:
        The list of matches.
    """
    # Reads the JSON file containing matches and stores it as a dictionary.
    try:
        with open(FILE_PATH, "r", encoding='utf-8') as match_file:
            file_content = dict(json.load(match_file))
    except:
        raise ValidationError("Could not read match file")

    # Creates a list of all matches in the server file.
    # Each match is stored as a Match model object in the list.
    match_list: list[Match] = []
    for value in file_content.values():
        # Changes non JSON storable data types
        # from string back into their original type.
        try:
            value["match_date"] = date.fromisoformat(value["match_date"])
            value["match_time"] = datetime.strptime(
                value["match_time"],
                "%H:%M:%S"
            ).time()
        except:
            raise ValidationError("Could not change attributes back")

        # Uses **value to unpack the dictionary into a Match model object.
        try:
            match_list.append(Match(**value))
        except:
            raise ValidationError("Could change file content back into Match object")

    return match_list


def update_match(uuid: str, updated_match: Match) -> None:
    """Updates a match stored with the store_match function.

    Looks for a match stored with the store_match function which
    has the same uuid as the given uuid, then updates that match.

    :param uuid:
        uuid to look up the match to update.

    :param updated_match:
        The match object to update the match to.
    """
    # Reads the JSON file containing matches and stores it as a dictionary.
    try:
        with open(FILE_PATH, "r", encoding='utf-8') as match_file:
            file_content = dict(json.load(match_file))
    except:
        raise ValidationError("Could not read match file")

    # Overwrites the object tied to the given uuid to the object
    # given after checking if it exists to prevent key error.
    if uuid in file_content:
        file_content[uuid] = updated_match.__dict__
    else:
        raise ValidationError("Could not find match with given uuid.")
    
    # Writes the updated dictionary into the match file.
    try:
        with open(FILE_PATH, "w", encoding='utf-8') as match_file:
            json.dump(file_content, match_file, indent=4, default=str)
    except:
        raise ValidationError("Could not write into match file.")
