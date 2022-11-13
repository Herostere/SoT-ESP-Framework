"""
@Author https://github.com/DougTheDruid
@Source https://github.com/DougTheDruid/SoT-ESP-Framework
"""


ships = {
    # ------------ SHIPS / AI SHIPS ------------
    "BP_SmallShipTemplate_C": {
        "Name": "Sloop (Near)",
    },
    "BP_SmallShipNetProxy_C": {
        "Name": "Sloop",
    },

    "BP_MediumShipTemplate_C": {
        "Name": "Brig (Near)",
    },
    "BP_MediumShipNetProxy_C": {
        "Name": "Brig",
    },

    "BP_LargeShipTemplate_C": {
        "Name": "Galleon (Near)",
    },
    "BP_LargeShipNetProxy_C": {
        "Name": "Galleon",
    },

    "BP_AISmallShipTemplate_C": {
        "Name": "Skeleton Sloop (Near)",
    },
    "BP_AISmallShipNetProxy_C": {
        "Name": "Skeleton Sloop",
    },
    "BP_AILargeShipTemplate_C": {
        "Name": "Skeleton Galleon (Near)",
    },
    "BP_AILargeShipNetProxy_C": {
        "Name": "Skeleton Galleon",
    },
    # "BP_AggressiveGhostShip_C": {
    #     "Name": "Flameheart Galleon",
    # },  # To implement, must modify ship.py's update method for visibility
}
athena = {
    "BP_BountyRewardSkullItemInfo_Mythical_C": {
        "Name": "Skull",
    }
}
events = {
    "BP_SkellyShip_ShipCloud_C": {
        "Name": "Skelly Ship",
    },
    "BP_SkellyFort_SkullCloud_C": {
        "Name": "Skelly Fort",
    },
    "BP_AshenLord_SkullCloud_C": {
        "Name": "Fire Tornado",
    },
    "BP_LegendSkellyFort_SkullCloud_C": {
        "Name": "Fort of Fortune",
    },
    "": {
        "Name": "",
    },
    "": {
        "Name": "",
    },
    "": {
        "Name": "",
    },
}

ship_keys = set(ships.keys())
athena_keys = set(athena.keys())
event_keys = set(events.keys())
