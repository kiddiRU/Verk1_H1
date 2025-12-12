from Models import Club, Player, Team, Tournament
from DataLayer import DataLayerAPI as dl_api
from uuid import uuid4
import csv, json

club_csv = "init_data/clubs.csv"
player_csv = "init_data/players.csv"
team_csv = "init_data/teams.csv"
tournament_csv = "init_data/tournaments.csv"

with open("DataLayer/Repository/clubs.json", "w") as f: json.dump(dict(), f)
with open("DataLayer/Repository/match.json", "w") as f: json.dump(dict(), f)
with open("DataLayer/Repository/players.json", "w") as f: json.dump(dict(), f)
with open("DataLayer/Repository/server.json", "w") as f: json.dump(dict(), f)
with open("DataLayer/Repository/teams.json", "w") as f: json.dump(dict(), f)
with open("DataLayer/Repository/tournament.json", "w") as f: json.dump(dict(), f)

handle_to_uuid: dict[str, str] = dict()
teams: dict[str, list[str]] = dict()

with open(player_csv, "r") as file:
    reader = csv.DictReader(file)

    for line in reader:
        player_id = str(uuid4())
        
        handle_to_uuid[line["handle"]] = player_id

        if line["team_name"] in teams:
            teams[line["team_name"]].append(player_id)
        else:
            teams[line["team_name"]] = [player_id]

        line.pop("player_id")
        line.pop("team_name")
        dl_api.store_player(Player(**line, uuid=player_id))

club_uuid = []

with open(club_csv, "r") as file:
    reader = csv.DictReader(file)

    for line in reader:
        line["uuid"] = str(uuid4())
        
        club_uuid.append(line["uuid"])

        dl_api.store_club(Club(**line))

with open(team_csv, "r") as file:
    reader = csv.DictReader(file)


    for line in reader:
        line["uuid"] = str(uuid4())
        line["list_player_uuid"] = teams[line["name"]]
        line["team_captain_uuid"] = handle_to_uuid[line["captain_handle"]]
        line["club_uuid"] = club_uuid[int(line["team_id"])%len(club_uuid)]
        line["in_tournament"] = None
        line["ascii_art"] = None
        
        line.pop("team_id")
        line.pop("captain_handle")

        dl_api.store_team(Team(**line))

with open(tournament_csv, "r") as file:
    reader = csv.DictReader(file)

    for line in reader:
        line["uuid"] = str(uuid4())
        
        line["number_of_servers"] = int(line["number_of_servers"])

        dl_api.store_tournament(Tournament(**line))
