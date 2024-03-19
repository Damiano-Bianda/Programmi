class Season:
    def __init__(self, data):
        self.data = data
        self.match_days_count = round_values = len({item["league"]["round"] for item in data})