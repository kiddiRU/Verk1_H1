"""
Author: Kristinn Hrafn <kristinnd25@ru.is>
Date: 2025-12-05

Functions which let you read, write and update servers
stored in the ./DataLayer/Repository/server.json
"""

import json
from Models import Server, ValidationError

FILE_PATH = "DataLayer/Repository/server.json"


def store_server(server: Server) -> None:
    """Stores new servers in a JSON file to be fetched later.

    :param server:
        The server object to store.
    """
    # Changes object Server into a dictionary mapping attributes to keys.
    data = server.__dict__

    # Reads JSON file containing server and stores the contents as a
    # dictionary.
    try:
        with open(FILE_PATH, "r", encoding='utf-8') as server_file:
            file_content = dict(json.load(server_file))
    except Exception:
        raise ValidationError("Could not read server file.")

    # Adds the new server into the dictionary mapping it's uuid to the
    # object for easy lookup.
    file_content[server.uuid] = data

    # Writes the updated file content int the JSON file.
    try:
        with open(FILE_PATH, "w", encoding='utf-8') as server_file:
            json.dump(file_content, server_file, indent=4)
    except Exception:
        raise ValidationError("Could not write into server file.")


def load_server() -> list[Server]:
    """Gets a list of all servers stored with the store_server function.

    :returns:
        The list of servers.
    """
    # Reads the JSON file containing servers and stores it as a dictionary.
    try:
        with open(FILE_PATH, "r", encoding='utf-8') as server_file:
            file_content = dict(json.load(server_file))
    except Exception:
        raise ValidationError("Could not read server file.")

    # Creates a list of all server in the server file.
    # Each server is stored as a Server model object in the list.
    server_list: list[Server] = []
    for value in file_content.values():
        # Uses **value to unpack the dictionary into a Server model object.
        try:
            server_list.append(Server(**value))
        except Exception:
            raise ValidationError(
                "Could not change file content into Server object."
            )

    return server_list


def update_server(uuid: str, updated_server: Server) -> None:
    """Updates the server stored with the store_server function.

    Looks for a servers stored with the store_server function which
    has the same uuid as the given uuid, then updates that server.

    :param uuid:
        uuid to look up the server to update.

    :param updated_server:
        The server object to update the server to.
    """
    # Reads the JSON file containing server and stores it as a dictionary.
    try:
        with open(FILE_PATH, "r", encoding='utf-8') as server_file:
            file_content = dict(json.load(server_file))
    except Exception:
        raise ValidationError("Could not read server file.")

    # Overwrites the object tied to the given uuid to the object
    # given after checking if it exists to prevent key error.
    if uuid in file_content:
        file_content[uuid] = updated_server.__dict__
    else:
        raise ValidationError("Could not find server with given uuid.")

    # Writes the updated dictionary into the server file.
    try:
        with open(FILE_PATH, "w", encoding='utf-8') as server_file:
            json.dump(file_content, server_file, indent=4)
    except Exception:
        raise ValidationError("Could not write into server file.")
