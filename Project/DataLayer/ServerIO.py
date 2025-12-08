"""
Author: Kristinn Hrafn <kristinnd25@ru.is>
Date: 2025-12-05

Functions which let you read, write and update servers
stored in the ./DataLayer/Repository/server.json
"""

import json
from Models import Server

FILE_PATH = "DataLayer/Repository/server.json"

def store_server(server: Server) -> None:
    # Changes object Server into a dictionary mapping attributes to keys.
    data = server.__dict__

    # Reads json file containing server and stores the contents as a
    # dictionary.
    with open(FILE_PATH, "r", encoding='utf-8') as server_file:
        file_content = dict(json.load(server_file))

    # Adds the new server into the dictionary mapping it's uuid to the
    # object for easy lookup.
    file_content[server.uuid] = data
    
    # Writes the updated file content int the json file.
    with open(FILE_PATH, "w", encoding='utf-8') as server_file:
        json.dump(file_content, server_file, indent=4)


def load_server() -> list[Server]:
    # Reads the json file containing servers and stores it as a dictionary.
    with open(FILE_PATH, "r", encoding='utf-8') as server_file:
        file_content = dict(json.load(server_file))

    # Creates a list of all server in the server file.
    # Each server is stored as a Server model object in the list.
    server_list: list[Server] = []
    for value in file_content.values():
        # Uses **value to unpack the dictionary into a Server model object.
        server_list.append(Server(**value))

    return server_list


def update_server(uuid: str, updated_server: Server) -> None:
    # Reads the json file containing server and stores it as a dictionary.
    with open(FILE_PATH, "r", encoding='utf-8') as server_file:
        file_content = dict(json.load(server_file))
   
    # Overwrites the object tied to the given uuid to the object
    # given after checking if it exists to prevent key error.
    if uuid in file_content:
        file_content[uuid] = updated_server.__dict__
    
    # Writes the updated dictionary into the server file.
    with open(FILE_PATH, "w", encoding='utf-8') as server_file:
        json.dump(file_content, server_file, indent=4)
