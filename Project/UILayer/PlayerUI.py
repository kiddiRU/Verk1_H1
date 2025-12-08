"""
Author: Ísak Elí Hauksson <isak25@ru.is>
Date: 2025-12-04

Co-Author: Andri Már Kristjánsson <andrik25@ru.is>

File that holds all the menus that the player can access
"""

from UILayer.MenuOptions import MenuOptions
from UILayer.UtilityUI import UtilityUI
from UILayer.Drawer import Drawer
from LogicLayer import LogicLayerAPI
from Models.Player import Player
from Models.Club import Club


class PlayerUI:
    """Every player menu option"""

    def __init__(self) -> None:
        self.utility = UtilityUI()
        self.tui = Drawer()
        self.message_color = "\033[36m"
        self.reset: str = "\033[0m"
        self.underscore = "\033[4m"


    def start_screen(self) -> MenuOptions:
        """Start screen with choices: 1, 2, 3 and q
        1: go to login screen
        2: go to register screen
        3: go to spectating page
        1: quit program

        Returns:
            MenuOptions: The next menu to navigate to
        """
        
        menu: str = "Start Page"
        user_path: list[str] = [MenuOptions.start_screen]
        info: list[str]= []
        options: dict[str, str]= {"1": "Log in", "2": "Register", "3": "Spectate", "q": "Quit program"}
        message: str = ""

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options, message))  


        choice: str = self.utility._prompt_choice(["1", "2", "3", "q"])
        match choice:
            case "1":
                return MenuOptions.login
            case "2":
                return MenuOptions.register
            case "3":
                return MenuOptions.spectate_screen
            case "q":
                return MenuOptions.quit

        return MenuOptions.start_screen



    def login_screen(self) -> MenuOptions:
        """Login screen, choices: fill info with input

        Returns:
            MenuOptions: The next menu to navigate to
        """

        player_list: list[Player] = LogicLayerAPI.list_players()
        player_handles: list[str] = [x.handle for x in player_list]

        menu: str = "Login"
        user_path: list[str] = [MenuOptions.start_screen, MenuOptions.login]
        info: list[str]= []
        options: dict[str, str]= {"t": "Try Again", "b": "Back"}
        message: str = "Handle Not Found!"
     
        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info))

        login_handle: str = input(self.message_color + "Input Your Handle: " + self.reset)

        match login_handle:
            case "admin":
                return MenuOptions.admin_screen
            case "Shrek":
                return MenuOptions.onion
            case "masterpiece":
                return MenuOptions.masterpiece
        
        if login_handle in player_handles:
            LogicLayerAPI.save_player(login_handle)


            return MenuOptions.player_screen
        
        print(self.tui.table(menu, user_path, info, options, message))

        if login_handle == "list of handles":
            for x in player_handles:
                print(x)

        choice: str = self.utility._prompt_choice(["t", "b"])

        if choice == "t":
            return MenuOptions.login
        
        return MenuOptions.start_screen
        


    def register_screen(self) -> MenuOptions:
        """Register screen, choices: fill info with input

        Returns:
            MenuOptions: The next menu to navigate to
        """
        # TODO: add fill in option  
        
        menu: str = "Register"
        user_path: list[str] = [MenuOptions.start_screen, MenuOptions.login, MenuOptions.register]
        info: list[str]= []
        options: dict[str, str]= {"c": "Continue"}
        message: str = "You Have Created A Player!"

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info))  
        user_name: str = self.utility._input_info("Enter Name: \n", "name", "PLAYER")
        self.tui.save_input("Name: " + user_name)


        print(self.tui.table(menu, user_path, info)) 
        user_dob: str = str(self.utility._input_info("Enter Date Of Birth: (yyyy-mm-dd) \n", "date_of_birth", "PLAYER"))
        self.tui.save_input("Date Of Birth: " + str(user_dob))


        print(self.tui.table(menu, user_path, info)) 
        user_addr: str = self.utility._input_info("Enter Home Address: (Streetname 00 Cityname)\n", 
                                                  "home_address", "PLAYER")
        self.tui.save_input("Home Address: " + user_addr)


        print(self.tui.table(menu, user_path, info))
        user_email: str = self.utility._input_info("Enter Email: \n", "email", "PLAYER")
        self.tui.save_input("Email: " + user_email)


        print(self.tui.table(menu, user_path, info))   
        user_phnum: str = self.utility._input_info("Enter Phone Number: 123-4567 \n", "phone_number", "PLAYER")
        self.tui.save_input("Phone Number: " + user_phnum)


        print(self.tui.table(menu, user_path, info))   
        user_handle: str = self.utility._input_info("Enter Handle: \n", "handle", "PLAYER")
        self.tui.save_input("Handle: " + user_handle)


        print(self.tui.table(menu, user_path, info))   
        user_url: str = input("Enter URL: (ooptional) \n") #TODO: This is just a basic input
        self.tui.save_input("URL: " + user_url)
        print(self.tui.table(menu, user_path, info, options, message))
        con: str = self.utility._prompt_choice(["c"])

        LogicLayerAPI.create_player(user_name, user_dob, user_addr, user_email, user_phnum, user_handle, user_url)

        LogicLayerAPI.save_player(user_handle)
        
        #if register
        return MenuOptions.player_screen
        #if cancel: return MenuOptions.main_menu



    def player_screen(self) -> MenuOptions:
        """Player page, choices: 1,2,3 and b
        1: Edit info
        2: See team
        3: Create a team
        b: back to main menu

        Returns:
            MenuOptions: The next menu to navigate to
        """
        
        current_login_handle = LogicLayerAPI.save_player()

        player_list: list[Player] = LogicLayerAPI.list_players()

        current_login_name = None
        current_login_dob = None
        current_login_addr = None
        current_login_phnum = None
        current_login_email = None
        current_login_team = None
        current_login_club = None
        current_login_rank = "Player"
        
        for player in player_list:
            if player.handle == current_login_handle:
                current_login_name = player.name
                current_login_dob = player.date_of_birth
                current_login_addr = player.home_address
                current_login_phnum = player.phone_number
                current_login_email = player.email



        menu: str = "Player Page"
        user_path: list[str] = [MenuOptions.player_screen]

        #Temporary info for testing, needs to get info from the actual info files
        info: list[str]= [f"""Name: {current_login_name}
Date of Birth: {current_login_dob}
Home Address: {current_login_addr}
Phone Number: {current_login_phnum}
Email: {current_login_email}
Handle: {current_login_handle}
Team: {current_login_team}
Club: {current_login_club}
Rank: {current_login_rank}"""]
        
        options: dict[str, str]= {"1": "Edit Info", "2": "My Team", "3": "Create a Team", "lo": "Log Out"}
        message: str = ""

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options, message))

        choice: str = self.utility._prompt_choice(["1", "2", "3", "lo"])
        match choice:
            case "1":
                return MenuOptions.edit_player_info
            case "2":
                if ...:  # TODO: check if team is empty aka if player not in a team
                    return MenuOptions.my_team_not_empty
                return MenuOptions.my_team_empty
            case "3":
                # if ...:  # TODO: check if player is already in a team
                #     print("You are already in a team")
                #     return MenuOptions.player_page
                return MenuOptions.create_team
            case "lo":
                return MenuOptions.logout


        return MenuOptions.start_screen
    


    def create_team(self) -> MenuOptions:
        """Create team screen, choices: fill info with input

        Returns:
            MenuOptions: The next menu to navigate to
        """

        menu: str = "Create Team"
        user_path: list[str] = [MenuOptions.player_screen, MenuOptions.create_team]

        #temporary info
        info: list[str]= ["- - - -List Of Clubs- - - -"]
        
        options: dict[str, str]= {"c": "Continue", "b": "Back"}
        message: str = "By Creating A Team You Are Assigned As The Captain Of It!"


        #clubs = LogicLayerAPI.list_clubs()
        #for club in clubs:
            #info.append(club)
            

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, [], {}, message))
        team_name: str | None = self.utility._input_info("Enter Team Name: \n", "name", "TEAM")
        if team_name != None:
            self.tui.save_input("Team Name: " + team_name)

        print(self.tui.table(menu, user_path))
        team_url: str = input("Enter Team URL (Optional): \n") #TODO: This is just a basic input
        self.tui.save_input("Team Name: " + team_url)

        print(self.tui.table(menu, user_path))
        team_ascii: str = input("Enter Team ASCII Art (Optional): \n") #TODO: This is just a basic input
        self.tui.save_input("Team ASCII Art: " + team_ascii)

        print(self.tui.table(menu, user_path, info))
        team_club: str = input("Choose A Club To Join: \n") #TODO: This is just a basic input
        self.tui.save_input("Club: " + team_club)

        print(self.tui.table(menu, user_path, info, options))
        choice: str = self.utility._prompt_choice(["c", "b"])

        #LogicLayerAPI.create_team(team_name, "", team_club, team_url, team_ascii)

        #name: str, team_captain: Player, club_name: Club, url: str, ascii_art: str
        
        if choice == "c":
            return MenuOptions.my_team_not_empty
        
 
        return MenuOptions.player_screen



    def edit_player_info(self) -> MenuOptions:
        """Edit player info screen, choices: fill info with input

        Returns:
            MenuOptions: The next menu to navigate to
        """

        # This Uses A temporary way to print out and change info
        # TODO: 

        user_name = "LOGIC"
        dob = "LOGIC"
        addr = "LOGIC"
        phnum = "LOGIC"
        email = "LOGIC"
        url = "LOGIC"



        menu: str = "Edit Player Info"
        user_path: list[str] = [MenuOptions.player_screen, MenuOptions.edit_player_info]
        info: list[str]= []
        options: dict[str, str]= {"c": "Continue", "b": "Back"}
        message: str = "You Have Changed Your Info!"

        self.tui.clear_saved_data()
        self.tui.save_input(f"- - - -{"PLAYERNAME"}- - - -")
        unchanged_message = "(Leave Field Empty If You Want To Leave Them Unchanged)"    

        print(self.tui.table(menu, user_path, info))
        new_name = input(unchanged_message + "\n Enter New Name: \n") #TODO: This is just a basic input
        if new_name:
            user_name = new_name
        self.tui.save_input("Name: " + user_name)

        print(self.tui.table(menu, user_path, info))
        new_dob = input(unchanged_message + "\n Enter New Date Of Birth: \n") #TODO: This is just a basic input
        if new_dob:
            dob = new_dob
        self.tui.save_input("Date Of Birth: " + dob)

        print(self.tui.table(menu, user_path, info))        
        new_addr = input(unchanged_message + "\n Enter New Home Address: \n") #TODO: This is just a basic input
        if new_addr:
            addr = new_addr
        self.tui.save_input("Home Address: " + addr)

        print(self.tui.table(menu, user_path, info))
        new_phnum = input(unchanged_message + "\n Enter New Phone Number: \n") #TODO: This is just a basic input
        if new_phnum:
            phnum = new_phnum
        self.tui.save_input("Phone Number: " + phnum)

        print(self.tui.table(menu, user_path, info))
        new_email = input(unchanged_message + "\n Enter New Email: \n") #TODO: This is just a basic input
        if new_email:
            email = new_email
        self.tui.save_input("Email: " + email)

        print(self.tui.table(menu, user_path, info))
        new_url = input(unchanged_message + "\n Enter New Email: \n") #TODO: This is just a basic input
        if new_url:
            url = new_url
        self.tui.save_input("URL: " + url)

        
        print(self.tui.table(menu, user_path, info, options, message))

        
        return MenuOptions.player_screen
    


    def my_team_empty(self) -> MenuOptions:
        """My team screen when team is empty, choices: b to go back

        Returns:
            MenuOptions: The next menu to navigate to
        """

        menu: str = "My Team"
        user_path: list[str] = [MenuOptions.player_screen, MenuOptions.my_team_empty]
        info: list[str]= []
        options: dict[str, str]= {"b": "Back"}
        message: str = "You Are Not In A Team!"
        
        self.tui.clear_saved_data()

        print(self.tui.table(menu, user_path, info, options, message))

        choice: str = self.utility._prompt_choice(["b"])
        match choice:
            case "b":
                return MenuOptions.player_screen
        return MenuOptions.player_screen
    


    def my_team_not_empty(self) -> MenuOptions:
        """My team screen when team is not empty, choices: 1,2 and b
        1: edit team
        2: leave team
        b: back to player page

        Returns:
            MenuOptions: The next menu to navigate to
        """
       
        menu: str = "My Team"
        user_path: list[str] = [MenuOptions.player_screen, MenuOptions.my_team_not_empty]
        info: list[str]= [f"""- - - -{"TEAMNAME"}- - - -
{self.underscore + "Rank:" + self.reset}{self.underscore + "Handle:": >21}
{self.reset + "Captain"}{"PLAYERHANDLE": >20}
{"Player"} {"PLAYERHANDLE": >20}
{"Player"} {"PLAYERHANDLE": >20}"""]
        options: dict[str, str]= {"1": "Edit Team", "2": "Leave Team", "b": "Back"}
        message: str = ""
        
        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options))


        choice: str = self.utility._prompt_choice(["1", "2", "b"])
        match choice:
            case "1": #TODO: check if player is captain and CAN edit the team
                return MenuOptions.edit_team
            case "2":
                if ...:  # TODO: check if player is captain
                    return MenuOptions.leave_team
            case "b":

                return MenuOptions.player_screen
        return MenuOptions.player_screen



    def edit_team(self) -> MenuOptions:
        """Edit team screen, choices: 1,2 and b
        1: Add player to team
        2: Remove player from team
        b: back to My Team

        Returns:
            MenuOptions: The next menu to navigate to
        """

        menu: str = "Edit Team"
        user_path: list = [MenuOptions.player_screen, MenuOptions.my_team_not_empty, MenuOptions.edit_team]
        info: list[str]= [f"""- - - -{"TEAMNAME"}- - - -
{self.underscore + "Rank:" + self.reset}{self.underscore + "Handle:": >21}
{self.reset + "Captain"}{"PLAYERHANDLE": >20}
{"Player"} {"PLAYERHANDLE": >20}
{"Player"} {"PLAYERHANDLE": >20}"""]
        options: dict[str, str]= {"1": "Add Player To Team", "2": "Remove Player From Team", "b": "Back"}
        message: str = ""
        
        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options))

        choice: str = self.utility._prompt_choice(["1", "2", "b"])
        match choice:
            case "1": #TODO: check if player is captain and CAN edit the team
                return MenuOptions.add_player
            case "2":
                if ...:  # TODO: check if player is captain
                    return MenuOptions.remove_player
            case "b":
                return MenuOptions.my_team_not_empty

        return MenuOptions.player_screen



    def add_player(self) -> MenuOptions:
        """Add player to team screen, choices: input player handle to add

        Returns:
            MenuOptions: The next menu to navigate to
        """
        
        menu: str = "Add Player"
        user_path: list = [MenuOptions.player_screen, MenuOptions.my_team_not_empty, MenuOptions.edit_team, MenuOptions.add_player]
        info: list = []
        options: dict = {"c": "Continue"}

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path))

        # Might add to the message if the search will be implemented
        add_handle: str = input("Enter A Players Handle To Add Them: \n") #TODO: This is just a basic input

        self.tui.save_input("Player To Add: " + add_handle)

        if...: #TODO: check if player is found and is not in a team
            message: str = f"The Player {add_handle} Was Found, Do You Want To Add Them To Your Team? Y/N:"
            print(self.tui.table(menu, user_path, info, {}, message))

            choice: str = self.utility._prompt_choice(["y", "n"])

            if choice == "n":
                message: str = "Operation Cancelled"
                print(self.tui.table(menu, user_path, info, options, message))
                choice: str = self.utility._prompt_choice(["c"])
                return MenuOptions.edit_team

            #TODO: save the player to the team

            message: str = f"{add_handle} Has Been Added To Your Team!"
            print(self.tui.table(menu, user_path, info, options, message))
            choice: str = self.utility._prompt_choice(["c"])
            return MenuOptions.edit_team
        

        message: str = f"The Player {add_handle} Was Not Found, Do You Want To Try Again? Y/N:"
        print(self.tui.table(menu, user_path, info, {}, message))

        choice: str = self.utility._prompt_choice(["y", "n"])

        if choice == "n":
            return MenuOptions.edit_team
        
        return MenuOptions.add_player



    def remove_player(self) -> MenuOptions:
        """Remove player from team screen, choices: input player handle to remove

        Returns:
            MenuOptions: The next menu to navigate to
        """

        menu: str = "Remove Player"
        user_path: list = [MenuOptions.player_screen, MenuOptions.my_team_not_empty, MenuOptions.edit_team, 
                           MenuOptions.remove_player]
        info: list[str]= [f"""- - - -{"TEAMNAME"}- - - -
{self.underscore + "Rank:" + self.reset}{self.underscore + "Handle:": >21}
{self.reset + "Captain"}{"PLAYERHANDLE": >20}
{"Player"} {"PLAYERHANDLE": >20}
{"Player"} {"PLAYERHANDLE": >20}"""]
        options: dict = {"c": "Continue"}
        message: str = ""

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, ))
        remove_handle: str = input("Enter A Players Handle To Remove Them: \n") #TODO: This is just a basic input

        if...: #TODO: check if player is found and is not in a team
            message: str = f"The Player {remove_handle} Was Found, Do You Want To Remove Them From Your Team? Y/N:"
            print(self.tui.table(menu, user_path, info, {}, message))

            choice: str = self.utility._prompt_choice(["y", "n"])

            if choice == "n":
                message: str = "Operation Cancelled"
                print(self.tui.table(menu, user_path, info, options, message))
                choice: str = self.utility._prompt_choice(["c"])
                return MenuOptions.edit_team

            #TODO: save the player to the team

            message: str = f"{remove_handle} Has Been Removed From Your Team!"
            print(self.tui.table(menu, user_path, info, options, message))
            choice: str = self.utility._prompt_choice(["c"])
            return MenuOptions.edit_team
        

        message: str = f"The Player {remove_handle} Was Not Found, Do You Want To Try Again? Y/N:"
        print(self.tui.table(menu, user_path, info, {}, message))

        choice: str = self.utility._prompt_choice(["y", "n"])

        if choice == "n":
            return MenuOptions.edit_team
        
        return MenuOptions.remove_player



    def leave_team(self) -> MenuOptions:
        """Leave team screen, choices: confirm leaving team with y or n and if captain then choose new captain

        Returns:
            MenuOptions: The next menu to navigate to
        """

        menu: str = "Leave Team"
        user_path: list[str] = [MenuOptions.player_screen, MenuOptions.my_team_not_empty, MenuOptions.leave_team]
        info: list[str] = []
        options: dict[str, str] = {"c": "Continue"}
        message: str = f"Are You Sure You Want To Leave {"TEAMNAME"}? Y/N"

        if ...:  # TODO: check if player is captain

            self.tui.clear_saved_data()
            print(self.tui.table(menu, user_path, info, {}, message))
            choice: str = self.utility._prompt_choice(["y", "n"])

            if choice == "n":
                message: str = "Operation Canceled"
                print(self.tui.table(menu, user_path, info, options, message))
                choice: str = self.utility._prompt_choice(["c"])
                return MenuOptions.my_team_not_empty

            message: str = "You Have Sucessfully Left The Team!"
            print(self.tui.table(menu, user_path, info, options, message))
            choice: str = self.utility._prompt_choice(["c"])
            return MenuOptions.my_team_empty

        return MenuOptions.my_team_empty
    


    def onion(self) -> MenuOptions:

            """This Program Has Layers"""

            print("""
    ⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
    ⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
    ⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀ 
    ⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀ 
    ⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆ 
    ⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿ 
    ⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀⠀ 
    ⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
    ⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
    ⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
    ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀ 
    ⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀ 
    ⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀ 
    ⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠛⠉
                
                
    Somebody once told me the world is gonna roll me
    I ain't the sharpest tool in the shed
    She was looking kind of dumb with her finger and her thumb
    In the shape of an "L" on her forehead
    Well, the years start comin' and they don't stop comin'
    Fed to the rules and I hit the ground runnin'
    Didn't make sense not to live for fun
    Your brain gets smart, but your head gets dumb
    So much to do, so much to see
    So, what's wrong with taking the backstreets?
    You'll never know if you don't go (go)
    You'll never shine if you don't glow
    Hey now, you're an all-star
    Get your game on, go play
    Hey now, you're a rock star
    Get the show on, get paid
    (And all that glitters is gold)
    Only shootin' stars break the mold
    It's a cool place, and they say it gets colder
    You're bundled up now, wait 'til you get older
    But the meteor men beg to differ
    Judging by the hole in the satellite picture
    The ice we skate is gettin' pretty thin
    The water's gettin' warm, so you might as well swim
    My world's on fire, how 'bout yours?
    That's the way I like it, and I'll never get bored
    Hey now, you're an all-star
    Get your game on, go play
    Hey now, you're a rock star
    Get the show on, get paid
    (All that glitters is gold)
    Only shootin' stars break the mold
    Go for the moon
    (Go, go, go) go for the moon
    (Go, go, go) go for the moon
    Go (go), go for the moon
    Hey now, you're an all-star
    Get your game on, go play
    Hey now, you're a rock star
    Get the show on, get paid
    (And all that glitters is gold)
    Only shooting stars
    Somebody once asked, "Could I spare some change for gas?
    I need to get myself away from this place"
    I said, "Yep, what a concept, I could use a little fuel myself
    And we could all use a little change"
    Well, the years start comin' and they don't stop comin'
    Fed to the rules and I hit the ground runnin'
    Didn't make sense not to live for fun
    Your brain gets smart, but your head gets dumb
    So much to do, so much to see
    So, what's wrong with taking the backstreets?
    You'll never know if you don't go (go!)
    You'll never shine if you don't glow
    Hey now, you're an all-star
    Get your game on, go play
    Hey now, you're a rock star
    Get the show on, get paid
    (And all that glitters is gold)
    Only shootin' stars break the mold
    Only shootin' stars break the mold
    Go for the moon
    Go for the moon
    Go for the moon
    This is how we do it
                    
                    """)
            

            a = input()
            if a == "GET OUTTA MA SWAMP!":
                return MenuOptions.start_screen
            
            return MenuOptions.onion
            

    def masterpiece(self) -> MenuOptions:
        """I think Gylfi will like this one"""


        print("""
                                   MMMMMMMMMMM                                         
                                 MMMMMMMMMMMMMMMMM                                      
                             NMMMMMMMMMMMMMMMMMMMMMMMM                                  
                          MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM                              
                        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN                          
                        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM                         
                        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM                        
                        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMD                       
                       DMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM                       
                       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM                       
                       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM                       
                      MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM                      
                      MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM                      
                     MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN                     
                    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN         
                    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN     
                    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN   
NM                  MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMM              MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM 
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMM8MMMMMMMMMIMMMMM8,. ...........OMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMM ..N. .....MMMM...............:MMMMNMMMMMMMMMMMMMMMMMMMMMMM
    NMMMMMMMMMMMMMMMMMMMMM.....:..DMMMMMNZ Z.... .......M$MMMMMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMNMMMMMMM....... 7=MMMMMMO....Z .......MM7MMMMMMMMMMMMMMMMMMMMMMMMM 
            MMMMMMMMMMMMMMMMM  Z...MMMZ .. .,M..,........MMMMMMMMMMMMMMMMMMMMMMMMMMMM 
                MMMMMM.......DOM ....N7..................MMMMMMMMMMMMMMMMMMMMMMMMMMM
                    MMM....... M. ... .  ... ..............M...$MMMMMMMMMMMMMMMMMMMM
                    ........... ......... ..............M..=....+MMMMMMMMMMMMMM
                    ......+.NMI........ . ..............M.,.I...MMMMMMMMMMMMMMN
                    ......$... ...... O..................,.....$MMMMMMMMMMMMN
                    .....M.......... M M.. .............. 8  .OMMMMMMMMMMMN
                    ..=7I,,.,,IMI...M.................. ..MMMMMMMMMMM
                    ....DMMMMMMMMMMMMMMMO..............D...MMMMMMMMM
                        .MMMMMMMMMMMMMMDDMM:,N..............DMMMMMMMMMMM
                        NMMMMMNMM8 . .... ...,............  MMMMMMMMM
                        MMMMM,:......::..M8M8MM...............MMMMMM
                        MMMM ... . .........,MM..............MMMMMO$
                        MMMMM... =.=. .. . . MM ....... . ...MMMMMMM
                        NMMMMMMMMMM?  ..O.?NM7 ....... ......MMMMMM
                        NMMMMMMMMMMMMMMMMM........  $ . ...MMMNMMM
                        MMMMMMMMMMMMMMM.........,, ......MMMMMMMM
                            OMMMMMMMM8 , .. .. .,N.... ...:MMMMMMMMMMN
                            MMMMMMMM?N. ...MD.:MNI8MMMMMMMMMMMMMMMMMN
                        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
                    NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
                    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
                MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
            MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
            NMMMMMMMMMMMMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
            MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM

            
            """)
        print("""
            ⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣷⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀
            ⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠟
            ⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⡆⠀⠀⠀⠀⢠⣶⡿⠟⠻⢿⣦⡀⠀⠀⣠⣾⠿⠛⠿⣷⣄⠀⠀⢠⣶⡿⠟⠻⢿⣦⡀⠀⢠⣾⠟⠛⠻⠷⠀⠀⢸⡇
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⣸⣿⠀⠀⠀⠀⣿⠏⠀⠀⠀⠀⢹⣿⠀⢸⣿⣁⣀⣀⣀⣈⣿⡆⠀⣿⠏⠀⠀⠀⠀⢹⣿⠀⠸⣿⣤⣀⣀⡀⠀⠀⢸⡇
            ⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⢀⣴⣿⣿⠀⠀⠀⢠⣿⡄⠀⠀⠀⠀⣸⣿⠀⢸⣿⡋⠉⠛⠛⢛⠉⠁⢀⣿⡆⠀⠀⠀⠀⣸⣿⠀⠀⠀⠉⠉⠛⣿⡆⠀⢸⡇
            ⠸⣿⣿⣿⣿⡿⠟⠉⠀⠀⢀⣀⣤⣶⣿⣿⣿⠇⠀⠀⠀⢸⣿⠿⣶⣤⣤⣾⠟⠁⠀⠀⠙⢿⣶⣤⣶⡿⠗⠀⢈⣿⠻⣶⣤⣤⣾⠟⠁⠀⠺⢷⣦⣤⣶⡿⠃⠀⢸⡇
            ⠀⠙⢛⣋⣥⣤⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠈⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠈⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠈⠉⠛⠛⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")




        like = input("Do you like my art? Y/N 	⤜(ⱺ ʖ̯ⱺ)⤏ \n")

    
        if like.lower() == "y":
            print("YAY")
            a = input("BYE BYE ⊂(◉‿◉)つ")
            return MenuOptions.start_screen
    
        elif like.lower() != "n":
            MenuOptions.start_screen
    
        return MenuOptions.quit

