"""
Defines MenuOptions, an enum containing all valid navigation targets
used by the UI layer.
"""

from enum import StrEnum


class MenuOptions(StrEnum):
    """
    Enum representing all available menu options in the UI layer.

    Each value corresponds to a navigation target used by the
    application's screen-routing system.
    """

    START_SCREEN = "StartScreen"
    QUIT = "Quit"
    LOGOUT = "LogOut"

    # StartScreen
    LOGIN = "LogIn"
    REGISTER = "Register"
    SPECTATE_SCREEN = "SpectateScreen"

    # Login
    ADMIN_SCREEN = "AdminScreen"

    # Login + Register
    PLAYER_SCREEN = "PlayerScreen"

    # AdminScreen
    CREATE_TOURNAMENT = "CreateTournament"
    MANAGE_TOURNAMENT = "ManageTournament"
    CREATE_CLUB = "CreateClub"

    # Manage Tournament
    MANAGE_ACTIVE_TOURNAMENT = "ManageActiveTournament"
    MANAGE_INACTIVE_TOURNAMENT = "ManageInactiveTournament"

    # ManageActiveTournament
    INPUT_RESULTS = "InputResults"
    SELECT_MATCH = "SelectMatch"

    # ManageInactiveTournament
    MANAGE_TEAMS = "ManageTeams"
    PUBLISH = "Publish"

    # ManageTeam
    ADD_TEAM = "AddTeam"
    REMOVE_TEAM = "RemoveTeam"

    # PlayerScreen
    EDIT_PLAYER_INFO = "EditPlayerInfo"
    MY_TEAM_EMPTY = "MyTeam "
    MY_TEAM_NOT_EMPTY = "MyTeam"
    CREATE_TEAM = "CreateTeam "
    CREATE_TEAM_IN_TEAM = "CreateTeam"

    # MyTeam
    EDIT_TEAM = "EditTeam"
    LEAVE_TEAM = "LeaveTeam"

    # EditTeam
    ADD_PLAYER = "AddPlayer"
    REMOVE_PLAYER = "RemovePlayer"

    # SpectateScreen
    SPECTATE_PLAYERS = "SpectatePlayers"
    VIEW_PLAYER_STATS = "ViewPlayerStats"

    SPECTATE_CLUBS = "SpectateClubs"
    VIEW_CLUB_STATS = "ViewClubStats"

    SPECTATE_TEAMS = "SpectateTeams"
    VIEW_TEAM_STATS = "ViewTeamStats"

    SPECTATE_TOURNAMENTS = "SpectateTournaments"

    # TournamentScreen
    ACTIVE_TOURNAMENT = "ActiveTournament"
    ARCHIVED_TOURNAMENT = "ArchivedTournament"

    # ActiveTournamentScreen
    GAME_SCHEDULE = "GameSchedule"
    TEAMS_IN_TOURNAMENT = "TeamsInTournament"
    TEAM_TOURNAMENT_STATS = "TeamTournamentStats"

    # Secret
    ONION = "Onion"
    MASTERPIECE = "Masterpiece"
    SINDRI_FC = "Sindri Fan Club"
