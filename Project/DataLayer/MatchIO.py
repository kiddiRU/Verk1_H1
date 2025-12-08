"""
Author: Kristinn Hrafn <kristinnd25@ru.is>
Date: 2025-12-05

Functions which let you read, write and update servers
stored in the ./DataLayer/Repository/match.json
"""

import json
from Models import Match
from datetime import date, datetime

FILE_PATH = "DataLayer/Repository/match.json"


def store_match(match: Match) -> None:
    # Changes object Match into a dictionary mapping attributes to keys.
    data = match.__dict__

    # Reads json file containing matches and stores the contents as a
    # dictionary.
    with open(FILE_PATH, "r", encoding='utf-8') as match_file:
        file_content = dict(json.load(match_file))

    # Adds the new match into the dictionary mapping it's uuid to the
    # object for easy lookup.
    file_content[match.uuid] = data
    
    # Writes the updated file content back into the json file.
    with open(FILE_PATH, "w", encoding='utf-8') as match_file:
        json.dump(file_content, match_file, indent=4, default=str)


def load_match() -> list[Match]:
    # Reads the json file containing matches and stores it as a dictionary.
    with open(FILE_PATH, "r", encoding='utf-8') as match_file:
        file_content = dict(json.load(match_file))

    # Creates a list of all matches in the server file.
    # Each match is stored as a Match model object in the list.
    match_list: list[Match] = []
    for value in file_content.values():
        # Changing non json storable data types
        # from string back into their original type
        value["match_date"] = date.fromisoformat(value["match_date"])
        value["match_time"] = datetime.strptime(
            value["match_time"],
            "%H:%M:%S"
        ).time()

        # Uses **value to unpack the dictionary into a Match model object.
        match_list.append(Match(**value))

    return match_list


def update_match(uuid: str, updated_match: Match) -> None:
    # Reads the json file containing matches and stores it as a dictionary.
    with open(FILE_PATH, "r", encoding='utf-8') as match_file:
        file_content = dict(json.load(match_file))
    
    # Overwrites the object tied to the given uuid to the object
    # given after checking if it exists to prevent key error.
    if uuid in file_content:
        file_content[uuid] = updated_match.__dict__
    
    # Writes the updated dictionary into the match file.
    with open(FILE_PATH, "w", encoding='utf-8') as match_file:
        json.dump(file_content, match_file, indent=4, default=str)
