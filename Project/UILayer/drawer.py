"""
Author: Andri Már Kristjánsson <andrik25@ru.is>
Date: 2025-12-04

File that takes in table info, creates the table and can clear the terminal
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
        self.table_color = self.BRIGHTER + GREEN



    def clear(self) -> None:
        "Clears the terminal"

        os.system("cls" if os.name == "nt" else "clear")



    def banner(self) -> str:
        "Prints the banner"


        return f"""{self.banner_border}
————————————————————————————————————————————————————————————————————————————————{self.RESET}{self.BOLD}{self.BRIGHTER}
                ____  __  __              _____                  __ 
               / __ \/ / / /   ___       / ___/____  ____  _____/ /_
              / /_/ / / / /   / _ \______\__ \/ __ \/ __ \/ ___/ __/
             / _, _/ /_/ /   /  __/_____/__/ / /_/ / /_/ / /  / /_  
            /_/ |_|\____/    \___/     /____/ .___/\____/_/   \__/  
                                           /_/                     
       ______     __                                                               
      / ____/  __/ /__________ __   ______ _____ _____ _____  ____  ____ _         
     / __/ | |/ / __/ ___/ __ `/ | / / __ `/ __ `/ __ `/ __ \/_  / / __ `/         
    / /___ >  </ /_/ /  / /_/ /| |/ / /_/ / /_/ / /_/ / / / / / /_/ /_/ /          
   /_____/_/|_|\__/_/   \__,_/ |___/\__,_/\__, /\__,_/_/ /_/ /___/\__,_/           
                                         /____/                             {self.RESET}
{self.banner_border}————————————————————————————————————————————————————————————————————————————————{self.RESET} \n\n"""
    


    def table(self, table_name, table_path = [], table_info = [], table_options = []) -> str:
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

        if table_options:
            for option in table_options:
                table += option + "\n"

            table += line
            table += "Choose Action:"
            


        return self.table_color + table + self.RESET









