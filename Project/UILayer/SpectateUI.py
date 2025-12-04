"""
Author: Ísak Elí Hauksson <isak25@ru.is>
Date: 2025-12-04

File that holds all the menus that the spectator can access
"""

from UILayer.MenuOptions import MenuOptions
from UILayer.UtilityUI import UtilityUI

class SpectateUI:
    """ Every spectate menu option """

    def __init__(self) -> None:
        self.utility = UtilityUI()