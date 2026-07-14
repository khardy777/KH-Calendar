def export_pine(events, filename="output/tradingview_calendar.txt"):

    with open(filename, "w", encoding="utf-8") as f:

        for event in events:

            start = (
                int(event.risk_start.timestamp() * 1000)
                if event.risk_start
                else 0
            )

            end = (
                int(event.risk_end.timestamp() * 1000)
                if event.risk_end
                else 0
            )

            line = (
                f"{start},"
                f"{end},"
                f"{event.kh_name},"
                f"{event.priority},"
                f"{event.group}"
            )

            f.write(line + "\n")


    print(
        f"Exported {len(events)} Pine events to {filename}"
    )