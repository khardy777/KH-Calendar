EVENT_RULES = {

    "CPI": {

        "aliases": [
            "CPI m/m",
            "Consumer Price Index",
            "CPI MoM"
        ],

        "priority": "Critical",
        "group": "Inflation",
        "holiday": False
    },


    "Core CPI": {

        "aliases": [
            "Core CPI m/m",
            "Core Consumer Price Index",
            "Core CPI"
        ],

        "priority": "Critical",
        "group": "Inflation",
        "holiday": False
    },


    "Non-Farm Payrolls": {

        "aliases": [
            "Non-Farm Employment Change",
            "Non Farm Payrolls",
            "NFP"
        ],

        "priority": "Critical",
        "group": "Employment",
        "holiday": False
    },


    "Retail Sales": {

        "aliases": [
            "Retail Sales m/m",
            "Retail Sales"
        ],

        "priority": "Important",
        "group": "Consumer",
        "holiday": False
    }

}