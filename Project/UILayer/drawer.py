"""
Author: Andri Már Kristjánsson <andrik25@ru.is>
Date: 2025-12-04

File that takes in table info, creates the table and can clear the terminal

takes 5 arguments:
     table name, user path, table info, table options, message to be displayed
"""
import os

class Drawer():

    def __init__(self) -> None:
        "Initializes the class"
        

        #Colours
        RED = "\033[31m"
        REDHIGH = "\033[41m"
        GREEN = "\033[32m"
        YELLOW = "\033[33m"        
        BLUE = "\033[34m"
        PINK = "\033[35m"
        CYAN = "\033[36m"


        #Text change
        self.RESET = "\033[0m"
        self.BOLD = "\033[1m"
        self.BRIGHTER = "\033[37m"

        self.banner_border = REDHIGH
        self.path_color = RED
        self.table_color = self.BRIGHTER + BLUE



    def clear(self) -> None:
        "Clears the terminal"

        os.system("cls" if os.name == "nt" else "clear")



    def banner(self) -> str:
        "Prints the banner"


        return f"""{self.banner_border}
————————————————————————————————————————————————————————————————————————————————{self.RESET}                                           
            ▗▖ ▗▖▗▄▄▖                 ▗▄▖                          
            ▐▌ ▐▌▐▛▀▜▌               ▗▛▀▜                 ▐▌       
            ▐▌ ▐▌▐▌ ▐▌      ▟█▙      ▐▙   ▐▙█▙  ▟█▙  █▟█▌▐███ ▗▟██▖
            ▐███▌▐███      ▐▙▄▟▌      ▜█▙ ▐▛ ▜▌▐▛ ▜▌ █▘   ▐▌  ▐▙▄▖▘
            ▐▌ ▐▌▐▌▝█▖     ▐▛▀▀▘ ██▌    ▜▌▐▌ ▐▌▐▌ ▐▌ █    ▐▌   ▀▀█▖
            ▐▌ ▐▌▐▌ ▐▌     ▝█▄▄▌     ▐▄▄▟▘▐█▄█▘▝█▄█▘ █    ▐▙▄ ▐▄▄▟▌
            ▝▘ ▝▘▝▘ ▝▀      ▝▀▀       ▀▀▘ ▐▌▀▘  ▝▀▘  ▀     ▀▀  ▀▀▀ 
                                          ▐▌                                                                     
                                                                
            ▗▄▄▄▖                      █                           
            ▐▛▀▀▘      ▐▌              ▀                           
            ▐▌   ▝█ █▘▐███  ▟██▖▐▙ ▟▌ ██   ▟█▟▌ ▟██▖▐▙██▖▐███▌ ▟██▖
            ▐███  ▐█▌  ▐▌   ▘▄▟▌ █ █   █  ▐▛ ▜▌ ▘▄▟▌▐▛ ▐▌  ▗▛  ▘▄▟▌
            ▐▌    ▗█▖  ▐▌  ▗█▀▜▌ ▜▄▛   █  ▐▌ ▐▌▗█▀▜▌▐▌ ▐▌ ▗▛  ▗█▀▜▌
            ▐▙▄▄▖ ▟▀▙  ▐▙▄ ▐▙▄█▌ ▐█▌ ▗▄█▄▖▝█▄█▌▐▙▄█▌▐▌ ▐▌▗█▄▄▖▐▙▄█▌
            ▝▀▀▀▘▝▀ ▀▘  ▀▀  ▀▀▝▘  ▀  ▝▀▀▀▘   ▐▌ ▀▀▝▘▝▘ ▝▘▝▀▀▀▘ ▀▀▝▘
                                           ▜█▛▘                                          {self.RESET}
{self.banner_border}————————————————————————————————————————————————————————————————————————————————{self.RESET} \n\n"""
    


    def table(self, table_name, table_path = [], table_info = [], table_options = [], message = "") -> str:
        "Creates and returns the UI tables"

        self.clear()
        print(self.banner())


        table = """"""
        path = ""
        line = "————————————————————————————————————————————————————————————————————————————————" + "\n"

        if table_path:
            path += table_path[0]
            for step in table_path[1:]:
                path += " -> " + step


            table += path + "\n"
            table += line
            
        table += f"{table_name: ^80}" + "\n"
        table += line

        if table_info:
            for info in table_info:
                table += info + "\n"

            table += line


        if message:
            table += message + "\n"
            table += line


        if table_options:
            for option in table_options:
                table += option + "\n"

            table += line
            table += "Choose Action:"



        return self.table_color + table + self.RESET









