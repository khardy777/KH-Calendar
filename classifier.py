from config.events import EVENT_RULES

def classify(news):

    rules = sorted(
        EVENT_RULES.items(),
        key=lambda x: max(len(alias) for alias in x[1]["aliases"]),
        reverse=True
    )

    for name, rule in rules:

        aliases = sorted(
            rule["aliases"],
            key=len,
            reverse=True
        )

        for alias in aliases:

            if alias.lower() in news.event.lower():

                news.kh_name = name
                news.priority = rule["priority"]
                news.group = rule["group"]
                news.stop_before = rule.get("stop_before", 0)
                news.stop_after = rule.get("stop_after", 0)
                news.holiday = rule.get("holiday", False)

                return news

    return news