"""
Author: Ísak Elí Hauksson <isak25@ru.is>
Date: 2025-12-03

File that holds all the menus
"""
# from LogicLayer.LogicLayerAPI import LogicAPI

class MenuUI:
    # def __init__(self, logic_api: LogicAPI) -> None:
    def __init__(self, logic_api) -> None:
        self.logic_api = logic_api

    def _prompt_choice(self, valid_choices: list[str]) -> str:
        valid_choices_lower: list[str] = [x.lower() for x in valid_choices]

        while True:
            choice: str = input("-> ").strip().lower()
            if choice in valid_choices_lower:
                return choice
            
            print("not a valid option try again")

    def show_start_screen(self) -> str:
        print("THIS IS THE START SCREEN")
        print(f"1. Login")
        print(f"2. Register")
        print(f"3. Spectate")
        print(f"q. Quit")

        choice: str = self._prompt_choice(["1","2","3","q"])
        if choice == "1":
            return "LOGIN"
        if choice == "2":
            return "REGISTER"
        if choice == "3":
            return "SPECTATE"
        return "Quit"



