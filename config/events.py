EVENT_RULES = {

    "CPI": {

        "aliases": [
            "CPI m/m",
            "Consumer Price Index"
        ],

        "priority": "Critical",
        "group": "Inflation",
        "stop_before": 15,
        "stop_after": 5
    },

    "Core CPI": {

        "aliases": [
            "Core CPI m/m",
            "Core Consumer Price Index"
        ],

        "priority": "Critical",
        "group": "Inflation",
        "stop_before": 15,
        "stop_after": 5
    },


    "PPI": {

        "aliases": [
            "PPI m/m",
            "Core PPI m/m",
            "Producer Price Index",
            "PPI MoM"
        ],

        "priority": "Critical",
        "group": "Inflation",
        "stop_before": 15,
        "stop_after": 5
    },


    "NFP": {

        "aliases": [
            "Non-Farm Employment Change",
            "Non Farm Payrolls",
            "NFP"
        ],

        "priority": "Critical",
        "group": "Employment",
        "stop_before": 15,
        "stop_after": 5
    },


    "Unemployment Rate": {

        "aliases": [
            "Unemployment Rate"
        ],

        "priority": "Important",
        "group": "Employment",
        "stop_before": 3,
        "stop_after": 5
    },


    "JOLTS": {

        "aliases": [
            "JOLTS Job Openings",
            "JOLTS"
        ],

        "priority": "Important",
        "group": "Employment",
        "stop_before": 3,
        "stop_after": 5
    },


    "Interest": {

        "aliases": [
            "Fed Interest Rate Decision",
            "Federal Funds Rate"
        ],

        "priority": "Critical",
        "group": "Interest Rates",
        "stop_before": 15,
        "stop_after": 5
    },


    "Fed": {

        "aliases": [
            "Fed Press Conference",
            "FOMC Press Conference"
        ],

        "priority": "Critical",
        "group": "Interest Rates",
        "stop_before": 3,
        "stop_after": 5
    },


    "Jobless Claims": {

        "aliases": [
            "Initial Jobless Claims"
        ],

        "priority": "Important",
        "group": "Employment",
        "stop_before": 3,
        "stop_after": 5
    },


    "GDP": {

        "aliases": [
            "GDP Growth Rate QoQ Final",
            "GDP m/m",
            "Advance GDP q/q"
        ],

        "priority": "Important",
        "group": "GDP",
        "stop_before": 3,
        "stop_after": 5
    },


    "PMI": {

        "aliases": [
            "ISM Manufacturing PMI",
            "ISM Services PMI"
        ],

        "priority": "Important",
        "group": "PMI",
        "stop_before": 3,
        "stop_after": 5
    }

}