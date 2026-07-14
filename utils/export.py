import json


def export_calendar(events, filename="output/kh_calendar.json"):

    data = []

    for event in events:

        item = {

            "event": event.kh_name,

            "source_event": event.event,

            "currency": event.currency,

            "priority": event.priority,

            "group": event.group,

            "risk_start": (
                event.risk_start.strftime("%Y-%m-%d %H:%M")
                if event.risk_start
                else None
            ),

            "risk_end": (
                event.risk_end.strftime("%Y-%m-%d %H:%M")
                if event.risk_end
                else None
            )

        }

        data.append(item)


    with open(filename, "w", encoding="utf-8") as f:

        json.dump(
            data,
            f,
            indent=4
        )


    print(f"Exported {len(data)} events to {filename}")