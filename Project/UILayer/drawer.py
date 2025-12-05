"""
Author: Andri Már Kristjánsson <andrik25@ru.is>
Date: 2025-12-04

File that takes in table info, creates the table and can clear the terminal, 
also can save previous user inputsthat need to be displayed on the table

takes 5 arguments:
     table name, user path, table info, table options, message to be displayed
"""

import os

class Drawer():

    def __init__(self) -> None:
        """Initializes the class"""
        
        self.previous_inputs: list = []

        #Colours
        RED: str = "\033[31m"
        REDHIGH: str = "\033[41m"
        GREEN: str = "\033[32m"
        YELLOW: str = "\033[33m"        
        BLUE: str = "\033[34m"
        PINK: str = "\033[35m"
        CYAN: str = "\033[36m"


        #Text change
        self.RESET: str = "\033[0m"
        self.BOLD: str = "\033[1m"

        self.banner_border: str = REDHIGH
        self.path_color: str = RED
        self.table_color: str = self.BOLD 

    
        self.line: str = 80 * "—" + "\n"



    def clear(self) -> None:
        "Clears the terminal"

        os.system("cls" if os.name == "nt" else "clear")



    def banner(self) -> str:
        """Prints the banner"""


        return f"""{self.banner_border}
{self.line}{self.RESET}                                           

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
{self.RESET}
{self.banner_border}{self.line}{self.RESET} \n\n"""
    


    def table(self, table_name, table_path = [], table_info = [], table_options = {}, message = "") -> str:
        """Creates and returns the UI tables"""

        self.clear()
        print(self.banner())

        table: str = """"""
        path: str = ""

        if table_path:
            path += table_path[0]
            for step in table_path[1:]:
                path += " -> " + step


            table += path + "\n"
            table += self.line
            
        table += f"{table_name: ^80}" + "\n"
        table += self.line

        if self.previous_inputs:
            for info in self.previous_inputs:
                table += info + "\n"

            table += self.line

        if table_info:
            for i in table_info:
                table += i + "\n"

            table += self.line


        if message:
            table += message + "\n"
            table += self.line


        if table_options:
            for num, option in table_options.items():
                table += str(num) + " " + option + "\n"

            table += self.line
            table += "Choose Action:"



        return self.table_color + table + self.RESET




    def save_input(self, user_input: str) -> list:
        """Saves data so that it will be printed at the top of the table"""

        self.previous_inputs.append(user_input)

        return self.previous_inputs
    





