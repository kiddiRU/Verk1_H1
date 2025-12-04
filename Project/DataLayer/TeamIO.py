"""
Author: Kristinn Hrafn <kristinnd25@ru.is>
Date: 2025-12-03

Functions which let you read, write and update teams
stored in the ./DataLayer/Repository/teams.json
"""

import json
from Models import Team

FILE_PATH = "./DataLayer/Repository/teams.json"

def store_team(team: Team) -> None:
    data = {
        "name": team.name,
        "list_player_uuid": team.list_player_uuid,
        "team_captain_uuid": team.team_captain_uuid,
        "club_uuid": team.club_uuid,
        "in_tournament": team.in_tournament,
        "url_homepage": team.url_homepage,
        "ascii_art": team.ascii_art
    }
    
    with open(FILE_PATH, "r") as team_file:
        file_content = json.load(team_file)

    file_content[team.uuid] = data

    with open(FILE_PATH, "w") as team_file:
        json.dump(file_content, team_file)

def load_teams() -> list[Team]:
    with open(FILE_PATH, "r") as team_file:
        file_content = dict(json.load(team_file))

    team_list: list[Team] = []
    for uuid, value in file_content.items():
        team_list.append(Team(uuid,
                              value["name"],
                              value["list_player_uuid"],
                              value["team_captain_uuid"],
                              value["club_uuid"],
                              value["in_tournament"],
                              value["url_homepage"],
                              value["ascii_art"]))

    return team_list

def update_team(uuid: str, key: str, value) -> None:
    with open(FILE_PATH, "r") as team_file:
        file_content = dict(json.load(team_file))

    if uuid in file_content:
        if key in file_content:
            file_content[uuid][key] = value

    with open(FILE_PATH, "w") as team_file:
        json.dump(file_content, team_file)
