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



class PlayerUI:
    """Every player menu option"""

    def __init__(self) -> None:
        self.utility = UtilityUI()
        self.tui = Drawer()
        self.input_color = "\033[36m"
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
        user_path: list[MenuOptions] = [MenuOptions.start_screen]
        options: dict[str, str]= {"1": "Log in", "2": "Register", "3": "Spectate", "q": "Quit program"}

        self.tui.clear_saved_data()
        print(self.tui.start_table(menu, user_path, options))  


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

        """ THIS IS TEMPORARY REMOVE LATER"""
        player_list = LogicLayerAPI.list_players()
        abc: str = 1

        menu: str = "Log In"
        user_path: list[MenuOptions] = [MenuOptions.start_screen, 
                                        MenuOptions.login]
        info: list[str]= []
        options: dict[str, str]= {"t": "Try Again", "b": "Back"}
        message: str = "Handle Not Found!"
     
        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info))

        login_handle: str = input(self.input_color + "Input Your Handle: " + self.reset)

        user_uuid = LogicLayerAPI.get_player_uuid(login_handle)
        if user_uuid:
            LogicLayerAPI.save_player(login_handle)
            return MenuOptions.player_screen  
        
        match login_handle:
            case "admin":
                return MenuOptions.admin_screen
            case "Shrek":
                return MenuOptions.onion
            case "masterpiece":
                return MenuOptions.masterpiece
        
        print(self.tui.table(menu, user_path, info, options, message))

        """ THIS IS TEMPORARY REMOVE LATER """
        if login_handle == "handle list":
            AAAA: int = 1
            abc: str = 1
            for player in player_list:
                print(player.handle)

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
        user_path: list[MenuOptions] = [MenuOptions.start_screen, 
                                        MenuOptions.register]
        info: list[str]= []
        options: dict[str, str]= {"c": "Continue", "b": "Back"}
        message: str = "You Have Created A Player!"


        # Python complained if i did not do this
        user_name = ""
        user_dob = ""
        user_addr = ""
        user_email = ""
        user_phnum = ""
        user_handle = ""
        user_url = ""

        self.tui.clear_saved_data()

        con = "b"
        while con == "b":
            print(self.tui.table(menu, user_path, info))  
            user_name: str = self.utility._input_info("Enter Name or 'q' to cancel: \n", "name", "PLAYER")
            if not user_name: 
                return user_path[-2]
            self.tui.save_input("Name: " + user_name)

            print(self.tui.table(menu, user_path, info, options)) 
            con: str = self.utility._prompt_choice(["c", "b"])
            if con == "b":
                self.tui.discard_last_input()

        con = "b"
        while con == "b":
            print(self.tui.table(menu, user_path, info)) 
            user_dob: str = str(self.utility._input_info("Enter Date Of Birth or 'q' to cancel: \n (yyyy-mm-dd) \n", 
                                                         "date_of_birth", "PLAYER"))
            if not user_dob: 
                return user_path[-2]
            self.tui.save_input("Date Of Birth: " + str(user_dob))

            print(self.tui.table(menu, user_path, info, options))  
            con: str = self.utility._prompt_choice(["c", "b"])
            if con == "b":
                self.tui.discard_last_input()

        con = "b"
        while con == "b":
            print(self.tui.table(menu, user_path, info)) 
            user_addr: str = self.utility._input_info("Enter Home Address or 'q' to cancel: \n (Streetname 00 Cityname) \n", 
                                                    "home_address", "PLAYER")
            if not user_addr: 
                return user_path[-2]
            self.tui.save_input("Home Address: " + user_addr)

            print(self.tui.table(menu, user_path, info, options))  
            con: str = self.utility._prompt_choice(["c", "b"])
            if con == "b":
                self.tui.discard_last_input()

        con = "b"
        while con == "b":
            print(self.tui.table(menu, user_path, info))
            user_email: str = self.utility._input_info("Enter Email or 'q' to cancel: \n", "email", "PLAYER")
            if not user_email: 
                return user_path[-2]
            self.tui.save_input("Email: " + user_email)

            print(self.tui.table(menu, user_path, info, options))
            con: str = self.utility._prompt_choice(["c", "b"])
            if con == "b":
                self.tui.discard_last_input()

        con = "b"
        while con == "b":
            print(self.tui.table(menu, user_path, info))   
            user_phnum: str = self.utility._input_info("Enter Phone Number or 'q' to cancel: \n (123-4567) \n", 
                                                       "phone_number", "PLAYER")
            if not user_phnum: 
                return user_path[-2]
            self.tui.save_input("Phone Number: " + user_phnum)

            print(self.tui.table(menu, user_path, info, options))  
            con: str = self.utility._prompt_choice(["c", "b"])
            if con == "b":
                self.tui.discard_last_input()

        con = "b"
        while con == "b":
            print(self.tui.table(menu, user_path, info))   
            user_handle: str = self.utility._input_info("Enter Handle or 'q' to cancel:  \n", "handle", "PLAYER")
            if not user_handle: 
                return user_path[-2]
            self.tui.save_input("Handle: " + user_handle)

            print(self.tui.table(menu, user_path, info, options))  
            con: str = self.utility._prompt_choice(["c", "b"])
            if con == "b":
                self.tui.discard_last_input()

        con = "b"
        while con == "b":
            print(self.tui.table(menu, user_path, info))   
            user_url: str = input(self.input_color + 
                                  "Enter URL or 'q' to cancel: \n(Optional, Press Enter To Leave Blank) \n" 
                                  + self.reset)
            if user_url.lower() == "q": 
                return user_path[-2]
            self.tui.save_input("URL: " + user_url)
            print(self.tui.table(menu, user_path, info, options))

            print(self.tui.table(menu, user_path, info, options))  
            con: str = self.utility._prompt_choice(["c", "b"])
            if con == "b":
                self.tui.discard_last_input()

        options: dict[str, str]= {"c": "Save Info And Continue", "b": "Discard Info And Go Back"}
        print(self.tui.table(menu, user_path, info, options, message))
        con: str = self.utility._prompt_choice(["c", "b"])

        if con == "b":
            return MenuOptions.start_screen

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
        
        # Change into string so that Vs Wont complain about type hinting
        current_login_handle: str = str(LogicLayerAPI.save_player())
        current_login_uuid = LogicLayerAPI.get_player_uuid(current_login_handle)
        player: Player | str = LogicLayerAPI.get_player_object(current_login_uuid)
        team, rank = LogicLayerAPI.get_player_team(current_login_handle)
        club = LogicLayerAPI.get_team_club(team)

        if not team:
            team = None
            rank = "Player"
            club = None

        # Need to make sure that no variable can be unbound so that VS code wont complain
        if type(player) is Player:
            current_login_name = player.name
            current_login_dob = player.date_of_birth
            current_login_addr = player.home_address
            current_login_phnum = player.phone_number
            current_login_email = player.email
            current_login_url = player.url
            current_login_team = team
            current_login_club = club
            current_login_rank = rank


        else:
            current_login_name = None
            current_login_dob = None
            current_login_addr = None
            current_login_phnum = None
            current_login_email = None
            current_login_url = None
            current_login_team = None
            current_login_club = None
            current_login_rank = "Player"


        menu: str = "Player Page"
        user_path: list[MenuOptions] = [MenuOptions.player_screen]

        #Temporary info for testing, needs to get info from the actual info files
        info: list[str]= [f"""Handle: {current_login_handle}
Name: {current_login_name}
Date of Birth: {current_login_dob}
Home Address: {current_login_addr}
Phone Number: {current_login_phnum}
Email: {current_login_email}
URL: {current_login_url}
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
                if not team:
                    return MenuOptions.my_team_empty
                return MenuOptions.my_team_not_empty
            case "3":
                if not team:
                    return MenuOptions.create_team_in_team
                return MenuOptions.create_team
            case "lo":
                return MenuOptions.logout


        return MenuOptions.start_screen
    


    def create_team(self) -> MenuOptions:
        """Create team screen, choices: fill info with input

        Returns:
            MenuOptions: The next menu to navigate to
        """

        current_login_handle: str | None = LogicLayerAPI.save_player()
        player_list: list[Player] = LogicLayerAPI.list_players()


        # VS Code complains if i dont do this
        team_name: str | None = ""
        team_captain: Player = player_list[0]
        team_club: str = ""
        team_url: str = ""
        team_ascii: str = ""


        for player in player_list:
            if player.handle == current_login_handle:
                team_captain: Player = player


        menu: str = "Create Team"
        user_path: list[MenuOptions] = [MenuOptions.player_screen, 
                                        MenuOptions.create_team]

        #temporary info
        info: list[str]= ["- - - -List Of Clubs- - - -"]
        
        options: dict[str, str] = {"c": "Continue", "b": "Back"}
        message: str = "By Creating A Team You Are Assigned As The Captain Of It!"


        clubs = LogicLayerAPI.list_clubs()
        club_names = [x.name for x in clubs]
        for club in club_names:
            info.append(club)
            

        con = "b"
        while con == "b":
            self.tui.clear_saved_data()
            print(self.tui.table(menu, user_path, [], {}, message))
            team_name: str | None = self.utility._input_info("Enter Team Name or 'q' to cancel: : \n", "name", "TEAM")
            if not team_name:
                return user_path[-2]
            self.tui.save_input("Team Name: " + team_name)

            print(self.tui.table(menu, user_path, [], options)) 
            con: str = self.utility._prompt_choice(["c", "b"])
            if con == "b":
                self.tui.discard_last_input()


        con = "b"
        while con == "b":
            print(self.tui.table(menu, user_path))
            team_url: str = input(self.input_color + "Enter Team URL (Optional): \n" + self.reset)
            self.tui.save_input("Team Url: " + team_url)

            print(self.tui.table(menu, user_path, [], options)) 
            con: str = self.utility._prompt_choice(["c", "b"])
            if con == "b":
                self.tui.discard_last_input()


        con = "b"
        while con == "b":
            print(self.tui.table(menu, user_path))
            team_ascii: str = input(self.input_color + "Enter A Single Line Team ASCII Art (Optional): \n" + self.reset)
            self.tui.save_input("Team ASCII Art: " + team_ascii)

            print(self.tui.table(menu, user_path, [], options)) 
            con: str = self.utility._prompt_choice(["c", "b"])
            if con == "b":
                self.tui.discard_last_input()

            message = ""
            while team_club not in club_names:
                print(self.tui.table(menu, user_path, info, {}, message))
                team_club: str = input(self.input_color + "Choose A Club To Join: \n" + self.reset) #TODO: This is just a basic input
                if team_club not in club_names:
                    print(self.tui.table(menu, user_path, info, options, message))
                    message = f"{team_club} Does Not Exist Or Is Not Available"
                
                else:
                    self.tui.save_input("Club: " + team_club)

                    print(self.tui.table(menu, user_path, [], options)) 
                    con: str = self.utility._prompt_choice(["c", "b"])
                    if con == "b":
                        self.tui.discard_last_input()

        options: dict[str, str] = {"c": "Save Info And Continue", "b": "Discard Info And Go Back"}
        message = f"You Have Created A Team!"
        print(self.tui.table(menu, user_path, [], options, message))
        choice: str = self.utility._prompt_choice(["c", "b"])
        
        if choice == "c":
            LogicLayerAPI.create_team(team_name, team_captain, team_club, team_url, team_ascii)

            return MenuOptions.my_team_not_empty
        
 
        return MenuOptions.player_screen



    def edit_player_info(self) -> MenuOptions:
        """Edit player info screen, choices: fill info with input

        Returns:
            MenuOptions: The next menu to navigate to
        """

        current_login_handle: str | None = LogicLayerAPI.save_player()
        if type(current_login_handle) is str:
            login_uuid: str = LogicLayerAPI.get_player_uuid(current_login_handle)
        else: 
            login_uuid: str  = "" # This should never run, this is just to apease the type hinting gods

        current_player: Player | str = LogicLayerAPI.get_player_object(login_uuid)

        if type(current_player) is Player:
            name: str = current_player.name
            dob: str  = current_player.date_of_birth
            addr: str  = current_player.home_address
            email: str  = current_player.email
            phnum: str  = current_player.phone_number
            handle: str  = current_player.handle
            url: str  = current_player.url

        # This should never run, this is just to apease the type hinting gods
        else:
            return MenuOptions.player_screen


        menu: str = "Edit Player Info"
        user_path: list[MenuOptions] = [MenuOptions.player_screen, 
                                        MenuOptions.edit_player_info]
        info: list[str]= []
        options: dict[str, str]= {"c": "Continue", "b": "Back"}
        message: str = "You Have Changed Your Info!"

        self.tui.clear_saved_data()
        unchanged_message = "(Leave Field Empty If You Want To Leave Them Unchanged)"    


        con = "b"
        while con == "b":
            print(self.tui.table(menu, user_path, info))
            new_name = self.utility._input_change(unchanged_message + "\n Enter New Name or 'q' to cancel: \n",
                                                   "name", "PLAYER")
            if new_name == "q":
                return user_path[-2]
            if new_name:
                name = new_name

            self.tui.save_input("Name: " + name)
            print(self.tui.table(menu, user_path, [], options)) 
            con: str = self.utility._prompt_choice(["c", "b"])
            if con == "b":
                self.tui.discard_last_input()

        con = "b"
        while con == "b":
            print(self.tui.table(menu, user_path, info))
            new_handle = self.utility._input_change(unchanged_message + "\n Enter New Handle or 'q' to cancel: \n", 
                                                  "handle", "PLAYER")
            if new_handle == "q":
                return user_path[-2]
            if new_handle:
                handle = new_handle

            self.tui.save_input("Handle: " + handle)
            print(self.tui.table(menu, user_path, [], options)) 
            con: str = self.utility._prompt_choice(["c", "b"])
            if con == "b":
                self.tui.discard_last_input()

        con = "b"
        while con == "b":
            print(self.tui.table(menu, user_path, info))
            new_dob = self.utility._input_change(unchanged_message + "\n Enter New Date Of Birth or 'q' to cancel: \n", 
                                               "date_of_birt", "PLAYER")
            if new_dob == "q":
                return user_path[-2]
            if new_dob:
                dob = new_dob

            self.tui.save_input("Date Of Birth: " + dob)
            print(self.tui.table(menu, user_path, [], options)) 
            con: str = self.utility._prompt_choice(["c", "b"])
            if con == "b":
                self.tui.discard_last_input()

        con = "b"
        while con == "b":
            print(self.tui.table(menu, user_path, info))        
            new_addr = self.utility._input_change(unchanged_message + "\n Enter New Home Address or 'q' to cancel: \n", 
                                                "home_address", "PLAYER")
            if new_addr == "q":
                return user_path[-2]
            if new_addr:
                addr = new_addr
                
            self.tui.save_input("Home Address: " + addr)
            print(self.tui.table(menu, user_path, [], options)) 
            con: str = self.utility._prompt_choice(["c", "b"])
            if con == "b":
                self.tui.discard_last_input()

        con = "b"
        while con == "b":
            print(self.tui.table(menu, user_path, info))
            new_phnum = self.utility._input_change(unchanged_message + "\n Enter New Phone Number or 'q' to cancel: \n", 
                                                 "phone_number", "PLAYER")
            if new_phnum == "q":
                return user_path[-2]
            if new_phnum:
                phnum = new_phnum

            self.tui.save_input("Phone Number: " + phnum)
            print(self.tui.table(menu, user_path, [], options)) 
            con: str = self.utility._prompt_choice(["c", "b"])
            if con == "b":
                self.tui.discard_last_input()

        con = "b"
        while con == "b":
            print(self.tui.table(menu, user_path, info))
            new_email = self.utility._input_change(unchanged_message + "\n Enter New Email or 'q' to cancel: \n", 
                                                 "email", "PLAYER")
            if new_email == "q":
                return user_path[-2]
            if new_email:
                email = new_email

            self.tui.save_input("Email: " + email)
            print(self.tui.table(menu, user_path, [], options)) 
            con: str = self.utility._prompt_choice(["c", "b"])
            if con == "b":
                self.tui.discard_last_input()

        con = "b"
        while con == "b":
            print(self.tui.table(menu, user_path, info))
            new_url = input(unchanged_message + self.input_color + "\n Enter New URL or 'q' to cancel: \n" + self.reset)

            if new_url == "q":
                return user_path[-2]
            if new_url:
                url = new_url
            
            self.tui.save_input("URL: " + url)
            print(self.tui.table(menu, user_path, [], options)) 
            con: str = self.utility._prompt_choice(["c", "b"])
            if con == "b":
                self.tui.discard_last_input()
        

        options: dict[str, str] = {"c": "Save Info And Continue", "b": "Discard Info And Go Back"}
        print(self.tui.table(menu, user_path, [], options, message))
        choice: str = self.utility._prompt_choice(["c", "b"])
        
        if choice == "c":
            LogicLayerAPI.update_player_info(current_player, name, dob, addr, email, phnum, handle, url)
            LogicLayerAPI.save_player(handle)
        
        return MenuOptions.player_screen
    


    def my_team_empty(self) -> MenuOptions:
        """My team screen when team is empty, choices: b to go back

        Returns:
            MenuOptions: The next menu to navigate to
        """

        menu: str = "My Team"
        user_path: list[MenuOptions] = [MenuOptions.player_screen, 
                                        MenuOptions.my_team_empty]
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

        current_login_handle: str = str(LogicLayerAPI.save_player())
        team, rank = LogicLayerAPI.get_player_team(current_login_handle)

        team_members = LogicLayerAPI.get_team_members(team)
       
        menu: str = "My Team"
        user_path: list[MenuOptions] = [MenuOptions.player_screen, 
                                        MenuOptions.my_team_not_empty]
        info: list[str]= [f"- - - -{team}- - - -", 
                    f"{self.underscore + "Rank:"} \t \t Handle:{self.reset}"]
        options: dict[str, str]= {"1": "Edit Team", "2": "Leave Team", "b": "Back"}
        message: str = ""

        for member in team_members: 
            player: Player | str = LogicLayerAPI.get_player_object(member)

            if type(player) is Player: # Only there for the type hinting gods
                team, member_rank = LogicLayerAPI.get_player_team(player.handle)

                if member_rank == "Captain":
                    info.append(f"{member_rank} \t {player.handle}")
                else:
                    info.append(f"{member_rank} \t \t {player.handle}")
            
            self.tui.clear_saved_data()

        if rank == "Captain":
            print(self.tui.table(menu, user_path, info, options))
            choice: str = self.utility._prompt_choice(["1", "2", "b"])
            match choice:
                case "1":
                    return MenuOptions.edit_team
                case "2":
                    if ...:  # TODO: check if player is captain
                        return MenuOptions.leave_team
                case "b":

                    return MenuOptions.player_screen
            return MenuOptions.player_screen
        

        options: dict[str, str]= {"1": "Leave Team", "b": "Back"}
        print(self.tui.table(menu, user_path, info, options))
        choice: str = self.utility._prompt_choice(["1", "b"])
        match choice:
            case "1":
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

        current_login_handle: str = str(LogicLayerAPI.save_player())
        player: Player | str = LogicLayerAPI.get_player_object(current_login_handle)
        team, rank = LogicLayerAPI.get_player_team(current_login_handle)

        team_members = LogicLayerAPI.get_team_members(team)

        menu: str = "Edit Team"
        user_path: list[MenuOptions] = [MenuOptions.player_screen, 
                                        MenuOptions.my_team_not_empty, 
                                        MenuOptions.edit_team]
        info: list[str]= [f"- - - -{team}- - - -", 
                    f"{self.underscore + "Rank:"} \t \t Handle:{self.reset}"]
        options: dict[str, str]= {"1": "Add Player To Team", "2": "Remove Player From Team", "b": "Back"}
        message: str = ""

        for member in team_members: 
            player: Player | str = LogicLayerAPI.get_player_object(member)
            
            if type(player) is Player: # Only there for the type hinting gods
                team, member_rank = LogicLayerAPI.get_player_team(player.handle)

                if member_rank == "Captain":
                    info.append(f"{member_rank} \t {player.handle}")
                else:
                    info.append(f"{member_rank} \t \t {player.handle}")
        
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
        user_path: list = [MenuOptions.player_screen, 
                           MenuOptions.my_team_not_empty, 
                           MenuOptions.edit_team, 
                           MenuOptions.add_player]
        info: list = []
        options: dict = {"c": "Continue"}

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path))

        # Might add to the message if the search will be implemented
        add_handle: str = input(self.input_color + "Enter A Players Handle To Add Them: \n" + self.reset)

        self.tui.save_input("Player To Add: " + add_handle)

        add_uuid = LogicLayerAPI.get_player_uuid(add_handle)
        add_in_team = LogicLayerAPI.get_players_team_uuid(add_uuid)
        print(add_uuid, add_in_team)

        if add_uuid and not add_in_team: 
            message: str = f"The Player {add_handle} Was Found \nDo You Want To Add Them To Your Team? Y/N:"
            print(self.tui.table(menu, user_path, info, {}, message))

            choice: str = self.utility._prompt_choice(["y", "n"])

            if choice == "n":
                message: str = "Operation Cancelled"
                print(self.tui.table(menu, user_path, info, options, message))
                choice: str = self.utility._prompt_choice(["c"])
                return MenuOptions.edit_team


            current_login_handle: str = str(LogicLayerAPI.save_player())
            current_login_uuid: str = LogicLayerAPI.get_player_uuid(current_login_handle)
            current_player: Player | str = LogicLayerAPI.get_player_object(current_login_uuid)

            if type(current_player) is Player: # Is Only there for the type hinting gods
                LogicLayerAPI.add_player(add_handle, current_player)


            message: str = f"{add_handle} Has Been Added To Your Team!"
            print(self.tui.table(menu, user_path, info, options, message))
            choice: str = self.utility._prompt_choice(["c"])
            return MenuOptions.edit_team
        

        message: str = f"The Player {add_handle} Was Not Found Or Is Not Available \nDo You Want To Try Again? Y/N:"
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

        current_login_handle: str = str(LogicLayerAPI.save_player())
        current_uuid: str = LogicLayerAPI.get_player_uuid(current_login_handle)
        current_player: Player | str = LogicLayerAPI.get_player_object(current_uuid)

        menu: str = "Remove Player"
        user_path: list = [MenuOptions.player_screen, 
                           MenuOptions.my_team_not_empty, 
                           MenuOptions.edit_team, 
                           MenuOptions.remove_player]
        info: list[str]= []
        options: dict = {"c": "Continue"}
        message: str = ""

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, ))
        remove_handle: str = input(self.input_color + "Enter A Players Handle To Remove Them: \n" + self.reset)


        remove_uuid = LogicLayerAPI.get_player_uuid(remove_handle)
        remove_in_team = LogicLayerAPI.get_players_team_uuid(remove_uuid)
        print(remove_uuid, remove_in_team)

        current_team, rank = LogicLayerAPI.get_player_team(remove_handle)
        remove_player_team, rank = LogicLayerAPI.get_player_team(current_login_handle)

        if current_team == remove_player_team:
            message: str = f"The Player {remove_handle} Was Found \nDo You Want To Remove Them From Your Team? Y/N:"
            print(self.tui.table(menu, user_path, info, {}, message))

            choice: str = self.utility._prompt_choice(["y", "n"])

            if choice == "n":
                message: str = "Operation Cancelled"
                print(self.tui.table(menu, user_path, info, options, message))
                choice: str = self.utility._prompt_choice(["c"])
                return MenuOptions.edit_team

            if type(current_player) is Player:
                LogicLayerAPI.remove_player(remove_handle, current_player)
            message: str = f"{remove_handle} Has Been Removed From Your Team!"
            print(self.tui.table(menu, user_path, info, options, message))
            choice: str = self.utility._prompt_choice(["c"])
            return MenuOptions.edit_team
        

        message: str = f"The Player {remove_handle} Was Not Found Or Is Not Removeable \nDo You Want To Try Again? Y/N:"
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

        current_login_handle: str = str(LogicLayerAPI.save_player())
        current_uuid: str = LogicLayerAPI.get_player_uuid(current_login_handle)
        current_player: Player | str = LogicLayerAPI.get_player_object(current_uuid)
        team, rank = LogicLayerAPI.get_player_team(current_login_handle)

        menu: str = "Leave Team"
        user_path: list[MenuOptions] = [MenuOptions.player_screen, MenuOptions.my_team_not_empty, MenuOptions.leave_team]
        info: list[str] = []
        options: dict[str, str] = {"Y": "Yes", "N": "No"}
        message: str = f"Are You Sure You Want To Leave {team}"

        if rank == "Captain":
            message: str = f"Select A New Captain Before Leaving {team}"
            print(self.tui.table(menu, user_path, info, {}, message))
            new_captain = input(self.input_color + "Enter A Players Handle To Promote Them To Captain: \n" + self.reset)
            current_team, rank = LogicLayerAPI.get_player_team(new_captain)
            new_captain_team, rank = LogicLayerAPI.get_player_team(current_login_handle)

            if current_team == new_captain_team:
                message: str = f"The Player {new_captain} Was Found \nDo You Want To Promote Them To Captain? Y/N:"
                print(self.tui.table(menu, user_path, info, {}, message))

                choice: str = self.utility._prompt_choice(["y", "n"])

                if type(current_player) is Player:
                    if choice == "y":
                        LogicLayerAPI.promote_captain(current_player, new_captain)

                        LogicLayerAPI.remove_player(current_login_handle, current_player)

                        return MenuOptions.player_screen
                    return MenuOptions.edit_team

            message: str = "Player Was Not Found Or Not Available \nDo You Want To Try Again? Y/N:"
            print(self.tui.table(menu, user_path, info, {}, message))
            choice: str = self.utility._prompt_choice(["y", "n"])

            if choice == "n":
                return MenuOptions.edit_team

            return MenuOptions.leave_team


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
    

    def create_team_in_team(self) -> MenuOptions:
        """ Screen That Is Shown When Player In A Team Tries To Create A New Team 

        Returns:
            MenuOptions: The next menu to navigate to
        """
    
        menu: str = "Create A Team"
        user_path: list[MenuOptions] = [MenuOptions.player_screen, 
                                        MenuOptions.create_team_in_team]
        info: list[str]= []
        options: dict[str, str]= {"b": "Back"}
        message: str = "You Are Already In A Team!"
        
        self.tui.clear_saved_data()

        print(self.tui.table(menu, user_path, info, options, message))

        choice: str = self.utility._prompt_choice(["b"])
        match choice:
            case "b":
                return MenuOptions.player_screen
        return MenuOptions.player_screen


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




        like = input(self.input_color + "Do you like my art? Y/N 	⤜(ⱺ ʖ̯ⱺ)⤏ \n" + self.reset)

    
        if like.lower() == "y":
            print("YAY")
            a = input("BYE BYE ⊂(◉‿◉)つ")
            return MenuOptions.start_screen
    
        elif like.lower() != "n":
            MenuOptions.start_screen
    
        print("\033[31m" + "Deleting File And System" + "\033[0m")
        return MenuOptions.quit
