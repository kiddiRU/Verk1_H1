"""
Author: Kristinn Hrafn <kristinnd25@ru.is>
Date: 2025-12-03

Functions which let you read, write and update teams
stored in the ./DataLayer/Repository/teams.json
"""

import json
from Models import Team

FILE_PATH = "DataLayer/Repository/teams.json"

"""
Takes in model class Team

Inserts information about the Team class into a json file
for storage
"""
def store_team(team: Team) -> None:
    # Changes object team int a dictionary mapping attributes to keys.
    data = team.__dict__
   
    # Reads json file containing teams and stores it as a dictionary.
    with open(FILE_PATH, "r") as team_file:
        file_content = dict(json.load(team_file))
    
    # Updates the dictionary adding the new team int the file content.
    file_content[team.uuid] = data
    
    # Writes the updated file content into the file containing teams.
    with open(FILE_PATH, "w") as team_file:
        json.dump(file_content, team_file)

"""
No parameters

Reads json file containing teams and creates a list of
Team model objects of each entry in the json file.

Returns the created team list.
"""
def load_teams() -> list[Team]:
    # Reads the json file containing teams and stores it as a dictionary.
    with open(FILE_PATH, "r") as team_file:
        file_content = dict(json.load(team_file))

    # Creates a list of all teams in the team file.
    # each team stored as a Team model object.
    team_list: list[Team] = []
    for value in file_content.values():
        # Uses **value to unpack the dictionary into a Team model object.
        team_list.append(Team(**value))

    return team_list

"""
Takes in uuid, key and value as parameters.

uuid and key have to exist in the json file.

Will attempt to find team with given uuid and update that
team with the new updated team object.
"""
def update_team(uuid: str, updated_team: Team) -> None:
    # Reads the json file containing players and stores it as a dictionary.
    with open(FILE_PATH, "r") as team_file:
        file_content = dict(json.load(team_file))
   
    # Updates the file content, checking if the uuid exists
    # in the dictionary.
    if uuid in file_content:
        file_content[uuid] = updated_team
    
    # Writes the updated dictionary into the player file.
    with open(FILE_PATH, "w") as team_file:
        json.dump(file_content, team_file)
