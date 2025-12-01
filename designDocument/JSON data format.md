### Player
``` json
{
  "c33430c2-8b58-4652-af49-0b6d6d17e6d2": {
    "name": "Sindri Freysson",
    "handle": "xxKvarturxx",
    "dob": "2006-09-07",
    "home_address": "I am not doxxing myself",
    "phone_number": 7830880,
    "email": "notReal@gmail.com",
    "social": "hamster.com"
  }
```
### Team
```json
{
  "0a6fd7d6-f1c7-4588-ae34-4938c1f942c4": {
    "name": "WarDove",
    "list_of_players": [
      "c33430c2-8b58-4652-af49-0b6d6d17e6d2"
    ],
    "win_counter": 1,
    "club": "Hamstur",
    "history": {
      "tournaments_played": [],
      "club_played_for": [],
      "all_team_members": [
        "c33430c2-8b58-4652-af49-0b6d6d17e6d2"
      ]
    },
    "url_homepage": "",
    "ascii_art": "(╯°□°)╯︵ ┻━┻",
    "status": "archive"
  }
}
```
### Club
```json
{
  "e78402e0-6d0f-4dd0-9906-317d852477e4": {
    "name": "Hamstur",
    "home_town": "Kopavogur",
    "country": "Iceland",
    "win_counter": 1,
    "teams_associated": [
      "0a6fd7d6-f1c7-4588-ae34-4938c1f942c4"
    ],
    "club_color": "yellow",
    "history": {
      "all_teams": [],
      "tournaments_played": []
    }
  }
}
```
### Tournament
```json
{
  "d4547d21-59fc-45a4-a407-8fce97a29ade": {
    "name": "e-girl sports",
    "teams_in_tournament": {
      "0a6fd7d6-f1c7-4588-ae34-4938c1f": {
        "team_members": {},
        "team_club": "UUID"
      }
    },
    "tournament_servers": [
      "966b1815-1376-438f-8008-44b14832412b"
    ],
    "rounds_in_tournament": {},
    "start": "2025-11-27",
    "end": "2025-11-27",
    "venue": "HR",
    "email": "notReal@gmail.com",
    "phone_number": 1234567,
    "status": "unpublished",
    "results": {
      "0a6fd7d6-f1c7-4588-ae34-4938c1f942c4": 1
    }
  }
}
```
### Servers
```json
{
  "988a09a6-236f-4439-8b2b-e1d9cb349e32": {
    "part_of_tournament": "d4547d21-59fc-45a4-a407-8fce97a29ade",
    "hosting_match": "e78402e0-6d0f-4dd0-9906-317d852477e4"
  }
}
```
### Matches
```json
{
  "active": {},
  "archive": {
    "e78402e0-6d0f-4dd0-9906-317d852477e4": {
      "serverID": "966b1815-1376-438f-8008-44b14832412b",
      "part_of_tournament": "d4547d21-59fc-45a4-a407-8fce97a29ade",
      "team1": "e78402e0-6d0f-4dd0-9906-317d852477e4",
      "team2": "988a09a6-236f-4439-8b2b-e1d9cb349e32",
      "time_of_match": {
        "date": "2025-11-27",
        "time": "12:00"
      },
      "winner": "988a09a6-236f-4439-8b2b-e1d9cb349e32"
    }
  }
}
```
