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
    "BP_TreasureArtifact_ItemInfo_piratelegendimpressive_03_a_C": {
        "Name": "Relic 1",
    },
    "BP_BountyRewardSkullItemInfo_PirateLegendUncommon_C": {
        "Name": "Villainous Skull",
    },
    "BP_MerchantCrate_CommonPirateLegend_ItemInfo_C": {
        "Name": "Crate",
    },
    "BP_trs_jar_leg_01_a_ItemInfo_C": {
        "Name": "Jar",
    },
    "BP_trs_impressive__leg_01_a_proxy_C": {
        "Name": "Relic 2",
    },
    "BP_trs_box_leg_01_a_Proxy_C": {
        "Name": "Box",
    },
    "BP_TreasureChest_ItemInfo_PirateLegend_C": {
        "Name": "Chest",
    },
    "BP_Treasure_Artifact_Proxy_piratelegendgoblet_02_a_C": {
        "Name": "Chalice"
    },
    "": {
        "Name": "Skull Blessing",
    },
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
    # "BP_PhantomTornado_C": {
    #     "Name": "Phantom Tornado",
    # },  TODO Add athena event
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
