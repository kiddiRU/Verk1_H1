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
    data: dict[str, str | list[str] | None] = {
        "name": team.name,
        "list_player_uuid": team.list_player_uuid,
        "team_captain_uuid": team.team_captain_uuid,
        "club_uuid": team.club_uuid,
        "in_tournament": team.in_tournament,
        "url_homepage": team.url_homepage,
        "ascii_art": team.ascii_art
    }
    
    with open(FILE_PATH, "r") as team_file:
        file_content: dict[str, dict[str, str | list[str] | None]]
        file_content = json.load(team_file)

    file_content[team.uuid] = data

    with open(FILE_PATH, "w") as team_file:
        json.dump(file_content, team_file)

"""
No parameters

Reads json file containing teams and creates a list of
Team model objects of each entry in the json file.

Returns the created team list.
"""
def load_teams() -> list[Team]:
    with open(FILE_PATH, "r") as team_file:
        file_content: dict[str, dict[str, str | list[str] | None]]
        file_content = dict(json.load(team_file))

    team_list: list[Team] = []
    for uuid, value in file_content.items():
        value: dict[str, str | list[str] | None]
        team_list.append(Team(uuid,
                              value["name"],
                              value["list_player_uuid"],
                              value["team_captain_uuid"],
                              value["club_uuid"],
                              value["in_tournament"],
                              value["url_homepage"],
                              value["ascii_art"]))

    return team_list

"""
Takes in uuid, key and value as parameters.

uuid and key have to exist in the json file.

Will attempt to find team with given uuid and update the
value tied to given key of that team.
"""
def update_team(uuid: str, key: str, value: str | list[str] | None) -> None:
    with open(FILE_PATH, "r") as team_file:
        file_content: dict[str, dict[str, str | list[str] | None]]
        file_content = dict(json.load(team_file))
    
    print(uuid, key, value)
    if uuid in file_content:
        if key in file_content[uuid]:
            file_content[uuid][key] = value

    with open(FILE_PATH, "w") as team_file:
        json.dump(file_content, team_file)
