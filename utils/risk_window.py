from datetime import datetime, timedelta


def calculate_risk_window(news):

    event_time = datetime.strptime(
        f"{news.date} {news.time}",
        "%Y-%m-%d %H:%M"
    )

    news.risk_start = (
        event_time -
        timedelta(minutes=news.stop_before)
    )

    news.risk_end = (
        event_time +
        timedelta(minutes=news.stop_after)
    )

    return news