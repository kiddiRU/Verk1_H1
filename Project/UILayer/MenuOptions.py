from enum import StrEnum


class MenuOptions(StrEnum):
    """Enum representing the available menu options in the UI layer."""

    start_screen = "StartScreen"
    quit = "Quit"
    logout = "LogOut"

    # StartScreen
    login = "LogIn"
    register = "Register"
    spectate_screen = "SpectateScreen"

    # Login
    admin_screen = "AdminScreen"

    # Login + Register
    player_screen = "PlayerScreen"

    # AdminScreen
    create_tournament = "CreateTournament"
    manage_tournament = "ManageTournament"
    create_club = "CreateClub"

    # Manage Tournament
    manage_active_tournament = "ManageActiveTournament"
    manage_inactive_tournament = "ManageInactiveTournament"

    # ManageActiveTournament
    input_results = "InputResults"
    select_match = "SelectMatch"

    # ManageInactiveTournament
    manage_teams = "ManageTeams"
    publish = "Publish"
    edit_tournament = "EditTournament"

    # ManageTeam
    add_team = "AddTeam"
    remove_team = "RemoveTeam"

    # EditTournament
    edit_tournament_time = "EditTournamentTime"
    edit_tournament_info = "EditTournamentInfo"

    # PlayerScreen
    edit_player_info = "EditPlayerInfo"
    my_team_empty = "MyTeam "
    my_team_not_empty = "MyTeam"
    create_team = "CreateTeam "
    create_team_in_team = "CreateTeam"

    # MyTeam
    edit_team = "EditTeam"
    leave_team = "LeaveTeam"

    # EditTeam
    add_player = "AddPlayer"
    remove_player = "RemovePlayer"

    # SpectateScreen
    spectate_players = "SpectatePlayers"
    view_player_stats = "ViewPlayerStats"

    spectate_clubs = "SpectateClubs"
    view_club_stats = "ViewClubStats"

    spectate_teams = "SpectateTeams"
    view_team_stats = "ViewTeamStats"

    spectate_tournaments = "SpectateTournaments"

    # TournamentScreen
    active_tournament = "ActiveTournament"
    archived_tournament = "ArchivedTournament"

    # ActiveTournamentScreen
    game_schedule = "GameSchedule"
    teams_in_tournament = "TeamsInTournament"
    team_tournament_stats = "TeamTournamentStats"


    # Secret
    onion = "Onion"
    masterpiece = "Masterpiece"