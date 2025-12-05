from enum import StrEnum


class MenuOptions(StrEnum):
    """Enum representing the available menu options in the UI layer."""

    main_menu = "MAIN_MENU"
    quit = "QUIT"
    logout = "LOGOUT"

    # StartPage
    login = "LOGIN"
    register = "REGISTER"
    spectate_screen = "SPECTATE_SCREEN"

    # Login
    admin_page = "ADMIN_PAGE"

    # Login + Register
    player_page = "PLAYER_PAGE"

    # AdminPage
    create_tournament = "CREATE_TOURNAMENT"
    manage_tournament = "MANAGE_TOURNAMENT"
    create_club = "CREATE_CLUB"

    # Manage Tournament
    manage_active_tournament = "MANAGE_ACTIVE_TOURNAMENT"
    manage_inactive_tournament = "MANAGE_INACTIVE_TOURNAMENT"

    # ManageActiveTournament
    input_results = "INPUT_RESULTS"
    select_match = "SELECT_MATCH"

    # ManageInactiveTournament
    manage_teams = "MANAGE_TEAMS"
    publish = "PUBLISH"
    edit_tournament = "EDIT_TOURNAMENT"

    # ManageTeam
    add_team = "ADD_TEAM"
    remove_team = "REMOVE_TEAM"

    # EditTournament
    edit_tournament_time = "EDIT_TOURNAMENT_TIME"
    edit_tournament_info = "EDIT_TOURNAMENT_INFO"

    # PlayerPage
    edit_player_info = "EDIT_PLAYER_INFO"
    my_team_empty = "MY_TEAM_EMPTY"
    my_team_not_empty = "My_TEAM_NOT_EMPTY"
    create_team = "CREATE_TEAM"

    # MyTEAM
    edit_team = "EDIT_TEAM"
    leave_team = "LEAVE_TEAM"

    # EditTeam
    add_player = "ADD_PLAYER"
    remove_player = "REMOVE_PLAYER"

    # SpectatePage

    spectate_players = "SPECTATE_PLAYERS"
    view_player_stats = "VIEW_PLAYER_STATS"

    spectate_clubs = "SPECTATE_CLUBS"
    view_club_stats = "VIEW_CLUB_STATS"

    spectate_teams = "SPECTATE_TEAMS"
    view_team_stats = "VIEW_TEAM_STATS"

    spectate_tournaments = "SPECTATE_TOURNAMENTS"

    # TournamentPage
    active_tournament = "ACTIVE_TOURNAMENT"
    archived_tournament = "ARCHIVED_TOURNAMENT"

    # ActiveTournamentPage
    game_schedule = "GAME_SCHEDULE"
    teams_in_tournament = "TEAMS_IN_TOURNAMENT"
    team_tournament_stats = "TEAM_TOURNAMENT_STATS"
    view_bracket = "VIEW_BRACKET"
