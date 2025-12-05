"""
Author: Kristinn Hrafn <kristinnd25@ru.is>
Date: 2025-12-05

Functions which let you read, write and update clubs
stored in the ./DataLayer/Repository/match.json
"""

import json
from Models import Match
from datetime import date, datetime

FILE_PATH = "DataLayer/Repository/match.json"

"""
Takes in model class Match

Inserts information about the Match class into a json file
for storage
"""
def store_match(match: Match) -> None:
    # Chnages object Match into a dictionary mapping attributes to keys.
    data = match.__dict__

    # Reads json file containing match and stores it as a dictionary.
    with open(FILE_PATH, "r") as match_file:
        file_content = dict(json.load(match_file))

    # Updates the dictionary adding the new match into the file content.
    file_content[match.uuid] = data
    
    # Writes the updated file content int the file containing matches.
    with open(FILE_PATH, "w") as match_file:
        json.dump(file_content, match_file, indent=4, default=str)


"""
No parameters

Reads json file containing matches and creates a list of
Match model objects of each entry in the json file.

Returns the created match list.
"""
def load_match() -> list[Match]:
    # Reads the json file containing matches and stores it as a dictionary.
    with open(FILE_PATH, "r") as match_file:
        file_content = dict(json.load(match_file))

    # Creates a list of all matches in the club file.
    # Each match is stored as a Match model object.
    match_list: list[Match] = []
    for value in file_content.values():
        # Changing non json storable data types
        # from string back into original type
        value["match_date"] = date.fromisoformat(value["match_date"])
        value["match_time"] = datetime.strptime(
            value["match_time"],
            "%H:%M:%S"
        ).time()

        # Uses **value to unpack the dictionary into a Match model object.
        match_list.append(Match(**value))

    return match_list


"""
Takes in uuid and the updated Match model object.

uuid has to exist in the json file.

Will attempt to find a match with given uuid and update that
match with the new updated match object.
"""
def update_match(uuid: str, updated_match: Match) -> None:
    # Reads the json file containing matches and stores it as a dictionary.
    with open(FILE_PATH, "r") as match_file:
        file_content = dict(json.load(match_file))
    
    # Updates the file content, checking if the uuid exists
    # in the dictionary.
    if uuid in file_content:
        file_content[uuid] = updated_match.__dict__
    
    # Writes the updated dictionary into the match file.
    with open(FILE_PATH, "w") as match_file:
        json.dump(file_content, match_file, indent=4, default=str)
