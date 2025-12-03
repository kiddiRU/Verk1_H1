from Models import Club, Match, Player, Server, Team, Tournament

class LogicAPI:
    ''' Logic Layer API '''

    # TODO implement __init__
    def __init__(self):
        pass

    ''' Player API '''

    # TODO implement validate_info and call it
    def validate_info(self) -> None: # ? 
        pass

    # TODO implement create_player and call it
    def create_player(
            self,
            name: str,
            home_address: str,
            phone_number: str, 
            date_of_birth: str, 
            handle: str, 
            email: str = '',
            url: str = ''
            ) -> Player:

        pass

    # TODO implement change_player_info and call it
    def change_player_info(self, player: Player) -> None:
        pass

    # TODO implement create_team and call it
    def create_team(self, name: str, team_captain: Player, club: Club) -> Team:
        pass

    # TODO implement leave_team and call it
    def leave_team(self, team: Team, player: Player) -> None:
        pass

    ''' Team API '''

    # TODO implement validate_unique and call it
    def validate_unique_name(self, name: str) -> bool:
        pass

    # TODO implement add_player and call it
    def add_player(self, team: Team, player: Player) -> None:
        pass

    # TODO implement remove_player and call it
    def remove_player(self, team: Team, player: Player) -> None:
        pass

    # TODO implement get_team_members and call it
    def get_team_members(self, team: Team) -> list[Player]:
        pass

    # TODO implement get_team_history and call it
    def get_team_history(self, team: Team) -> list:       
        pass

    ''' Tournament API '''

    # TODO implement validate_unique_name and call it
    def validate_unique_name(self, name: str) -> bool:
        pass

    # TODO implement create_tournament and call it
    def create_tournament(
            self, 
            name: str,
            start_date: str,
            end_date: str,
            venue: str,
            teams: dict[Team.uuid, list[Player]],
            teams_playing: list[Team],
            email: str,
            phone_number: str,
            status: Status = Status.INACTIVE
          # list_of_servers: list[uuid: str] ?
            ) -> Tournament:

        pass

    # TODO implement publish and call it
    def publish(self, tournament: Tournament) -> None:
        pass

    # TODO implement add_team and call it
    def add_team(self, tournament: Tournament, team: Team) -> None:
        pass

    # TODO implement remove_team and call it
    def remove_team(self, tournament: Tournament, team: Team) -> None:
        pass

    # TODO implement change_info and call it
    def change_info(self, tournament: Tournament) -> None:
        pass

    # TODO implement next_round and call it
    def next_round(self) -> None:
        pass

    # TODO implement cancel_tournament and call it
    def cancel_tournament(self, tournament: Tournament) -> None:
        pass

    ''' Club API '''

    # TODO implement validate_unique_name and call it
    def validate_unique_name(self, name: str) -> None:
        pass

    # TODO implement create_club and call it
    def create_club(self) -> Club:
        pass

    # TODO implement change_club_info and call it
    def change_club_info(self, club: Club) -> None:
        pass

    ''' Match API '''

    # TODO implement input_match_results and call it
    def input_match_results(self, match: Match) -> None:
        pass