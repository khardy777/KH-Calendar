import csv

from models import News


def load_calendar(csv_file):

    events = []

    with open(csv_file, newline="", encoding="utf-8-sig") as file:

        for line in file:

            line = line.strip()

            # Remove Excel quotes
            line = line.strip('"')

            parts = line.split(",")

            # Skip header row
            if parts[0] == "Date":
                continue

            news = News(
                date=parts[0],
                time=parts[1],
                currency=parts[2],
                event=parts[3],
                impact=parts[4]
            )

            events.append(news)

    return events