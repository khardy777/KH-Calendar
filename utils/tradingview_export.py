import json


def export_tradingview(events, filename="output/tradingview_calendar.json"):

    data = []

    for event in events:

        item = {

            "event": event.kh_name,

            "priority": event.priority,

            "group": event.group,

            "start": int(event.risk_start.timestamp() * 1000)
                if event.risk_start else None,

            "end": int(event.risk_end.timestamp() * 1000)
                if event.risk_end else None

        }

        data.append(item)


    with open(filename, "w", encoding="utf-8") as f:

        json.dump(
            data,
            f,
            indent=4
        )


    print(
        f"Exported {len(data)} TradingView events to {filename}"
    )