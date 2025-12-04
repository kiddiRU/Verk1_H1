from Models import Player
import DataLayer.DataLayerAPI as dlapi

from LogicLayer import LogicLayerAPI, PlayerLL

from uuid import uuid4

uuid = str(uuid4())

for p in dlapi.load_players():
    print(p.name)

# Store player með data layer
#
# p = Player(uuid,
#            "Kristinn Hrafn",
#            "2006-07-13",
#            "hraunbraut 43",
#            "kristinnd25@ru.is",
#            "855-2006",
#            "kiddi",
#            "",)
# dlapi.store_player(p)
# dlapi.update_player(uuid, "home_address", "brog 36")


# Bua til player i gegnum playerLL
#
# p = PlayerLL()
# p.create_player(
#     "Kristinn Hrafn",
#     "2006-07-13",
#     "hraunbraut 43",
#     "kristinnd25@ru.is",
#     "855-2006",
#     "kiddi",
#     ""
# )


# Bua til player i gegnum LogicLayerAPI
#
# LogicLayerAPI.create_player(
#     "Kristinn Hrafn",
#     "2006-07-13",
#     "hraunbraut 43",
#     "kristinnd25@ru.is",
#     "855-2006",
#     "kiddi",
#     ""
# )