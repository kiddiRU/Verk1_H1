"""
Author: Andri Már Kristjánsson <andrik25@ru.is>
Date: 2025-12-04

File that takes in table info, creates the table and can clear the terminal, 
also can save previous user inputs that need to be displayed on the table

takes 5 arguments:
     table name, user path, table info, table options, message to be displayed
"""

import os
from UILayer.MenuOptions import MenuOptions # Imported for type hinting


class Drawer():
    """Draws TUI tables and banner"""

    def __init__(self) -> None:
        """Initializes the class"""

        self.previous_inputs: list[str] = []

        # Codes frot the colors that will be used in the table
        red: str = "\033[31m"
        red_high: str = "\033[41m"
        green: str = "\033[32m"
        yellow: str = "\033[33m"

        # Codes that will be used to change the text
        self.reset: str = "\033[0m"
        self.bold: str = "\033[1m"

        self.banner_border: str = red_high
        self.logo_color: str = red
        self.table_color: str = self.bold
        self.options_color: str = self.bold + green
        self.message_color: str = self.bold + yellow

        self.line: str = 80 * "—" + "\n"

    def clear(self) -> None:
        """Clears the terminal

        :returns:
            Nothing
        """
        # Use the os import to check what system the user uses and run the appropriate clear command
        os.system("cls" if os.name == "nt" else "clear")

    def banner(self) -> str:
        """Creates the banner

        :returns:
            A tripple quoted format string that holds the colored banner
        """

        # Creates the banner with the appropriate colors
        banner = f"""{self.banner_border}
{self.line}{self.reset}

        ▄▄▄   ▄▄▄ ▄▄▄▄▄▄▄                  ▄▄▄▄▄▄▄                                 
        ███   ███ ███▀▀███▄               █████▀▀▀                    ██           
        █████████ ███▄▄███▀   ▄█▀█▄        ▀████▄  ████▄ ▄███▄ ████▄ ▀██▀▀         
        ███▀▀▀███ ███▀▀██▄    ██▄█▀ ▀▀▀▀▀    ▀████ ██ ██ ██ ██ ██ ▀▀  ██           
        ███   ███ ███  ▀███   ▀█▄▄▄       ███████▀ ████▀ ▀███▀ ██     ██           
                                                   ██                              
                                                   ▀▀                              

    ▄▄▄▄▄▄▄                                                                   
    ███▀▀▀▀▀        ██                                                         
    ███▄▄    ██ ██ ▀██▀▀ ████▄  ▀▀█▄ ██ ██  ▀▀█▄ ▄████  ▀▀█▄ ████▄ ▀▀▀██  ▀▀█▄ 
    ███       ███   ██   ██ ▀▀ ▄█▀██ ██▄██ ▄█▀██ ██ ██ ▄█▀██ ██ ██   ▄█▀ ▄█▀██ 
    ▀███████ ██ ██  ██   ██    ▀█▄██  ▀█▀  ▀█▄██ ▀████ ▀█▄██ ██ ██ ▄██▄▄ ▀█▄██ 
                                                    ██                         
                                                  ▀▀▀                          
{self.reset}
{self.banner_border}{self.line}{self.reset} \n\n"""

        return banner

    def table(self, menu: str, user_path: list[MenuOptions] = [], info: list[str] = [], 
              options: dict[str, str] = {}, message: str = "") -> str:
        """Creates the TUI tables

        :param menu:
            String of the name of the table
        :type menu: str
            
        :param user_path:
            List of the users previous screens
        :type user_path: list[MenuOptions]

        :param info:
            List of all the info that will be printed in the table
        :type info: list[str]
            
        :param options:
            Dictionary of all the input options that the user has and what action they correspond to
        :type options: dict[str, str]

        :param message:
            String of the message that will be printed in the table
        :type message: str

        :returns:
            A tripple quoted format string that hold the table 
            and all the information from the parameters

        """


        self.clear()

        # Create an empty string that will position the table a little from the top of the string
        # and hold the entirety of the table as a string
        table: str = "\n\n\n"

        # Create an empty sting that will be concatinated with the path
        # so that it can be printed as a string
        path: str = ""

        # Adds all the path steps to a string
        # and adds an arrow in front of all steps exept for the first one
        if user_path:
            path += user_path[0]
            for step in user_path[1:]:
                path += " -> " + step

            # Adds the path and a line to the table
            table += path + "\n"
            table += self.line

        # Formats the table name so that is is int he middle of the table
        # and adds it to the table along with a line to seperate the information
        table += f"{menu: ^80}" + "\n"
        table += self.line

        # If there are any previous inputs saved, they are added to the table along with a line
        if self.previous_inputs:
            for previous_info in self.previous_inputs:
                table += previous_info + "\n"

            table += self.line

        # Info is added line by line to the table
        if info:
            for i in info:
                table += i + "\n"

            table += self.line

        # If there is a message, it is colored yellow and added to the table
        if message:
            table += self.message_color + message + self.reset + "\n"
            table += self.line

        # Options are colored green
        # and added to the table with a space between the key and value in the dictionary
        if options:
            for opt, option in options.items():
                table += self.options_color + opt + " " + option + "\n"

            table += self.reset + self.line
            table += self.options_color + "Choose Action:" + self.reset


        # Makes the table bold and returns it
        return self.table_color + table + self.reset

    def start_table(self, menu: str, user_path: list[MenuOptions] = [], options: dict[str, str] = {}) -> str:
        """Creates the TUI table for the start screen

        :param menu:
            String of the name of the table
        :type menu: str
            
        :param user_path:
            List of the users previous screens
        :type user_path: list[MenuOptions]
            
        :param options:
            Dictionary of all the input options that the user has and what action they correspond to
        :type options: dict[str, str]

        :returns:
            A tripple quoted format string that hold the table 
            and all the information from the parameters

        """


        self.clear()
        print(self.banner())

        # Create an empty string that will hold the entirety of the table as a string
        table: str = ""

        # Create an empty sting that will be concatinated with the path
        # so that it can be printed as a string
        path: str = ""

        # Adds all the path steps to a string
        # and adds an arrow in front of all steps exept for the first one
        if user_path:
            path += user_path[0]
            for step in user_path[1:]:
                path += " -> " + step

            table += path + "\n"
            table += self.line

        # Formats the table name so that is is int he middle of the table
        # and adds it to the table along with a line to seperate the information
        table += f"{menu: ^80}" + "\n"
        table += self.line


        # Options are colored green
        # and added to the table with a space between the key and value in the dictionary
        if options:
            for opt, option in options.items():
                table += self.options_color + opt + " " + option + "\n"

            table += self.reset + self.line
            table += self.options_color + "Choose Action:" + self.reset


        # Makes the table bold and returns it
        return self.table_color + table + self.reset

    def save_input(self, user_input: str) -> None:
        """Saves data so that it will be printed at the top of the table
        
        :param user_input:
            String of the info that is to be printed on top of the table along with the user input
            ex. (Name: USERINPUT)
        :type user_input: str

        :return:
            Nothing
        """

        # Saves the info and user input in a string that is then used when creating a table
        self.previous_inputs.append(user_input)

    def discard_last_input(self):
        """Discards the previous input from the user
        
        :return:
            Nothing
        """

        # Pops the last user input so that it can be changed
        self.previous_inputs.pop()

    def clear_saved_data(self) -> None:
        """Clears all the date that has been saved in the drawer
        
        :return:
            Nothing
        """

        # Clears all the previous inputs so that they dont print in other tables
        self.previous_inputs.clear()
