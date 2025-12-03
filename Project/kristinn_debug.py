from Models.Player import Player
import DataLayer.DataLayerAPI as dlapi

from uuid import uuid4

uuid = str(uuid4())

p = Player(uuid,
           "Kristinn Hrafn",
           "2006-07-13",
           "hraunbraut 43",
           "kristinnd25@ru.is",
           "855-2006",
           "kiddi",
           "",)

dlapi.store_player(p)

dlapi.update_player(uuid, "home_address", "brog 36")
