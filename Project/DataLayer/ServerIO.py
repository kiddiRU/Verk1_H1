"""
Author: Kristinn Hrafn <kristinnd25@ru.is>
Date: 2025-12-05

Functions which let you read, write and update servers
stored in the ./DataLayer/Repository/server.json
"""

import json
from Models import Server

FILE_PATH = "DataLayer/Repository/server.json"

"""
Takes in model class Server

Inserts information about the Server class into a json file
for storage
"""
def store_server(server: Server) -> None:
    # Changes object Server into a dictionary mapping attributes to keys.
    data = server.__dict__

    # Reads json file containing server and stores it as a dictionary.
    with open(FILE_PATH, "r", encoding='utf-8') as server_file:
        file_content = dict(json.load(server_file))

    # Updates the dictionary adding the new server into the file content.
    file_content[server.uuid] = data
    
    # Writes the updated file content int the file containing servers.
    with open(FILE_PATH, "w", encoding='utf-8') as server_file:
        json.dump(file_content, server_file, indent=4)


"""
No parameters

Reads json file containing servers and creates a list of
Server model objects of each entry in the json file.

Returns the created server list.
"""
def load_server() -> list[Server]:
    # Reads the json file containing Server and stores it as a dictionary.
    with open(FILE_PATH, "r", encoding='utf-8') as server_file:
        file_content = dict(json.load(server_file))

    # Creates a list of all server in the server file.
    # Each server is stored as a Server model object.
    server_list: list[Server] = []
    for value in file_content.values():
        # Uses **value to unpack the dictionary into a Server model object.
        server_list.append(Server(**value))

    return server_list


"""
Takes in uuid and the updated Server model object.

uuid has to exist in the json file.

Will attempt to find a server with given uuid and update that
server with the new updated server object.
"""
def update_server(uuid: str, updated_server: Server) -> None:
    # Reads the json file containing server and stores it as a dictionary.
    with open(FILE_PATH, "r", encoding='utf-8') as server_file:
        file_content = dict(json.load(server_file))
    
    # Updates the file content, checking if the uuid exists
    # in the dictionary.
    if uuid in file_content:
        file_content[uuid] = updated_server.__dict__
    
    # Writes the updated dictionary into the server file.
    with open(FILE_PATH, "w", encoding='utf-8') as server_file:
        json.dump(file_content, server_file, indent=4)
