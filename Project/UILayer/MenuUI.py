"""
Author: Ísak Elí Hauksson <isak25@ru.is>
Date: 2025-12-03

File that holds all the menus
"""
#from LogicLayer.LogicLayerAPI import LogicAPI

class MenuUI:
# def __init__(self, logic_api: LogicAPI) -> None:
    def __init__(self, logic_api) -> None:
        # TODO: Initialize the logic api
        self.logic_api = logic_api

    def _prompt_choice(self, valid_choices: list[str]) -> str:
        valid_choices_lower: list[str] = [x.lower() for x in valid_choices]

        while True:
            choice: str = input("-> ").strip().lower()
            if choice in valid_choices_lower:
                return choice
            
            else: print("not a valid option try again")


