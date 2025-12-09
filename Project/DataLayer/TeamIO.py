"""
Author: Kristinn Hrafn <kristinnd25@ru.is>
Date: 2025-12-03

Functions which let you read, write and update teams
stored in the ./DataLayer/Repository/teams.json
"""

import json
from Models import Team, ValidationError

FILE_PATH = "DataLayer/Repository/teams.json"

def store_team(team: Team) -> None:
    # Changes object team into a dictionary mapping attributes to keys.
    data = team.__dict__
   
    # Reads json file containing teams and stores the contents as a
    # dictionary.
    try:
        with open(FILE_PATH, "r", encoding='utf-8') as team_file:
            file_content = dict(json.load(team_file))
    except:
        raise ValidationError("Could not read team file.")
   
    # Adds the new team into the dictionary mapping it's uuid to the
    # object for easy lookup.
    file_content[team.uuid] = data
    
    # Writes the updated file content into the file containing teams.
    try:
        with open(FILE_PATH, "w", encoding='utf-8') as team_file:
            json.dump(file_content, team_file, indent=4)
    except:
        raise ValidationError("Could not write into team file.")

def load_teams() -> list[Team]:
    # Reads the json file containing teams and stores it as a dictionary.
    try:
        with open(FILE_PATH, "r", encoding='utf-8') as team_file:
            file_content = dict(json.load(team_file))
    except:
        raise ValidationError("Could not read team file.")

    # Creates a list of all teams in the team file.
    # each team stored as a Team model object in the list.
    team_list: list[Team] = []
    for value in file_content.values():
        # Uses **value to unpack the dictionary into a Team model object.
        try:
            team_list.append(Team(**value))
        except:
            raise ValidationError("Could not change file content into Team object.")

    return team_list

def update_team(uuid: str, updated_team: Team) -> None:
    # Reads the json file containing teams and stores it as a dictionary.
    try:
        with open(FILE_PATH, "r", encoding='utf-8') as team_file:
            file_content = dict(json.load(team_file))
    except:
        raise ValidationError("Could not read team file.")

    # Overwrites the object tied to the given uuid to the object
    # given after checking if it exists to prevent key error.
    if uuid in file_content:
        file_content[uuid] = updated_team.__dict__
    else:
        raise ValidationError("Could not find team with given uuid")
    
    # Writes the updated dictionary into the team file.
    try:
        with open(FILE_PATH, "w", encoding='utf-8') as team_file:
            json.dump(file_content, team_file, indent=4)
    except:
        raise ValidationError("Could not write into team file.")
