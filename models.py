class News:

    def __init__(
        self,
        date,
        time,
        currency,
        event,
        impact
    ):
        self.date = date
        self.time = time
        self.currency = currency
        self.event = event
        self.impact = impact

        self.priority = "Normal"
        self.group = "Unclassified"
        self.kh_name = "Unknown"
        self.holiday = False
        self.stop_before = 0
        self.stop_after = 0
        self.risk_start = None
        self.risk_end = None

    def __str__(self):
        return (
            f"{self.date} | "
            f"{self.time} | "
            f"{self.currency} | "
            f"{self.event} | "
            f"KH={self.kh_name} | "
            f"{self.priority} | "
            f"{self.group}"
        )