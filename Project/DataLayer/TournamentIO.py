"""
Author: Kristinn Hrafn <Kristinnd25@ru.is>
Date: 2025-12-04

Functions which let you read, write and update tournaments
stored in the ./DataLayer/Repository/touranment.json
"""

import json
from Models import Tournament
from datetime import date, datetime

FILE_PATH = "DataLayer/Repository/tournament.json"


def store_tournament(tournament: Tournament) -> None:
    # Changes object tournament into a dictionary, mapping attributes to keys
    data = tournament.__dict__

    # Reads json file containing tournaments and stores the contents as a
    # dictionary
    with open(FILE_PATH, "r", encoding='utf-8') as tournament_file:
        file_content = dict(json.load(tournament_file))

    # Adds the new tournament into the dictionary mapping it's uuid to the
    # object for easy lookup.
    file_content[tournament.uuid] = data

    # Writes the updated file content into the file containing tournaments.
    # Changes all non json storable data types into strings with default=str
    with open(FILE_PATH, "w", encoding='utf-8') as tournament_file:
        json.dump(file_content, tournament_file, indent=4, default=str)


def load_tournaments() -> list[Tournament]:
    # Reads the json file containing tournaments and stores it as a dictionary
    with open(FILE_PATH, "r", encoding='utf-8') as tournament_file:
        file_content = dict(json.load(tournament_file))

    # Creates a list of all teams in the tournament file.
    # Each tournament is stored as a Tournament model object in the list.
    tournament_list: list[Tournament] = []
    for value in file_content.values():

        # Changes non json storable data types
        # from string back into their original type.
        value["start_date"] = date.fromisoformat(value["start_date"])
        value["end_date"] = date.fromisoformat(value["end_date"])
        value["time_frame_start"] = datetime.strptime(
            value["time_frame_start"],
            "%H:%M:%S"
        ).time()
        value["time_frame_end"] = datetime.strptime(
            value["time_frame_end"],
            "%H:%M:%S"
        ).time()
        value["status"] = Tournament.StatusType(value["status"])
    
        # Uses **value to unpack the dictionary into a Tournament model object
        tournament_list.append(Tournament(**value))

    return tournament_list


def update_tournament(uuid: str, updated_tournament: Tournament) -> None:
    # Reads the json file containing tournaments adn stores it as a dictionary
    with open(FILE_PATH, "r", encoding='utf-8') as tournament_file:
        file_content = dict(json.load(tournament_file))

    # Overwrites the object tied to the given uuid to the object
    # given after checking if it exists to prevent key error.
    if uuid in file_content:
        file_content[uuid] = updated_tournament.__dict__
    
    # Writes the updated dictionary into the tournament file.
    with open(FILE_PATH, "w", encoding='utf-8') as tournament_file:
        json.dump(file_content, tournament_file, indent=4, default=str)
