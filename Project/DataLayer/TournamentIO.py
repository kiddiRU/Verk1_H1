"""
Author: Kristinn Hrafn <Kristinnd25@ru.is>
Date: 2025-12-04

Functions which let you read, write and update tournaments
stored in the ./DataLayer/Repository/touranment.json
"""

import json
from Models import Tournament
from datetime import date, time

FILE_PATH = "DataLayer/Repository/tournament.json"

def store_tournament(tournament: Tournament) -> None:
    data = tournament.__dict__

    data["start_date"] = str(data["start_date"])
    data["end_date"] = str(data["end_date"])
    data["time_frame_start"] = str(data["time_frame_start"])
    data["time_frame_end"] = str(data["time_frame_end"])
    data["status"] = str(data["status"])

    with open(FILE_PATH, "r") as tournament_file:
        file_content = dict(json.load(tournament_file))

    file_content[tournament.uuid] = data

    with open(FILE_PATH, "w") as tournament_file:
        json.dump(file_content, tournament_file, indent=2)


