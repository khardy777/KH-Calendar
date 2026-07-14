"""
KH Calendar Builder
Main Entry Point

Author: Kim
"""
from utils.export import export_calendar
from utils.tradingview_export import export_tradingview
from utils.pine_export import export_pine
from pathlib import Path

from parser import load_calendar

from classifier import classify

def main():

    csv_file = Path("input/samples/calendar.csv")

    events = load_calendar(csv_file)
    for event in events:
        classify(event)
        from utils.risk_window import calculate_risk_window
        calculate_risk_window(event)

    export_calendar(events)
    export_tradingview(events)
    export_pine(events)

    print(f"Loaded {len(events)} events\n")

    for event in events:
        #print(event)

        print(
            event,
            "| Risk:",
            event.risk_start,
            "-",
            event.risk_end
        )


if __name__ == "__main__":
    main()