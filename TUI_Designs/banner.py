import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


REDHIGH = "\033[41m"
BLUE = "\033[34m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
PINK = "\033[35m"
CYAN = "\033[36m"

RESET = "\033[0m"
BOLD = "\033[1m"
EXTRABOLD = "\033[37m"

banner_border = REDHIGH
path_color = RED

user_path = "AdminPage -> CreateTournament"
table = "Insert super duper extra fantastic cool table here"


clear()
print("\n" + banner_border + BOLD +
"————————————————————————————————————————————————————————————————————————————————" + RESET + BOLD +
"""
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
""" + REDHIGH +
"————————————————————————————————————————————————————————————————————————————————" + RESET + "\n")


print(BOLD + "HELLO WORLD THIS IS BOLD")
print(EXTRABOLD + "HELLO WORLD THIS IS EXTRA BOLD")


print( 
"\n" +"* User Path *" + "\n" + path_color + user_path + RESET)
print(EXTRABOLD + table + RESET)