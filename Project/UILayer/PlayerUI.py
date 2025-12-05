"""
Author: Ísak Elí Hauksson <isak25@ru.is>
Date: 2025-12-04
Co-author: Andri Már Kristjá.nsson <andrik25@ru.is>

File that holds all the menus that the player can access
"""

from UILayer.MenuOptions import MenuOptions
from UILayer.UtilityUI import UtilityUI
from UILayer.Drawer import Drawer


class PlayerUI:
    """Every player menu option"""

    def __init__(self) -> None:
        self.utility = UtilityUI()
        self.tui = Drawer()

    def start_screen(self) -> MenuOptions:
        """Start screen with choices: 1, 2, 3 and q
        1: go to login screen
        2: go to register screen
        3: go to spectating screen
        1: quit program

        Returns:
            MenuOptions: The next menu to navigate to
        """
        menu: str = "Start Screen"
        user_path: list[str]= [MenuOptions.start_screen]
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

        menu: str = "Login"
        user_path: list[str]= ["StartScreen", "Login"]
        info: list[str]= []
        options: dict[str, str]= {}
        message: str = ""

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options, message))        

        choice: str = self.utility._input_info("Input Your Handle: ")

        if choice == "admin":
            return MenuOptions.admin_screen

        # TODO: check if handle exists from LL API
        # if choice in Player_list:
        #     return MenuOption.player_screen

        return MenuOptions.quit

    def register_screen(self) -> MenuOptions:
        """Register screen, choices: fill info with input

        Returns:
            MenuOptions: The next menu to navigate to
        """
        # TODO: add fill in option  
        
        menu: str = "Register"
        user_path: list[str]= ["StartScreen", "Login", "Register"]
        info: list[str]= []
        options: dict[str, str]= {"c": "Continue"}
        message: str = "You Have Created A Player!"

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info))  
        self.choice_name: str = input("Enter Name: \n")
        self.tui.save_input("Name: " + self.choice_name)
        print(self.tui.table(menu, user_path, info, options))  
        con = input()

        print(self.tui.table(menu, user_path, info)) 
        self.choice_dob: str = input("Enter Date Of Birth: \n")
        self.tui.save_input("Date Of Birth: " + self.choice_dob)
        print(self.tui.table(menu, user_path, info, options))
        con = input()

        print(self.tui.table(menu, user_path, info)) 
        self.choice_addr: str = input("Enter Home Adderess: \n")
        self.tui.save_input("Home Address: " + self.choice_addr)
        print(self.tui.table(menu, user_path, info, options))
        con = input()  

        print(self.tui.table(menu, user_path, info))
        self.choice_email: str = input("Enter Email: \n")
        self.tui.save_input("Email: " + self.choice_email)
        print(self.tui.table(menu, user_path, info, options))
        con = input()  

        print(self.tui.table(menu, user_path, info))   
        self.choice_pnum: str = input("Enter Phone Number: \n")
        self.tui.save_input("Phone Number: " + self.choice_pnum)
        print(self.tui.table(menu, user_path, info, options))
        con = input()  

        print(self.tui.table(menu, user_path, info))   
        self.choice_handle: str = input("Enter Handle: \n")
        self.tui.save_input("Handle: " + self.choice_handle)
        print(self.tui.table(menu, user_path, info, options, message))
        con = input()  

        
        #if register
        return MenuOptions.player_screen
        #if cancel: return MenuOptions.start_screen

    def player_screen(self) -> MenuOptions:
        """Player screen, choices: 1,2,3 and b
        1: Edit info
        2: See team
        3: Create a team
        b: back to main menu

        Returns:
            MenuOptions: The next menu to navigate to
        """
        

        menu: str = "Player Screen"
        user_path: list[str]= ["StartScreen", "PlayerScreen"]

        #Temporary info for testing, needs to get info from the actual info files
        info: list[str]= [f"""Name: {self.choice_name}
Date of Birth: {self.choice_dob}
Home Address: {self.choice_addr}
Phone Number: {self.choice_pnum}
Email: {self.choice_email}
Handle: {self.choice_handle}
Team: NONE
Club: NONE
Rank: Player"""]
        
        options: dict[str, str]= {"1": "Edit Info", "2": "My Team", "3": "Create a Team", "q": "Log Out"}
        message: str = ""

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path, info, options, message))

        choice: str = self.utility._prompt_choice(["1", "2", "3", "q"])
        match choice:
            case "1":
                return MenuOptions.edit_player_info
            case "2":
                # if ...:  # TODO: check if team is empty aka if player not in a team
                #     return MenuOptions.my_team_not_empty
                return MenuOptions.my_team_empty
            case "3":
                # if ...:  # TODO: check if player is already in a team
                #     print("You are already in a team")
                #     return MenuOptions.player_screen
                return MenuOptions.create_team
            case "q":
                return MenuOptions.quit


        return MenuOptions.start_screen
    
    def create_team(self) -> MenuOptions:
        """Create team screen, choices: fill info with input

        Returns:
            MenuOptions: The next menu to navigate to
        """
        
        menu: str = "Create Team"
        user_path: list[str]= ["PlayerScreen -> CreateTeam"]

        #temporary info
        info: list[str]= ["""- - - -List Of Clubs- - - -
Club1
Club2
Club3
Club4"""]
        
        options: dict[str, str]= {"c": "Continue", "b": "Back"}
        message: str = "By Creating A Team You Are Assigned As The Captain Of It!"

        self.tui.clear_saved_data()
        print(self.tui.table(menu, user_path))
        choice_tname: str = input("Enter Team Name: \n")
        self.tui.save_input("Team Name: " + choice_tname)

        print(self.tui.table(menu, user_path))
        choice_url: str = input("Enter Team URL (Optional): \n")
        self.tui.save_input("Team Name: " + choice_url)

        print(self.tui.table(menu, user_path))
        choice_ascii: str = input("Enter Team ASCII Art (Optional): \n")
        self.tui.save_input("Team ASCII Art: " + choice_ascii)

        print(self.tui.table(menu, user_path, info))
        choice_club = input("Choose A Club To Join: \n")
        self.tui.save_input("Club: " + choice_club)

        print(self.tui.table(menu, user_path, info, options, message))
        con = input()


        

        return MenuOptions.player_screen

    def edit_player_info(self) -> MenuOptions:
        """Edit player info screen, choices: fill info with input

        Returns:
            MenuOptions: The next menu to navigate to
        """

        # This Uses A temporary way to print out and change info


        menu: str = "Edit Player Info"
        user_path: list[str]= ["PlayerScreen", "EditPlayerInfo"]
        info: list[str]= []
        options: dict[str, str]= {"c": "Continue", "b": "Back"}
        message: str = "You Have Changed Your Info!"

        self.tui.clear_saved_data()
        self.tui.save_input(f"- - - -{self.choice_name}- - - -")
        unchanged_message = "(Leave Field Empty If You Want To Leave Them Unchanged)"    

        print(self.tui.table(menu, user_path, info))
        self.choice_newname = input(unchanged_message + "\n Enter New Name: \n")
        if self.choice_newname:
            self.choice_name = self.choice_newname
        self.tui.save_input("Name: " + self.choice_name)

        print(self.tui.table(menu, user_path, info))
        self.choice_newdob = input(unchanged_message + "\n Enter New Date Of Birth: \n")
        if self.choice_newdob:
            self.choice_dob = self.choice_newdob
        self.tui.save_input("Date Of Birth: " + self.choice_dob)

        print(self.tui.table(menu, user_path, info))        
        self.choice_newaddr = input(unchanged_message + "\n Enter New Home Address: \n")
        if self.choice_newaddr:
            self.choice_addr = self.choice_newaddr
        self.tui.save_input("Home Address: " + self.choice_addr)

        print(self.tui.table(menu, user_path, info))
        self.choice_newpnum = input(unchanged_message + "\n Enter New Phone Number: \n")
        if self.choice_newpnum:
            self.choice_pnum = self.choice_newpnum
        self.tui.save_input("Phone Number: " + self.choice_pnum)

        print(self.tui.table(menu, user_path, info))
        self.choice_newemail = input(unchanged_message + "\n Enter New Email: \n")
        if self.choice_newemail:
            self.choice_email = self.choice_newemail
        self.tui.save_input("Email: " + self.choice_email)

        
        print(self.tui.table(menu, user_path, info, options, message))

        
        return MenuOptions.player_screen
    
    def my_team_empty(self) -> MenuOptions:
        """My team screen when team is empty, choices: b to go back

        Returns:
            MenuOptions: The next menu to navigate to
        """

        menu: str = "My Team"
        user_path: list[str]= ["PlayerScreen", "MyTeam"]
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
        b: back to player screen

        Returns:
            MenuOptions: The next menu to navigate to
        """
        print("This is your team screen")
        choice: str = self.utility._prompt_choice(["1", "2", "b"])
        match choice:
            case "1":
                return MenuOptions.edit_team
            case "2":
                if ...:  # TODO: check if player is captain
                    return MenuOptions.leave_team
            case "b":
                return MenuOptions.my_team_not_empty
        return MenuOptions.player_screen
    
    def edit_team(self) -> MenuOptions:
        """Edit team screen, choices: 1,2 and b
        1: Add player to team
        2: Remove player from team
        b: back to My Team

        Returns:
            MenuOptions: The next menu to navigate to
        """
        print("This is the edit team screen")
        return MenuOptions.my_team_not_empty
    
    def add_player(self) -> MenuOptions:
        """Add player to team screen, choices: input player handle to add

        Returns:
            MenuOptions: The next menu to navigate to
        """
        print("This is the add player to team screen")
        return MenuOptions.edit_team
    
    def remove_player(self) -> MenuOptions:
        """Remove player from team screen, choices: input player handle to remove

        Returns:
            MenuOptions: The next menu to navigate to
        """
        print("This is the remove player from team screen")
        return MenuOptions.edit_team
    
    def leave_team(self) -> MenuOptions:
        """Leave team screen, choices: confirm leaving team with y or n and if captain then choose new captain

        Returns:
            MenuOptions: The next menu to navigate to
        """
        print("This is the leave team screen")
        if ...:  # TODO: check if player is captain
            print("You are the captain, please choose a new captain before leaving")

        return MenuOptions.player_screen