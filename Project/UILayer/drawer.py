"""404 Andri Not Found"""
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
        self.EXTRABOLD = self.BOLD + "\033[37m"

        self.banner_border = REDHIGH
        self.path_color = RED



    def clear(self) -> None:
        "Clears the system"

        os.system("cls" if os.name == "nt" else "clear")



    def banner(self) -> str:
        "Prints the banner"


        return f"""{self.banner_border}
————————————————————————————————————————————————————————————————————————————————{self.RESET}
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
                                         /____/                             
{self.banner_border}————————————————————————————————————————————————————————————————————————————————{self.RESET}"""
    


    def table_create(self):
        "Creates the UI tables"
    

    def table_print(self):
        "Prints the UI table"







test = Drawer()

a = "" 

while a != "0":
    test.clear()
    print(test.banner())
    a = input()



 
