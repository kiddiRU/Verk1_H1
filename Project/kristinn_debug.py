from Models.Player import Player
import DataLayer.DataLayerAPI as dlapi


p = Player("Kristinn Hrafn",
           "2006-07-13",
           "hraunbraut 43",
           "kristinnd25@ru.is",
           "855-2006",
           "kiddi",
           "",)

dlapi.store_player(p)
