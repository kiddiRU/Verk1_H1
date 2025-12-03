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

    # ManageTournament + 