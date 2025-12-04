from enum import StrEnum

class MenuOptions(StrEnum):
    """ Enum representing the available menu options in the UI layer. """

    main_menu = "MAIN_MENU"
    back = "BACK"
    quit = "QUIT"
    logout = "LOGOUT"

    # StartPage
    login = "LOGIN"
    register = "REGISTER"
    spectate_page = "SPECTATE_PAGE"

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