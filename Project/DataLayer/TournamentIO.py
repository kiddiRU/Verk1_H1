"""
Author: Kristinn Hrafn <Kristinnd25@ru.is>
Date: 2025-12-04

Functions which let you read, write and update tournaments
stored in the ./DataLayer/Repository/touranment.json
"""

import json
from datetime import date, datetime
from Models import Tournament, ValidationError

FILE_PATH = "DataLayer/Repository/tournament.json"


def store_tournament(tournament: Tournament) -> None:
    """Stores new tournaments in a JSON file to be fetched later.

    :param tournament:
        The tournament object to store.
    """
    # Changes object tournament into a dictionary, mapping attributes to keys
    data = tournament.__dict__

    # Reads JSON file containing tournaments and stores the contents as a
    # dictionary
    try:
        with open(FILE_PATH, "r", encoding='utf-8') as tournament_file:
            file_content = dict(json.load(tournament_file))
    except:
        raise ValidationError("Could not read tournament file.")

    # Adds the new tournament into the dictionary mapping it's uuid to the
    # object for easy lookup.
    file_content[tournament.uuid] = data

    # Writes the updated file content into the file containing tournaments.
    # Changes all non JSON storable data types into strings with default=str
    try:
        with open(FILE_PATH, "w", encoding='utf-8') as tournament_file:
            json.dump(file_content, tournament_file, indent=4, default=str)
    except:
        raise ValidationError("Could not write into tournament file.")


def load_tournaments() -> list[Tournament]:
    """Gets a list of all tournaments stored with the store_tournament
    function.

    :returns:
        The list of tournaments.
    """
    # Reads the JSON file containing tournaments and stores it as a dictionary
    try:
        with open(FILE_PATH, "r", encoding='utf-8') as tournament_file:
            file_content = dict(json.load(tournament_file))
    except:
        raise ValidationError("Could not read tournament file.")

    # Creates a list of all teams in the tournament file.
    # Each tournament is stored as a Tournament model object in the list.
    tournament_list: list[Tournament] = []
    for value in file_content.values():

        # Changes non JSON storable data types
        # from string back into their original type.
        try:
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
        except:
            raise ValidationError("Could not change attributes into original data types.")
        # Uses **value to unpack the dictionary into a Tournament model object
        try:
            tournament_list.append(Tournament(**value))
        except:
            raise ValidationError("Could not change file content into tournament object.")

    return tournament_list


def update_tournament(uuid: str, updated_tournament: Tournament) -> None:
    """Updates a tournament stored with the store_tournament function.

    Looks for a tournament stored with the store_tournament function which
    has the same uuid as the given uuid, then updates that tournament.

    :param uuid:
        uuid to look up the tournament to update.

    :param updated_tournament:
        The tournament object to update the tournament to.
    """
    # Reads the JSON file containing tournaments adn stores it as a dictionary
    try:
        with open(FILE_PATH, "r", encoding='utf-8') as tournament_file:
            file_content = dict(json.load(tournament_file))
    except:
        raise ValidationError("Could not read tournament file.")

    # Overwrites the object tied to the given uuid to the object
    # given after checking if it exists to prevent key error.
    if uuid in file_content:
        file_content[uuid] = updated_tournament.__dict__
    else:
        raise ValidationError("Could not find tournament with given uuid.")
    
    # Writes the updated dictionary into the tournament file.
    try:
        with open(FILE_PATH, "w", encoding='utf-8') as tournament_file:
            json.dump(file_content, tournament_file, indent=4, default=str)
    except:
        raise ValidationError("Could not write into tournament file.")
