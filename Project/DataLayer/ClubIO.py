"""
Author: Kristinn Hrafn <kristinnd25@ru.is>
Date: 2025-12-03

Functions which let you read, write and update clubs
stored in the ./DataLayer/Repository/clubs.json
"""

import json
from Models import Club

FILE_PATH = "DataLayer/Repository/clubs.json"

"""
Takes in model class Club

Inserts information about the Club class into a json file
for storage
"""
def store_club(club: Club) -> None:
    # Chnages object blub into a dictionary mapping attributes to keys.
    data = club.__dict__

    # Reads json file containing clubs and stores it as a dictionary.
    with open(FILE_PATH, "r") as club_file:
        file_content = dict(json.load(club_file))

    # Updates the dictionary addint the new club into the file content.
    file_content[club.uuid] = data
    
    # Writes the updated file content int the file containing clubs.
    with open(FILE_PATH, "w") as club_file:
        json.dump(file_content, club_file, indent=4)


"""
No parameters

Reads json file containing clubs and creates a list of
Club model objects of each entry in the json file.

Returns the created club list.
"""
def load_club() -> list[Club]:
    # Reads the json file containing clubs and stores it as a dictionary.
    with open(FILE_PATH, "r") as club_file:
        file_content = dict(json.load(club_file))

    # Creates a list of all clubs in the club file.
    # Each clubs is stored as a Club model object.
    club_list: list[Club] = []
    for value in file_content.values():
        # Uses **value to unpack the dictionary into a Club model object.
        club_list.append(Club(**value))

    return club_list


"""
Takes in uuid and the updated Club model object.

uuid has to exist in the json file.

Will attempt to find a club with given uuid and update that
club with the new updated club object.
"""
def update_club(uuid: str, updated_club: Club) -> None:
    # Reads the json file containing clubs and stores it as a dictionary.
    with open(FILE_PATH, "r") as club_file:
        file_content = dict(json.load(club_file))
    
    # Updates the file content, checking if the uuid exists
    # in the dictionary.
    if uuid in file_content:
        file_content[uuid] = updated_club.__dict__
    
    # Writes the updated dictionary into the club file.
    with open(FILE_PATH, "w") as club_file:
        json.dump(file_content, club_file, indent=4)
